import os
import sys
import json
import subprocess
import datetime
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VERSIONS_FILE = os.path.join(BASE_DIR, 'versions.json')
INDEX_FILE = os.path.join(BASE_DIR, 'index.html')
VERCEL_FILE = os.path.join(BASE_DIR, 'vercel.json')

def load_versions():
    if not os.path.exists(VERSIONS_FILE):
        return []
    with open(VERSIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_versions(versions):
    with open(VERSIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(versions, f, indent=2)

def update_vercel_json():
    config = {
        'version': 2,
        'cleanUrls': True,
        'trailingSlash': True,
        'headers': [
            {
                'source': '/(.*)',
                'headers': [
                    {'key': 'Cache-Control', 'value': 'public, max-age=0, must-revalidate'}
                ]
            }
        ]
    }
    with open(VERCEL_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print('[+] Updated vercel.json.')

def build_portal_html(versions):
    cards_html = []
    for v in versions:
        is_latest = v.get('is_latest', False)
        badge_class = 'latest' if is_latest else 'archived'
        badge_text = 'Active Latest' if is_latest else 'Archived'
        card_class = 'version-card is-latest' if is_latest else 'version-card'
        commit = v.get('commit', '')
        short_hash = v.get('short_hash', commit[:7])
        title = v.get('title', 'Version ' + short_hash)
        desc = v.get('description', 'Snapshot commit.')
        branch = v.get('branch', 'main')
        date_str = v.get('date', '')

        primary_btn = f'<a href="/{short_hash}/" class="btn btn-primary btn-card">Launch Version (/{short_hash}/)</a>' if is_latest else f'<a href="/{short_hash}/" class="btn btn-sub btn-card">Launch Version (/{short_hash}/)</a>'

        card = f'''      <div class="{card_class}">
        <div class="card-header">
          <span class="status-badge {badge_class}">{badge_text}</span>
          <span class="commit-meta">{short_hash}</span>
        </div>
        <h3 class="card-title">{title}</h3>
        <p class="card-desc">{desc}</p>
        <div class="card-details">
          <div class="detail-row"><span>Branch</span><strong>{branch}</strong></div>
          <div class="detail-row"><span>Short Hash</span><code>/{short_hash}/</code></div>
          <div class="detail-row"><span>Full SHA</span><code>{commit[:10]}...{commit[-4:]}</code></div>
          <div class="detail-row"><span>Date</span><span>{date_str}</span></div>
        </div>
        <div class="card-actions">
          {primary_btn}
          <a href="/{commit}/" class="btn btn-sub btn-card" title="Launch via full commit SHA">Full SHA &rarr;</a>
        </div>
      </div>'''
        cards_html.append(card)

    cards_joined = '\n\n'.join(cards_html)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dr. Johar &amp; Kratam — Version Archive &amp; Deployment Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0d1117;
      --card-bg: #161b22;
      --card-border: #30363d;
      --accent: #238636;
      --accent-hover: #2ea043;
      --gold: #d4af37;
      --text: #c9d1d9;
      --text-white: #f0f6fc;
      --text-muted: #8b949e;
      --code-bg: #0d1117;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: rgba(22, 27, 34, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-white);
      font-weight: 700;
      font-size: 1.15rem;
    }}
    .brand-badge {{
      background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%);
      color: #000;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }}
    .hero {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 56px 24px 32px;
      text-align: center;
    }}
    .hero h1 {{
      font-size: clamp(2rem, 5vw, 2.75rem);
      font-weight: 800;
      color: var(--text-white);
      letter-spacing: -0.5px;
      margin-bottom: 14px;
    }}
    .hero p {{
      font-size: 1.1rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 28px;
    }}
    .hero-actions {{
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }}
    .btn-primary {{
      background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(35, 134, 54, 0.35);
    }}
    .btn-primary:hover {{
      background: #2ea043;
      transform: translateY(-1px);
    }}
    .main-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 20px 24px 60px;
      flex: 1;
      width: 100%;
    }}
    .section-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .section-title span {{
      background: var(--card-border);
      color: var(--text-muted);
      font-size: 0.8rem;
      padding: 2px 8px;
      border-radius: 12px;
    }}
    .versions-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }}
    .version-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.25s ease;
    }}
    .version-card:hover {{
      border-color: #58a6ff;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }}
    .version-card.is-latest {{
      border-color: rgba(35, 134, 54, 0.6);
      background: linear-gradient(180deg, rgba(35, 134, 54, 0.06) 0%, var(--card-bg) 60px);
    }}
    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}
    .status-badge {{
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .status-badge.latest {{
      background: rgba(35, 134, 54, 0.2);
      color: #3fb950;
      border: 1px solid rgba(35, 134, 54, 0.4);
    }}
    .status-badge.archived {{
      background: rgba(110, 118, 129, 0.15);
      color: #8b949e;
      border: 1px solid rgba(110, 118, 129, 0.3);
    }}
    .commit-meta {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: #58a6ff;
      background: rgba(56, 139, 253, 0.1);
      padding: 3px 8px;
      border-radius: 6px;
      border: 1px solid rgba(56, 139, 253, 0.2);
    }}
    .card-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 8px;
    }}
    .card-desc {{
      font-size: 0.92rem;
      color: var(--text-muted);
      margin-bottom: 20px;
      flex: 1;
    }}
    .card-details {{
      background: var(--code-bg);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 20px;
      font-size: 0.82rem;
      border: 1px solid rgba(255,255,255,0.05);
    }}
    .detail-row {{
      display: flex;
      justify-content: space-between;
      padding: 3px 0;
      color: var(--text-muted);
    }}
    .detail-row strong {{
      color: var(--text);
    }}
    .card-actions {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn-card {{
      flex: 1;
      justify-content: center;
      padding: 10px 16px;
      font-size: 0.88rem;
    }}
    .btn-sub {{
      background: #21262d;
      color: var(--text-white);
      border: 1px solid var(--card-border);
    }}
    .btn-sub:hover {{
      background: #30363d;
      border-color: #8b949e;
    }}
    .how-it-works {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 32px;
    }}
    .how-it-works h2 {{
      color: var(--text-white);
      font-size: 1.25rem;
      margin-bottom: 16px;
    }}
    .how-it-works pre {{
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #79c0ff;
      overflow-x: auto;
      margin: 14px 0;
    }}
    footer {{
      border-top: 1px solid var(--card-border);
      padding: 24px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: auto;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="brand">
        <span>Dr. Manoj Johar</span>
        <span class="brand-badge">KRATAM</span>
      </a>
      <a href="/latest/" class="btn btn-primary" style="padding: 8px 16px; font-size: 0.85rem;">
        Launch Latest &rarr;
      </a>
    </div>
  </header>

  <section class="hero">
    <h1>Deployment &amp; Commit Hub</h1>
    <p>Every commit uploaded to GitHub is preserved and accessible at its own dedicated subpath under this domain.</p>
    <div class="hero-actions">
      <a href="/latest/" class="btn btn-primary">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Open Current Live Version (/latest/)
      </a>
    </div>
  </section>

  <main class="main-container">
    <div class="section-title">
      Deployed Versions <span>{len(versions)} Available</span>
    </div>

    <div class="versions-grid">
{cards_joined}
    </div>

    <div class="how-it-works">
      <h2>How Multi-Commit Routing Works</h2>
      <p style="color: var(--text-muted); margin-bottom: 12px;">
        You can access any version using either its short 7-character hash, its full 40-character commit SHA, or the <code>/latest/</code> alias:
      </p>
      <pre>https://dr-johar.vercel.app/latest/
https://dr-johar.vercel.app/6ce732e/
https://dr-johar.vercel.app/6ce732e63260f60c0203ef7caa72248ad6fedf5c/
https://dr-johar.vercel.app/6609d4e/
https://dr-johar.vercel.app/6609d4ea1bcf45512772c0bd37a906c74a4ef3b6/</pre>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 14px;">
        To publish future commits automatically, run: <code>python publish_version.py &quot;Commit description&quot;</code>
      </p>
    </div>
  </main>

  <footer>
    &copy; 2026 Dr. Manoj Johar &amp; Kratam Hospital &bull; Multi-Version Vercel Deployment System
  </footer>

</body>
</html>
'''
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[+] Rebuilt root index.html portal successfully.')

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Multi-version deployment manager for Dr. Johar on Vercel.')
    parser.add_argument('message', nargs='?', default=None, help='Commit message / description for new version.')
    parser.add_argument('--refresh', action='store_true', help='Only rebuild index.html and vercel.json from versions.json.')
    parser.add_argument('--source', default=None, help='Source folder containing updated files to snapshot into new commit folder.')
    args = parser.parse_args()

    versions = load_versions()

    if args.refresh or not args.message:
        update_vercel_json()
        build_portal_html(versions)
        print('[OK] System refreshed successfully.')
        return

    title = args.message
    now_str = datetime.date.today().isoformat()
    
    try:
        commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=BASE_DIR).decode().strip()
    except Exception:
        import hashlib
        commit_sha = hashlib.sha1((title + str(datetime.datetime.now())).encode()).hexdigest()

    short_hash = commit_sha[:7]
    dest_dir = os.path.join(BASE_DIR, commit_sha)
    short_dest_dir = os.path.join(BASE_DIR, short_hash)
    latest_dest_dir = os.path.join(BASE_DIR, 'latest')

    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(short_dest_dir, exist_ok=True)
    os.makedirs(latest_dest_dir, exist_ok=True)

    src_dir = args.source
    if not src_dir:
        for v in versions:
            if v.get('is_latest'):
                src_dir = os.path.join(BASE_DIR, v['commit'])
                break

    if src_dir and os.path.exists(src_dir):
        print(f'[+] Copying snapshot from {src_dir} to commit folders...')
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        shutil.copytree(src_dir, short_dest_dir, dirs_exist_ok=True)
        shutil.copytree(src_dir, latest_dest_dir, dirs_exist_ok=True)

    for v in versions:
        v['is_latest'] = False

    new_entry = {
        'commit': commit_sha,
        'short_hash': short_hash,
        'title': title,
        'description': title,
        'branch': 'main',
        'date': now_str,
        'is_latest': True
    }
    versions.insert(0, new_entry)
    save_versions(versions)
    update_vercel_json()
    build_portal_html(versions)
    print(f'[OK] Published version {short_hash} ({commit_sha}).')

if __name__ == '__main__':
    main()
