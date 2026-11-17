# Script to fix mobile responsiveness, GMB map overflow, booking form inputs, Netlify badge, and clinic tour captions
import re

file_path = r'C:\Users\vivek\Desktop\Dental-India\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Gallery Items: Remove subtext, keep only headings
# Advanced Operatory Suite
html = re.sub(
    r'(<div style="font-size: 1\.25rem; font-weight: 800; color: #FFFFFF;">Advanced Operatory Suite</div>)\s*<div style="font-size: 0\.95rem; color: #E2E8F0; font-weight: 500; margin-top: 4px;">[^<]+</div>',
    r'\1',
    html
)

# Reception & Waiting Lounge
html = re.sub(
    r'(<div style="font-size: 1\.25rem; font-weight: 800; color: #FFFFFF;">Reception & Waiting Lounge</div>)\s*<div style="font-size: 0\.95rem; color: #E2E8F0; font-weight: 500; margin-top: 4px;">[^<]+</div>',
    r'\1',
    html
)

# Class-B Autoclave Sterilization Lab
html = re.sub(
    r'(<div style="font-size: 1\.25rem; font-weight: 800; color: #FFFFFF;">Class-B Autoclave Sterilization Lab</div>)\s*<div style="font-size: 0\.95rem; color: #E2E8F0; font-weight: 500; margin-top: 4px;">[^<]+</div>',
    r'\1',
    html
)

# Digital 3D Diagnostic & X-Ray Center
html = re.sub(
    r'(<div style="font-size: 1\.25rem; font-weight: 800; color: #FFFFFF;">Digital 3D Diagnostic & X-Ray Center</div>)\s*<div style="font-size: 0\.95rem; color: #E2E8F0; font-weight: 500; margin-top: 4px;">[^<]+</div>',
    r'\1',
    html
)

# 2. Update Date and Slot in Booking Form
html = html.replace(
    '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">\n                <input type="date" id="ptDate"',
    '<div class="date-slot-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">\n                <input type="date" id="ptDate"'
)
# In case line breaks differ:
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">\s*<input type="date" id="ptDate"',
    r'<div class="date-slot-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">\n                <input type="date" id="ptDate"',
    html
)

# 3. Add robust mobile styles for GMB, Booking Form, Containers, Netlify badge obliteration, and Gallery
mobile_css_additions = """
    /* Global Container and Viewport Overflow Protection */
    html, body {
      max-width: 100vw !important;
      overflow-x: hidden !important;
      position: relative !important;
    }
    * {
      box-sizing: border-box !important;
    }
    .container {
      width: 100% !important;
      max-width: 1200px !important;
      padding-left: 16px !important;
      padding-right: 16px !important;
      box-sizing: border-box !important;
    }

    /* Form Controls Universal Robustness */
    .form-group {
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .form-control {
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      display: block !important;
    }

    /* Netlify Badge Complete Obliteration */
    [class*="netlify"],
    [id*="netlify"],
    [data-netlify],
    netlify-badge,
    netlify-drawer,
    a[href*="netlify.com"],
    div:has(> a[href*="netlify.com"]),
    div:has(> [class*="netlify"]),
    body > div[style*="fixed"][style*="bottom"],
    body > a[style*="fixed"][style*="bottom"] {
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
      width: 0 !important;
      height: 0 !important;
      position: absolute !important;
      left: -9999px !important;
      z-index: -999999 !important;
    }

    /* Mobile Sticky Bar: Highest Priority */
    .mobile-sticky-bar {
      z-index: 2147483647 !important;
    }

    @media (max-width: 768px) {
      /* GMB Section: 1-Column Mobile Layout (prevents side overflow & circle button distortion) */
      .gmb-grid {
        grid-template-columns: 1fr !important;
        gap: 20px !important;
        width: 100% !important;
      }
      .gmb-card {
        padding: 24px 18px !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
      .gmb-card .btn {
        width: 100% !important;
        border-radius: 12px !important;
        padding: 13px 16px !important;
        justify-content: center !important;
        text-align: center !important;
        font-size: 0.9rem !important;
        box-sizing: border-box !important;
      }
      .gmb-map-wrap {
        width: 100% !important;
        height: 280px !important;
        border-radius: var(--radius-md) !important;
        box-sizing: border-box !important;
      }

      /* Booking Form Mobile Overhaul */
      .booking-card {
        padding: 24px 18px !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        border-radius: 16px !important;
      }
      .form-grid {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
        width: 100% !important;
        box-sizing: border-box !important;
        margin-bottom: 20px !important;
      }
      .form-control {
        height: 48px !important;
        font-size: 16px !important;
        padding: 12px 14px !important;
      }
      .date-slot-row {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }
      .btn-submit-booking {
        width: 100% !important;
        height: 50px !important;
        font-size: 1.02rem !important;
        justify-content: center !important;
      }

      /* Clinic Tour Gallery: Clean 1-Column on Mobile */
      .gallery-grid {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }
      .gallery-item {
        height: 250px !important;
      }
    }
"""

# Insert before </head>
html = html.replace('</head>', f'<style>{mobile_css_additions}</style>\n</head>')

# Add JS purge for Netlify badge before </body>
js_purge = """
<script>
  (function() {
    function purgeNetlifyBadge() {
      var elements = document.querySelectorAll('[class*="netlify"], [id*="netlify"], [data-netlify], netlify-badge, netlify-drawer, a[href*="netlify.com"]');
      elements.forEach(function(el) {
        if (el) el.remove();
      });
      var allDivs = document.querySelectorAll('body > div, body > a');
      allDivs.forEach(function(d) {
        if (d && d.textContent && d.textContent.indexOf('Powered by Netlify') !== -1) {
          d.remove();
        }
      });
    }
    purgeNetlifyBadge();
    setInterval(purgeNetlifyBadge, 400);
  })();
</script>
"""
html = html.replace('</body>', f'{js_purge}\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated successfully!")
