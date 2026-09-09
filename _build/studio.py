"""Apply the Studio design to current pages without regenerating clinical copy.

Run `python _build/studio.py` from the site folder after editing templates.
The original content builder also calls apply_design for future builds.
"""
from pathlib import Path
import re

SITE_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = Path(__file__).resolve().parent / 'templates'
PATHS = {
    'arrow': 'M7 17 17 7M7 7h10v10',
    'caret': 'm6 9 6 6 6-6',
    'close': 'm6 6 12 12M6 18 18 6',
    'phone': 'M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.5 2.7.7a2 2 0 0 1 1.9 2.1z',
    'chat': 'M21 11.5a8.5 8.5 0 0 1-12.4 7.6L3 21l1.9-5.6A8.5 8.5 0 1 1 21 11.5Z',
    'up': 'M12 19V5m-6 6 6-6 6 6',
    'down': 'M12 5v14m-6-6 6 6 6-6',
    'check': 'm5 12 4 4L19 6',
    'spark': 'm12 2 2.8 7.2L22 12l-7.2 2.8L12 22l-2.8-7.2L2 12l7.2-2.8Z',
    'heart': 'M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z',
    'play': 'm9 5 11 7-11 7Z',
}

def template(name, root=''):
    content = (TEMPLATES / (name + '.html')).read_text(encoding='utf-8')
    content = content.replace('{{root}}', root)
    for key, value in PATHS.items():
        icon = f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="{value}"/></svg>'
        content = content.replace('{{' + key + '}}', icon)
    return content

def redesign_intro(body):
    pattern = r'<section class="page-hero([^"]*)">\s*(<img\b[^>]*class="page-hero__bg"[^>]*>)?\s*<div class="container">(.*?)</div></section>'
    def replace(match):
        classes, image, content = match.groups()
        if 'page-intro-layout' in content or not image or 'page-hero__grid' in content:
            return match.group(0)
        image = image.replace('class="page-hero__bg"', 'class="intro-image"')
        return f'<section class="page-hero{classes} studio-page-intro"><div class="container"><div class="page-intro-layout"><div class="page-intro-copy">{content}</div><div class="page-intro-photo">{image}</div></div></div></section>'
    return re.sub(pattern, replace, body, count=1, flags=re.S)

def apply_design(content, relative):
    relative = str(relative).replace('\\', '/')
    root = '../' * (len(Path(relative).parts) - 1)
    head = content.split('<body', 1)[0]
    if not head.endswith('\n'): head += '\n'
    main_match = re.search(r'<main\b[^>]*>(.*?)</main>', content, re.S)
    if not main_match:
        raise ValueError(f'Missing main element: {relative}')
    body = (template('home') if relative == 'index.html' else redesign_intro(main_match.group(1))).strip()
    mode = 'studio-home' if relative == 'index.html' else 'studio-interior'
    head = re.sub(r'<link\b[^>]*href="https://fonts.googleapis.com/css2[^>]*>', '', head)
    head = re.sub(r'<link\b[^>]*href="[^"]*assets/css/studio.css[^>]*>', '', head)
    head = re.sub(r'assets/css/style.css(?:\?[^"\s]*)?', 'assets/css/style.css?v=studio-2', head)
    head = re.sub(r'<meta name="theme-color" content="[^"]*">', '<meta name="theme-color" content="#29262e">', head)
    head = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', head)
    resources = '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">\n'
    resources += f'<link rel="stylesheet" href="{root}assets/css/studio.css?v=studio-2">\n'
    head = head.replace('</head>', resources + '</head>')
    if relative == 'index.html':
        head = re.sub(r'<title>.*?</title>', '<title>Kratam | Plastic Surgery & Aesthetic Care with Dr. Manoj Johar</title>', head)
    # Normalize only the shared shell; existing inner-page content stays intact.
    result = head + f'<body class="{mode}">\n' + template('header', root)
    result += '\n<main id="main-content">\n' + body + '\n</main>\n' + template('footer', root) + '\n</body>\n</html>\n'
    return result

if __name__ == '__main__':
    pages = [p for p in SITE_ROOT.rglob('*.html') if '_build' not in p.relative_to(SITE_ROOT).parts and '.git' not in p.parts]
    for page in pages:
        relative = page.relative_to(SITE_ROOT)
        original = page.read_text(encoding='utf-8')
        updated = apply_design(original, relative)
        if original != updated:
            page.write_text(updated, encoding='utf-8')
    print(f'Applied Studio design to {len(pages)} pages.')
