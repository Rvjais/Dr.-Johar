import os, shutil

targets = [
    '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
    '6ce732e',
    'latest'
]

js_src = '6ce732e63260f60c0203ef7caa72248ad6fedf5c/assets/js/krtam-gsap.js'

gsap_scripts = '''<!-- GSAP & ScrollTrigger Animation Suite -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="assets/js/krtam-gsap.js"></script>
'''

for t in targets:
    # 1. Copy JS
    t_js_dir = os.path.join(t, 'assets', 'js')
    os.makedirs(t_js_dir, exist_ok=True)
    t_js = os.path.join(t_js_dir, 'krtam-gsap.js')
    if t != '6ce732e63260f60c0203ef7caa72248ad6fedf5c':
        shutil.copy2(js_src, t_js)

    # 2. Update CSS for Team photo: no crop, full scaling
    css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    css = css.replace(
'''team__photo {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.05);
  display: block;
}''',
'''team__photo {
  max-width: 100%;
  height: auto;
  max-height: 380px;
  object-fit: contain;
  border-radius: 12px;
  box-shadow: 0 6px 24px rgba(0,0,0,0.06);
  display: block;
}'''
    )
    # Also handle alternate styling if present
    css = css.replace(
'''team__visual {
  width: 100%;
}''',
'''team__visual {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}'''
    )

    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)
    print(f'Updated CSS in {css_file}')

    # 3. Update HTML to include GSAP scripts before </body>
    html_file = os.path.join(t, 'index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'krtam-gsap.js' not in html:
        html = html.replace('</body>', gsap_scripts + '</body>')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Added GSAP scripts to {html_file}')

print('ALL DONE!')

