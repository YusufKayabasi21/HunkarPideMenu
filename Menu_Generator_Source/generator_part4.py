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
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
    padding: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    scroll-behavior: smooth;
    box-shadow: inset 0 -1px 0 rgba(0,0,0,0.1);
  }
  .lang-select-wrapper {
    position: relative;
    width: 100%;
    max-width: 300px;
  }
  .lang-select {
    width: 100%;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.5);
    color: white;
    font-family: inherit;
    font-size: 15px;
    font-weight: 600;
    padding: 12px 40px 12px 20px;
    border-radius: 30px;
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    outline: none;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }
  .lang-select:focus {
    background: rgba(255, 255, 255, 0.25);
    border-color: #D4AF37;
    box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.2);
  }
  .lang-select-wrapper::after {
    content: '';
    position: absolute;
    right: 18px;
    top: 50%;
    transform: translateY(-50%);
    width: 12px;
    height: 12px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: center;
    pointer-events: none;
    transition: transform 0.3s ease;
  }
  html[dir="rtl"] .lang-select {
    padding: 12px 20px 12px 40px;
  }
  html[dir="rtl"] .lang-select-wrapper::after {
    right: auto;
    left: 18px;
  }
  .lang-select option {
    background-color: white;
    color: #2C3E3D;
    font-weight: 500;
  }
  .brand-header {
    text-align: center;
    padding: 36px 20px 24px;
    background: radial-gradient(circle at center, #fdfbf7 0%, #ffffff 100%);
    position: relative;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .brand-header::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 15%;
    width: 70%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.4;
    transition: all 0.3s ease;
  }
  .header.collapsed .brand-header {
    padding: 12px 20px 10px;
  }
  .header.collapsed .brand-header::after {
    opacity: 0;
  }
  
  @keyframes scaleIn {
    from { opacity: 0; transform: scale(0.92); }
    to { opacity: 1; transform: scale(1); }
  }
  @keyframes slideUpFade {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .logo-img {
    max-height: 85px;
    width: auto;
    margin-bottom: 16px;
    background: #ffffff;
    border-radius: 16px;
    padding: 8px;
    border: 1px solid rgba(212, 175, 55, 0.3);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08), 0 2px 8px rgba(212, 175, 55, 0.15);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    animation: scaleIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  .header.collapsed .logo-img {
    max-height: 40px;
    margin-bottom: 8px;
    padding: 4px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }
  
  .restaurant-name {
    font-size: 24px;
    font-weight: 700;
    color: var(--primary-dark);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    position: relative;
    padding-bottom: 18px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  .restaurant-name::after {
    content: '— GELENEKSEL LEZZET —';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--accent);
    font-weight: 600;
    opacity: 0.9;
  }
  .header.collapsed .restaurant-name {
    font-size: 18px;
    letter-spacing: 1px;
    padding-bottom: 0;
  }
  .header.collapsed .restaurant-name::after {
    display: none;
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
  
  .menu-item.recommended {
    border: 2px solid var(--accent);
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.15);
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
    
    <div style="margin-top: 16px; display: flex; justify-content: center; gap: 20px; align-items: center;">
      <a href="https://www.instagram.com/hunkarpidee/" target="_blank" style="color: var(--primary); text-decoration: none;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
      </a>
      <a href="https://hunkarpide.com/" target="_blank" style="display: flex; align-items: center;">
        <img src="data:image/jpeg;base64,{{LOGO_B64}}" style="height: 24px; width: auto; border-radius: 4px;" alt="Hünkar Pide">
      </a>
    </div>

  </div>
</div>
<div id="imageModal" class="modal">
  <span class="close-modal" id="closeModal">&times;</span>
  <img class="modal-content" id="modalImg">
</div>
<script>
  const MENU_DATA = {{MENU_DATA_JSON}};
  const IMAGES = {{IMAGES_JSON}};
  const LANGS = ['tr', 'en', 'es', 'ar', 'zh', 'it', 'fr', 'ru', 'fa', 'bs', 'sq', 'de', 'bg', 'el', 'ro', 'az'];
  const LANG_LABELS = {
    'tr': 'Türkçe',
    'en': 'English',
    'es': 'Español',
    'ar': 'العربية',
    'zh': '中文',
    'it': 'Italiano',
    'fr': 'Français',
    'ru': 'Русский',
    'fa': 'فارسی',
    'bs': 'Bosanski',
    'sq': 'Shqip',
    'de': 'Deutsch',
    'bg': 'Български',
    'el': 'Ελληνικά',
    'ro': 'Română',
    'az': 'Azərbaycanca'
  };
  
  function init() {
    const savedLang = localStorage.getItem('hunkar_lang') || 'tr';
    const activeLang = LANGS.includes(savedLang) ? savedLang : 'tr';
    renderLangSwitcher(activeLang);
    renderMenu(activeLang);
  }
  function switchLang(lang) {
    if (!MENU_DATA[lang]) return;
    localStorage.setItem('hunkar_lang', lang);
    
    const isRtl = (lang === 'ar' || lang === 'fa');
    document.documentElement.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
    document.documentElement.setAttribute('lang', lang);
    
    renderMenu(lang);
  }
  function renderLangSwitcher(activeLang) {
    const isRtl = (activeLang === 'ar' || activeLang === 'fa');
    document.documentElement.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
    document.documentElement.setAttribute('lang', activeLang);
    const switcher = document.getElementById('langSwitcher');
    switcher.innerHTML = '';
    
    const wrapper = document.createElement('div');
    wrapper.className = 'lang-select-wrapper';
    
    const select = document.createElement('select');
    select.className = 'lang-select';
    select.onchange = (e) => switchLang(e.target.value);
    
    LANGS.forEach(lang => {
      const opt = document.createElement('option');
      opt.value = lang;
      opt.textContent = LANG_LABELS[lang] || lang.toUpperCase();
      opt.selected = (lang === activeLang);
      select.appendChild(opt);
    });
    
    wrapper.appendChild(select);
    switcher.appendChild(wrapper);
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
        const isRecommended = (idx === 0);
        itemEl.className = 'menu-item' + (imgSrc ? ' has-image' : '') + (isRecommended ? ' recommended' : '');
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

  window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
      header.classList.add('collapsed');
    } else {
      header.classList.remove('collapsed');
    }
  });

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
