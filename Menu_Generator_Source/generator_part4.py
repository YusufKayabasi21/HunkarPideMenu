html_template = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Hünkar Pide Börek - Menü</title>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #2E8B37;
      --primary-dark: #1e5c24;
      --bg: #F8FAF9;
      --card-bg: #FFFFFF;
      --text: #2C3E3D;
      --text-light: #6B7C7B;
      --border: #E8F0EF;
      --accent: #D4AF37;
    }
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Outfit', sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }

    .container {
      max-width: 680px;
      margin: 0 auto;
      background-color: var(--bg);
      min-height: 100vh;
      position: relative;
    }

    /* Header & Lang Switcher */
    .header {
      background: var(--card-bg);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0, 130, 127, 0.08);
      border-bottom: 1px solid var(--border);
    }

    .lang-switcher {
      display: flex;
      overflow-x: auto;
      padding: 12px 16px;
      gap: 12px;
      background: var(--primary);
      scroll-behavior: smooth;
      -ms-overflow-style: none;  /* IE and Edge */
      scrollbar-width: none;  /* Firefox */
    }
    .lang-switcher::-webkit-scrollbar { display: none; }

    .lang-btn {
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      color: white;
      font-family: inherit;
      font-size: 14px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 20px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      min-height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .lang-btn.active {
      background: white;
      color: var(--primary-dark);
      border-color: white;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .brand-header {
      text-align: center;
      padding: 32px 20px;
      background: linear-gradient(135deg, var(--card-bg) 0%, var(--bg) 100%);
    }

    .logo-img {
      max-height: 80px;
      width: auto;
      margin-bottom: 16px;
      border-radius: 8px;
    }
    
    .restaurant-name {
      font-size: 24px;
      font-weight: 700;
      color: var(--primary-dark);
      letter-spacing: -0.5px;
    }

    /* Menu Layout */
    .menu-content {
      padding: 20px 16px 80px;
    }

    .section {
      margin-bottom: 40px;
      animation: fadeIn 0.4s ease forwards;
    }

    .section-title {
      font-size: 22px;
      font-weight: 600;
      color: var(--primary-dark);
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--border);
      display: flex;
      align-items: center;
    }
    
    .section-title::before {
      content: '';
      display: inline-block;
      width: 4px;
      height: 20px;
      background: var(--accent);
      margin-right: 12px;
      border-radius: 2px;
    }
    
    html[dir="rtl"] .section-title::before {
      margin-right: 0;
      margin-left: 12px;
    }

    .items-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .menu-item {
      background: var(--card-bg);
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.03);
      border: 1px solid var(--border);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    
    .menu-item:active {
      transform: scale(0.98);
      background: #F4F9F8;
    }

    .item-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
    }

    .item-name {
      font-size: 18px;
      font-weight: 600;
      color: var(--text);
      line-height: 1.3;
    }

    .item-price {
      font-size: 16px;
      font-weight: 700;
      color: var(--primary);
      background: rgba(0, 130, 127, 0.1);
      padding: 4px 10px;
      border-radius: 8px;
      white-space: nowrap;
    }

    .item-desc {
      font-size: 14px;
      color: var(--text-light);
      line-height: 1.6;
    }

    .about-text {
      font-size: 15px;
      color: var(--text-light);
      line-height: 1.8;
      background: var(--card-bg);
      padding: 24px;
      border-radius: 16px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.03);
      border: 1px solid var(--border);
      border-left: 4px solid var(--primary);
      white-space: pre-wrap;
    }
    
    html[dir="rtl"] .about-text {
      border-left: 1px solid var(--border);
      border-right: 4px solid var(--primary);
    }

    .footer {
      text-align: center;
      padding: 40px 20px;
      color: var(--text-light);
      font-size: 13px;
      border-top: 1px solid var(--border);
    }
    
    .footer-brand {
      font-weight: 600;
      color: var(--primary);
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    /* RTL Specific Fixes */
    html[dir="rtl"] .item-header { flex-direction: row; }

    /* Modal & Thumbnails */
    .modal {
      display: none;
      position: fixed;
      z-index: 1000;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.8);
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .modal.show {
      display: flex;
      opacity: 1;
    }
    .modal-content {
      max-width: 90%;
      max-height: 90%;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      transform: scale(0.95);
      transition: transform 0.3s ease;
    }
    .modal.show .modal-content {
      transform: scale(1);
    }
    .close-modal {
      position: absolute;
      top: 20px;
      right: 30px;
      color: white;
      font-size: 40px;
      font-weight: bold;
      cursor: pointer;
      z-index: 1001;
    }
    
    .item-with-img {
      display: flex;
      gap: 16px;
    }
    .has-image {
      cursor: pointer;
    }
    .has-image:hover {
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }
    .item-text-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .item-thumbnail {
      width: 80px;
      height: 80px;
      object-fit: cover;
      border-radius: 8px;
      border: 1px solid var(--border);
      flex-shrink: 0;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="lang-switcher" id="langSwitcher"></div>
      <div class="brand-header">
        <img src="data:image/jpeg;base64,{{LOGO_B64}}" alt="Logo" class="logo-img">
        <h1 class="restaurant-name" id="restName"></h1>
      </div>
    </div>
    
    <div class="menu-content" id="menuContent"></div>
    
    <div class="footer">
      <span class="footer-brand">Hünkar Pide Börek</span> &copy; 2026 Menü<br><br>
      Fiyatlarımıza KDV Dahildir.
    </div>
  </div>

  <div id="imageModal" class="modal">
    <span class="close-modal" id="closeModal">&times;</span>
    <img class="modal-content" id="modalImg">
  </div>

  <script>
    const MENU_DATA = {{MENU_DATA_JSON}};
    const IMAGES = {{IMAGES_JSON}};
    const LANGS = ['tr', 'en', 'es', 'ar', 'zh', 'it', 'fr', 'ru'];
    
    function init() {
      const savedLang = localStorage.getItem('hunkar_lang') || 'tr';
      const activeLang = LANGS.includes(savedLang) ? savedLang : 'tr';
      renderLangSwitcher(activeLang);
      renderMenu(activeLang);
    }

    function switchLang(lang) {
      if (!MENU_DATA[lang]) return;
      localStorage.setItem('hunkar_lang', lang);
      
      const isRtl = lang === 'ar';
      document.documentElement.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
      document.documentElement.setAttribute('lang', lang);
      
      document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
      });
      
      renderMenu(lang);
    }

    function renderLangSwitcher(activeLang) {
      const isRtl = activeLang === 'ar';
      document.documentElement.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
      document.documentElement.setAttribute('lang', activeLang);

      const switcher = document.getElementById('langSwitcher');
      switcher.innerHTML = '';
      
      LANGS.forEach(lang => {
        const btn = document.createElement('button');
        btn.className = `lang-btn ${lang === activeLang ? 'active' : ''}`;
        btn.textContent = lang.toUpperCase();
        btn.dataset.lang = lang;
        btn.onclick = () => switchLang(lang);
        switcher.appendChild(btn);
      });
    }

    function renderMenu(lang) {
      const data = MENU_DATA[lang];
      document.getElementById('restName').textContent = data.restaurantName;
      
      const content = document.getElementById('menuContent');
      content.innerHTML = '';
      
      data.sections.forEach((sec, idx) => {
        const secEl = document.createElement('div');
        secEl.className = 'section';
        secEl.style.animationDelay = `${idx * 0.05}s`;
        
        const titleEl = document.createElement('h2');
        titleEl.className = 'section-title';
        titleEl.textContent = sec.title;
        secEl.appendChild(titleEl);
        
        const gridEl = document.createElement('div');
        gridEl.className = 'items-grid';
        
        sec.items.forEach((item, itemIdx) => {

          const trItemName = MENU_DATA['tr'].sections[idx].items[itemIdx].name;
          const imgSrc = IMAGES[trItemName];

          const itemEl = document.createElement('div');
          itemEl.className = 'menu-item' + (imgSrc ? ' has-image' : '');
          if (imgSrc) {
            itemEl.onclick = () => openModal(imgSrc);
          }
          
          let innerHtml = '';
          if (imgSrc) {
            innerHtml += `<img src="${imgSrc}" class="item-thumbnail" alt="${item.name}">`;
          }

          let textHtml = `<div class="item-text-content">
                            <div class="item-header">
                              <div class="item-name">${item.name}</div>`;
          if (item.price) {
            textHtml += `<div class="item-price">${item.price}</div>`;
          }
          textHtml += `</div>`;
          
          if (item.description) {
            textHtml += `<div class="item-desc">${item.description}</div>`;
          }
          textHtml += `</div>`;
          
          if (imgSrc) {
            itemEl.innerHTML = `<div class="item-with-img">${innerHtml}${textHtml}</div>`;
          } else {
            itemEl.innerHTML = textHtml;
          }

          gridEl.appendChild(itemEl);
        });
        
        secEl.appendChild(gridEl);
        content.appendChild(secEl);
      });
    }

    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const closeModalBtn = document.getElementById('closeModal');

    function openModal(src) {
      modalImg.src = src;
      modal.classList.add('show');
    }

    function closeModal() {
      modal.classList.remove('show');
      setTimeout(() => { modalImg.src = ''; }, 300);
    }

    closeModalBtn.onclick = closeModal;
    modal.onclick = (e) => {
      if (e.target === modal) closeModal();
    };

    document.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

import json

# Output everything
with open("generator_core.py", "w", encoding="utf-8") as f:
    f.write('from generator_part1 import MENU_DATA as d1\n')
    f.write('from generator_part2 import MENU_DATA as d2\n')
    f.write('from generator_part3 import MENU_DATA as d3\n')
    f.write('import json\n')
    f.write('import base64\n')
    f.write('try:\n')
    f.write('    with open("logo_base64.txt", "r", encoding="utf-8") as fb:\n')
    f.write('        logo_b64 = fb.read().strip()\n')
    f.write('except:\n')
    f.write('    logo_b64 = ""\n')
    f.write('try:\n')
    f.write('    with open("images_base64.json", "r", encoding="utf-8") as fj:\n')
    f.write('        images_b64_json = fj.read().strip()\n')
    f.write('except:\n')
    f.write('    images_b64_json = "{}"\n')
    f.write('MENU_DATA = {**d1, **d2, **d3}\n')
    f.write('html = ' + repr(html_template) + '\n')
    f.write('html = html.replace("{{LOGO_B64}}", logo_b64)\n')
    f.write('html = html.replace("{{MENU_DATA_JSON}}", json.dumps(MENU_DATA, ensure_ascii=False))\n')
    f.write('html = html.replace("{{IMAGES_JSON}}", images_b64_json)\n')
    f.write('with open("index.html", "w", encoding="utf-8") as fout:\n')
    f.write('    fout.write(html)\n')
    f.write('print("index.html generated successfully")\n')
