import urllib.request
import json
import io
import zipfile
import os
import time

TOKEN = "nfp_63K5AV5Dyyx42UAWZ84QagKzq8E1PerF2c15"
SITE_ID = "88b926df-914c-4200-a801-7b60bee7d3ec"
SITE_DIR = r"C:\Users\vivek\Desktop\Dental-India"

print("Creating ZIP of updated project...")
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

for attempt in range(1, 4):
    try:
        print(f"Deploy attempt {attempt}...")
        req = urllib.request.Request(deploy_url, data=zip_data, headers=deploy_headers, method="POST")
        with urllib.request.urlopen(req, timeout=120) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print("\n=== DEPLOY SUCCESSFUL! ===")
            print(f"Deploy ID: {res.get('id')}")
            print(f"State: {res.get('state')}")
            print(f"URL: {res.get('ssl_url') or res.get('url')}")
            break
    except Exception as e:
        print(f"Attempt {attempt} failed: {e}")
        time.sleep(3)
