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
  
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #0F1210;
      --card-bg: #1A1F1C;
      --text: #E8F0EF;
      --text-light: #A0B0AF;
      --border: #26302B;
      --primary: #3DAE48;
    }
  }

  [data-theme="dark"] {
    --bg: #0F1210;
    --card-bg: #1A1F1C;
    --text: #E8F0EF;
    --text-light: #A0B0AF;
    --border: #26302B;
    --primary: #3DAE48;
  }
  
  [data-theme="light"] {
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
    padding: 12px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    scroll-behavior: smooth;
    box-shadow: inset 0 -1px 0 rgba(0,0,0,0.1);
    gap: 12px;
  }
  .theme-toggle {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: white;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    flex-shrink: 0;
  }
  .theme-toggle:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-2px);
  }
  .theme-toggle:active {
    transform: scale(0.95);
  }
  .sun-icon { display: none; }
  
  /* Show correct icon based on active state */
  [data-theme="dark"] .moon-icon { display: none; }
  [data-theme="dark"] .sun-icon { display: block; }
  
  /* Fallback for system preference when no data-theme is set */
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) .moon-icon { display: none; }
    :root:not([data-theme="light"]) .sun-icon { display: block; }
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
    background: radial-gradient(circle at center, var(--card-bg) 0%, var(--bg) 100%);
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
    border: 1px solid var(--accent);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08), 0 0 15px rgba(212, 175, 55, 0.4);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    animation: scaleIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  [data-theme="dark"] .logo-img {
    box-shadow: 0 8px 24px rgba(0,0,0,0.4), 0 0 20px rgba(212, 175, 55, 0.6);
    background: #ffffff; /* Keep logo background white for contrast if it has no transparency */
  }
  .header.collapsed .logo-img {
    max-height: 40px;
    margin-bottom: 8px;
    padding: 4px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05), 0 0 8px rgba(212, 175, 55, 0.3);
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
    position: relative;
    overflow: hidden;
    animation: fadeUpItem 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
  }
  
  .menu-item.recommended {
    border: 2px solid var(--accent);
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.15);
  }
  
  .menu-item:active {
    transform: scale(0.98);
  }
  .ripple-effect {
    position: absolute;
    border-radius: 50%;
    background: rgba(212, 175, 55, 0.2);
    transform: scale(0);
    animation: rippleAnim 0.55s linear;
    pointer-events: none;
  }
  @keyframes rippleAnim {
    to { transform: scale(4); opacity: 0; }
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
  @keyframes fadeUpItem {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  /* Section Divider */
  .section-divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: -12px 0 28px;
    color: var(--accent);
    font-size: 13px;
    letter-spacing: 5px;
    opacity: 0.75;
    user-select: none;
  }
  .section-divider::before,
  .section-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.4;
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
  .modal-card {
    background: var(--card-bg);
    max-width: 90%;
    width: 400px;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.7);
    transform: translateY(40px) scale(0.96);
    opacity: 0;
    transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
    position: relative;
    border: 1px solid var(--border);
    display: flex;
    flex-direction: column;
  }
  .modal-card::before {
    content: '';
    display: block;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--accent), #f5d76e, var(--accent));
    flex-shrink: 0;
  }
  .modal.show .modal-card {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  .modal-image {
    width: 100%;
    max-height: 40vh;
    object-fit: cover;
    display: block;
    background: #000;
  }
  .modal-info {
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .modal-title {
    font-size: 22px;
    font-weight: 700;
    color: var(--text);
    margin: 0;
  }
  .modal-desc {
    font-size: 15px;
    color: var(--text-light);
    line-height: 1.6;
    margin: 0;
  }
  .modal-price {
    align-self: flex-start;
    font-size: 20px;
    font-weight: 700;
    color: var(--accent);
    background: rgba(212, 175, 55, 0.1);
    padding: 8px 16px;
    border-radius: 12px;
    margin-top: 4px;
    border: 1px solid rgba(212, 175, 55, 0.2);
  }
  .close-modal {
    position: absolute;
    top: 16px;
    right: 16px;
    width: 32px;
    height: 32px;
    background: rgba(0, 0, 0, 0.5);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    z-index: 10;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    transition: background 0.2s ease;
  }
  .close-modal:hover {
    background: rgba(0, 0, 0, 0.8);
  }
  html[dir="rtl"] .close-modal {
    right: auto;
    left: 16px;
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
  /* Shimmer skeleton */
  @keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
  }
  .img-wrapper {
    width: 80px;
    height: 80px;
    border-radius: 8px;
    flex-shrink: 0;
    overflow: hidden;
    background: linear-gradient(90deg, var(--border) 25%, rgba(212,175,55,0.07) 50%, var(--border) 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s ease-in-out infinite;
  }
  .img-wrapper.loaded {
    animation: none;
    background: none;
  }
  .item-thumbnail {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    opacity: 0;
    transition: opacity 0.35s ease;
  }
  .img-wrapper.loaded .item-thumbnail {
    opacity: 1;
  }
  /* Scroll-to-top */
  .scroll-top-btn {
    position: fixed;
    bottom: 28px;
    right: 20px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: var(--accent);
    color: #1a1200;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(212, 175, 55, 0.45);
    opacity: 0;
    transform: translateY(16px);
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    pointer-events: none;
    z-index: 500;
  }
  .scroll-top-btn.visible {
    opacity: 1;
    transform: translateY(0);
    pointer-events: all;
  }
  .scroll-top-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 28px rgba(212, 175, 55, 0.65);
  }
  .scroll-top-btn:active { transform: scale(0.94); }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="lang-switcher">
      <div id="langSwitcher" style="flex: 1;"></div>
      <div class="theme-toggle" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle Theme">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="moon-icon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="sun-icon"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
      </div>
    </div>
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
<button class="scroll-top-btn" id="scrollTopBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Back to top">
  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
</button>
<div id="imageModal" class="modal">
  <div class="modal-card">
    <span class="close-modal" id="closeModal">&times;</span>
    <img class="modal-image" id="modalImg">
    <div class="modal-info">
      <h3 id="modalTitle" class="modal-title"></h3>
      <div id="modalPrice" class="modal-price"></div>
      <p id="modalDesc" class="modal-desc"></p>
    </div>
  </div>
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
    
    // Theme logic
    const savedTheme = localStorage.getItem('hunkar_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
    
    renderLangSwitcher(activeLang);
    renderMenu(activeLang);
  }
  function toggleTheme() {
    let currentTheme = document.documentElement.getAttribute('data-theme');
    
    // If no attribute set, determine from system
    if (!currentTheme) {
      currentTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('hunkar_theme', newTheme);
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
      
      let itemCounter = 0;
      sec.items.forEach((item, itemIdx) => {
        const trItemName = MENU_DATA['tr'].sections[idx].items[itemIdx].name;
        const imgSrc = IMAGES[trItemName];
        const itemEl = document.createElement('div');
        const isRecommended = (idx === 0);
        itemEl.className = 'menu-item' + (imgSrc ? ' has-image' : '') + (isRecommended ? ' recommended' : '');
        itemEl.style.animationDelay = `${(idx * 60 + itemCounter * 50)}ms`;
        itemCounter++;
        if (imgSrc) {
          itemEl.onclick = () => openModal(imgSrc, item.name, item.description, item.price);
          itemEl.addEventListener('mousedown', createRipple);
        }
        
        let innerHtml = '';
        if (imgSrc) {
          innerHtml += `<div class="img-wrapper"><img src="${imgSrc}" class="item-thumbnail" alt="${item.name}" onload="this.parentElement.classList.add('loaded')"></div>`;
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
      
      // Gold divider between sections
      if (idx < data.sections.length - 1) {
        const divider = document.createElement('div');
        divider.className = 'section-divider';
        divider.innerHTML = '<span>❖</span>';
        content.appendChild(divider);
      }
    });
  }
  const modal = document.getElementById('imageModal');
  const modalImg = document.getElementById('modalImg');
  const modalTitle = document.getElementById('modalTitle');
  const modalDesc = document.getElementById('modalDesc');
  const modalPrice = document.getElementById('modalPrice');
  const closeModalBtn = document.getElementById('closeModal');
  
  function openModal(src, title, desc, price) {
    modalImg.src = src;
    modalTitle.textContent = title;
    
    if (desc) {
      modalDesc.textContent = desc;
      modalDesc.style.display = 'block';
    } else {
      modalDesc.style.display = 'none';
    }
    
    if (price) {
      modalPrice.textContent = price;
      modalPrice.style.display = 'inline-block';
    } else {
      modalPrice.style.display = 'none';
    }
    
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

  function createRipple(e) {
    const item = e.currentTarget;
    const circle = document.createElement('span');
    const diameter = Math.max(item.clientWidth, item.clientHeight);
    const rect = item.getBoundingClientRect();
    circle.className = 'ripple-effect';
    circle.style.cssText = `width:${diameter}px;height:${diameter}px;left:${e.clientX - rect.left - diameter/2}px;top:${e.clientY - rect.top - diameter/2}px;`;
    const old = item.querySelector('.ripple-effect');
    if (old) old.remove();
    item.appendChild(circle);
    setTimeout(() => circle.remove(), 600);
  }

  // Scroll: header collapse with hysteresis + scroll-to-top btn
  let headerCollapsed = false;
  window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    const scrollBtn = document.getElementById('scrollTopBtn');
    const y = window.scrollY;
    // Hysteresis: collapse at 90px, uncollapse at 20px
    if (!headerCollapsed && y > 90) {
      headerCollapsed = true;
      header.classList.add('collapsed');
    } else if (headerCollapsed && y < 20) {
      headerCollapsed = false;
      header.classList.remove('collapsed');
    }
    if (scrollBtn) scrollBtn.classList.toggle('visible', y > 300);
  }, { passive: true });

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
