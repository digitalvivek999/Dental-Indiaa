import re
import os
import zipfile
import io
import urllib.request
import json

INSTA_URL = "https://www.instagram.com/dr.sreedentist?xtok=cHQ1Z2V5eXI1NDBr"

# 1. Update config.js
cfg_path = r'C:\Users\vivek\Desktop\Dental-India\config.js'
with open(cfg_path, 'r', encoding='utf-8') as f:
    cfg = f.read()

cfg = cfg.replace('999/mo",\n', '')
if 'instagramUrl' not in cfg:
    cfg = cfg.replace(
        'email: "care@drlathasreedental.com",',
        f'email: "care@drlathasreedental.com",\n  instagramUrl: "{INSTA_URL}",\n  instagramHandle: "@dr.sreedentist",'
    )

with open(cfg_path, 'w', encoding='utf-8') as f:
    f.write(cfg)
print("SUCCESS: config.js updated!")

# 2. Update index.html
html_path = r'C:\Users\vivek\Desktop\Dental-India\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# A. Top Utility bar
old_utility = '<a href="tel:+919347594646" data-config-href="phoneLink" style="color: #FFFFFF; font-weight: 700; text-decoration: none;"><i class="fa-solid fa-phone"></i> <span data-config="phone">+91 93475 94646</span></a>'
new_utility = f'''<a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer" style="color: #FFFFFF; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;"><i class="fa-brands fa-instagram" style="color: #F472B6; font-size: 1.05rem;"></i> <span>@dr.sreedentist</span></a>
        {old_utility}'''

if old_utility in html and '@dr.sreedentist' not in html:
    html = html.replace(old_utility, new_utility, 1)

# B. Doctor Video Contact Card (Add Follow on Instagram button beside WhatsApp)
old_wa_btn = '''<a href="https://wa.me/919347594646?text=Hi%20Dr.%20Lathasree,%20I%20watched%20your%20video%20and%20want%20to%20consult%20for%20dental%20treatment." target="_blank" class="btn btn-whatsapp" style="background: #25D366; color: #FFFFFF; padding: 11px 20px; font-size: 0.92rem; font-weight: 700; border-radius: 12px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                <i class="fa-brands fa-whatsapp" style="font-size: 1.15rem;"></i>
                <span>Chat on WhatsApp</span>
              </a>'''

new_contact_buttons = f'''<div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                {old_wa_btn}
                <a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer" class="btn" style="background: linear-gradient(45deg, #F58529, #D92E7F, #833AB4); color: #FFFFFF; padding: 11px 18px; font-size: 0.92rem; font-weight: 700; border-radius: 12px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; box-shadow: 0 4px 14px rgba(217, 46, 127, 0.35); transition: transform 0.2s;">
                  <i class="fa-brands fa-instagram" style="font-size: 1.15rem;"></i>
                  <span>Follow on Instagram</span>
                </a>
              </div>'''

if old_wa_btn in html:
    html = html.replace(old_wa_btn, new_contact_buttons, 1)

# C. Doctor Bio Right Column (Add watch reels link under appointment buttons)
old_doc_btns = '''<a href="tel:+919347594646" class="btn btn-outline" style="border-radius: var(--radius-full); padding: 14px 28px;">
              <i class="fa-solid fa-phone"></i> Call: +91 93475 94646
            </a>
          </div>'''

new_doc_btns = f'''<a href="tel:+919347594646" class="btn btn-outline" style="border-radius: var(--radius-full); padding: 14px 28px;">
              <i class="fa-solid fa-phone"></i> Call: +91 93475 94646
            </a>
          </div>
          <div style="margin-top: 14px;">
            <a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 8px; color: #D92E7F; font-weight: 700; font-size: 0.95rem; text-decoration: none;">
              <i class="fa-brands fa-instagram" style="font-size: 1.25rem;"></i>
              <span>Watch Real Patient Cases & Reels on Instagram (@dr.sreedentist) &rarr;</span>
            </a>
          </div>'''

if old_doc_btns in html:
    html = html.replace(old_doc_btns, new_doc_btns, 1)

# D. Footer Social Icon
old_footer_insta = '<a href="#" style="width: 38px; height: 38px; border-radius: 50%; background: rgba(255, 255, 255, 0.12); display: flex; align-items: center; justify-content: center; color: #FFFFFF; text-decoration: none;"><i class="fa-brands fa-instagram"></i></a>'
new_footer_insta = f'<a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer" style="width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(45deg, #F58529, #D92E7F, #833AB4); display: flex; align-items: center; justify-content: center; color: #FFFFFF; text-decoration: none; font-size: 1.2rem; box-shadow: 0 4px 14px rgba(217, 46, 127, 0.35); transition: transform 0.2s;" title="Follow Dr. Sreedentist on Instagram"><i class="fa-brands fa-instagram"></i></a>'

if old_footer_insta in html:
    html = html.replace(old_footer_insta, new_footer_insta, 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated with Instagram links!")

# 3. Deploy to Netlify
TOKEN = "nfp_63K5AV5Dyyx42UAWZ84QagKzq8E1PerF2c15"
SITE_ID = "88b926df-914c-4200-a801-7b60bee7d3ec"
SITE_DIR = r"C:\Users\vivek\Desktop\Dental-India"

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(SITE_DIR):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file.endswith((".py", ".pyc")):
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, SITE_DIR)
            zip_file.write(abs_path, rel_path)

zip_data = zip_buffer.getvalue()
print(f"ZIP size: {len(zip_data)} bytes. Deploying to Netlify...")

deploy_url = f"https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys"
deploy_headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/zip",
    "User-Agent": "AntigravityDeployer/1.0"
}

req = urllib.request.Request(deploy_url, data=zip_data, headers=deploy_headers, method="POST")
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    print("\n=== DEPLOY SUCCESSFUL! ===")
    print(f"Deploy ID: {res.get('id')}")
    print(f"State: {res.get('state')}")
    print(f"URL: {res.get('ssl_url') or res.get('url')}")
