import json
import re

price_map = {
    1: "450 ₺",
    2: "300 ₺", 3: "300 ₺", 4: "300 ₺", 5: "300 ₺",
    6: "450 ₺", 7: "425 ₺", 8: "450 ₺", 9: "425 ₺",
    10: "260 ₺", 11: "270 ₺", 12: "260 ₺", 13: "300 ₺",
    14: "60 ₺", 15: "140 ₺", 16: "140 ₺", 17: "120 ₺",
    18: "60 ₺", 19: "50 ₺", 20: "60 ₺", 21: "60 ₺", 22: "40 ₺",
    23: "30 ₺", 24: "15 ₺", 25: "25 ₺", 26: "70 ₺", 27: "70 ₺"
}

tr_sections = [
  {"title": "Şefin Önerisi", "items": [{"name": "Palamut Pide", "description": "İnce Çıtır Hamur, Hakiki Rize Kavurma, Tereyağı, Palamut Şekli, Şefin Önerisi"}]},
  {"title": "Karadeniz Pidesi", "items": [
    {"name": "Kıymalı Pide", "description": "Hünkar usulü özel kıymalı harç (Ekstra Yumurta 10 TL)"},
    {"name": "Kıymalı Sebzeli", "description": "Hünkar usulü özel kıymalı harç, taze domates, çıtır yeşil biber (Ekstra Yumurta 10 TL)"},
    {"name": "Kıymalı Kaşarlı", "description": "Hünkar usulü özel kıymalı harç, erimiş artisan Kaşar peyniri (Ekstra Yumurta 10 TL)"},
    {"name": "Kıymalı Karışık", "description": "Hünkar usulü özel kıymalı harç, erimiş Kaşar peyniri, taze domates, çıtır yeşil biber (Ekstra Yumurta 10 TL)"},
    {"name": "Kavurmalı Pide", "description": "Özel Rize kavurması (Ekstra Yumurta 10 TL)"},
    {"name": "Kavurmalı Kaşarlı", "description": "Özel Rize kavurması, erimiş artisan Kaşar peyniri (Ekstra Yumurta 10 TL)"},
    {"name": "Kavurmalı Sebzeli", "description": "Özel Rize kavurması, taze domates, çıtır yeşil biber (Ekstra Yumurta 10 TL)"},
    {"name": "Kavurmalı Karışık", "description": "Özel Rize kavurması, erimiş Kaşar peyniri, taze domates, çıtır yeşil biber (Ekstra Yumurta 10 TL)"},
    {"name": "Kaşarlı Pide", "description": "Erimiş artisan Kaşar peyniri (Ekstra Yumurta 10 TL)"},
    {"name": "Kaşarlı Yumurtalı", "description": "Erimiş artisan Kaşar peyniri, köy yumurtası (Ekstra Yumurta 10 TL)"},
    {"name": "Kaşarlı Sebzeli", "description": "Erimiş artisan Kaşar peyniri, taze domates, çıtır yeşil biber (Ekstra Yumurta 10 TL)"},
    {"name": "Sucuklu Kaşarlı", "description": "Dana kasap sucuk, erimiş artisan Kaşar peyniri (Ekstra Yumurta 10 TL)"}
  ]},
  {"title": "Pide & Börek", "items": [
    {"name": "Kır Pidesi", "description": "Kıymalı, Peynirli, Patatesli seçenekleriyle yumuşak artisan hamur"},
    {"name": "Kol Böreği", "description": "Kıymalı, Peynirli, Patatesli, Ispanaklı, Tahinli el açması çıtır yufka"},
    {"name": "Su Böreği", "description": "El açması haşlama yufka, hakiki tereyağı, artisan beyaz peynir"},
    {"name": "Sade Börek", "description": "El açması çıtır yufka, hakiki tereyağı. Geleneksel olarak pudra şekeri ile servis edilir."}
  ]},
  {"title": "İçecekler", "items": [
    {"name": "Kola", "description": ""},
    {"name": "Gazoz", "description": "Klasik/Portakallı"},
    {"name": "Meyve Suyu", "description": "Şeftali/Vişne/Karışık"},
    {"name": "Iced Tea", "description": "Limon/Şeftali"},
    {"name": "Ayran", "description": ""},
    {"name": "Soda", "description": ""},
    {"name": "Su", "description": ""},
    {"name": "Çay", "description": ""},
    {"name": "Limonata", "description": ""},
    {"name": "Türk Kahvesi", "description": ""}
  ]}
]

en_sections = [
  {"title": "Chef's Recommendation", "items": [{"name": "Acorn-Shaped Black Sea Pide", "description": "Thin Crispy Dough, Authentic Rize Braised Beef, Butter, Acorn Shape, Chef's Recommendation"}]},
  {"title": "Black Sea Pide", "items": [
    {"name": "Minced Beef Pide", "description": "Signature 'Hünkar-style' minced beef mix (Extra Egg 10 TL)"},
    {"name": "Minced Beef & Vegetables", "description": "Signature 'Hünkar-style' minced beef mix, fresh tomatoes, crisp green peppers (Extra Egg 10 TL)"},
    {"name": "Minced Beef & Cheese", "description": "Signature 'Hünkar-style' minced beef mix, melted artisan Kaşar cheese (Extra Egg 10 TL)"},
    {"name": "The Supreme Mixed", "description": "Signature 'Hünkar-style' minced beef mix, melted Kaşar cheese, fresh tomatoes, crisp green peppers (Extra Egg 10 TL)"},
    {"name": "Roasted Beef Pide", "description": "Premium slow-roasted Rize beef (Kavurma) (Extra Egg 10 TL)"},
    {"name": "Roasted Beef & Cheese", "description": "Premium slow-roasted Rize beef (Kavurma), melted artisan Kaşar cheese (Extra Egg 10 TL)"},
    {"name": "Roasted Beef & Vegetables", "description": "Premium slow-roasted Rize beef (Kavurma), fresh tomatoes, crisp green peppers (Extra Egg 10 TL)"},
    {"name": "Mixed Beef & Veggie Melt", "description": "Premium slow-roasted Rize beef (Kavurma), melted Kaşar cheese, fresh tomatoes, crisp green peppers (Extra Egg 10 TL)"},
    {"name": "Melted Cheese Pide", "description": "Premium melting artisan Kaşar cheese (Extra Egg 10 TL)"},
    {"name": "Cheese & Farm-Fresh Egg", "description": "Melted artisan Kaşar cheese, farm-fresh egg (Extra Egg 10 TL)"},
    {"name": "Melted Cheese & Vegetables", "description": "Melted artisan Kaşar cheese, fresh tomatoes, crisp green peppers (Extra Egg 10 TL)"},
    {"name": "Spiced Beef Sausage & Melted Cheese", "description": "Spiced Turkish beef sausage (Sucuk), melted artisan Kaşar cheese (Extra Egg 10 TL)"}
  ]},
  {"title": "Pide & Börek", "items": [
    {"name": "Traditional Kır Pide", "description": "Soft artisan dough with your choice of seasoned minced beef, cheese, or seasoned potatoes"},
    {"name": "Rolled Pastry", "description": "Hand-rolled crispy dough layers with minced beef, artisan cheese, potatoes, spinach, or tahini"},
    {"name": "Ottoman-Style Layered Pastry", "description": "Hand-rolled boiled dough layers, premium melted butter, white artisan cheese"},
    {"name": "Flaky Butter Pastry", "description": "Hand-rolled crispy dough layers, premium melted butter. Traditionally enjoyed with a generous dusting of powdered sugar."}
  ]},
  {"title": "Beverages", "items": [
    {"name": "Classic Cola", "description": ""},
    {"name": "Turkish Soda", "description": "Classic/Orange"},
    {"name": "Fruit Juice", "description": "Peach/Sour Cherry/Mixed Fruit"},
    {"name": "Iced Tea", "description": "Lemon / Peach"},
    {"name": "Ayran", "description": ""},
    {"name": "Mineral Water", "description": ""},
    {"name": "Water", "description": ""},
    {"name": "Authentic Black Sea Tea", "description": ""},
    {"name": "Handcrafted Lemonade", "description": ""},
    {"name": "Turkish Coffee", "description": ""}
  ]}
]

es_sections = [
  {"title": "Recomendación del Chef", "items": [{"name": "Pide del Mar Negro en Forma de Bellota", "description": "Masa Fina y Crujiente, Auténtica Ternera Estofada de Rize, Mantequilla, Forma de Bellota, Recomendación del Chef"}]},
  {"title": "Pide del Mar Negro", "items": [
    {"name": "Pide de Carne Picada", "description": "Mezcla de carne picada estilo Hünkar (Huevo extra 10 TL)"},
    {"name": "Carne Picada con Verduras", "description": "Mezcla de carne picada estilo Hünkar, tomates frescos, pimientos verdes crujientes (Huevo extra 10 TL)"},
    {"name": "Carne Picada y Queso", "description": "Mezcla de carne picada estilo Hünkar, queso artesanal Kaşar fundido (Huevo extra 10 TL)"},
    {"name": "Pide Mixto Supremo", "description": "Mezcla de carne picada estilo Hünkar, queso Kaşar fundido, tomates frescos, pimientos verdes crujientes (Huevo extra 10 TL)"},
    {"name": "Pide de Ternera Asada", "description": "Ternera de Rize asada a fuego lento premium (Kavurma) (Huevo extra 10 TL)"},
    {"name": "Ternera Asada y Queso", "description": "Ternera de Rize asada a fuego lento premium, queso artesanal Kaşar fundido (Huevo extra 10 TL)"},
    {"name": "Ternera Asada y Verduras", "description": "Ternera de Rize asada a fuego lento premium, tomates frescos, pimientos verdes crujientes (Huevo extra 10 TL)"},
    {"name": "Mixto de Ternera Asada y Verduras", "description": "Ternera de Rize asada a fuego lento premium, queso Kaşar fundido, tomates frescos, pimientos verdes crujientes (Huevo extra 10 TL)"},
    {"name": "Pide de Queso Fundido", "description": "Queso artesanal Kaşar premium fundido (Huevo extra 10 TL)"},
    {"name": "Queso y Huevo de Granja", "description": "Queso artesanal Kaşar fundido, huevo fresco de granja (Huevo extra 10 TL)"},
    {"name": "Queso Fundido y Verduras", "description": "Queso artesanal Kaşar fundido, tomates frescos, pimientos verdes crujientes (Huevo extra 10 TL)"},
    {"name": "Salchicha Especiada y Queso Fundido", "description": "Salchicha de ternera turca especiada (Sucuk), queso artesanal Kaşar fundido (Huevo extra 10 TL)"}
  ]},
  {"title": "Pide y Börek", "items": [
    {"name": "Kır Pide Tradicional", "description": "Masa artesanal suave con elección de carne picada sazonada, queso o patatas sazonadas"},
    {"name": "Pastel Enrollado (Kol Böreği)", "description": "Capas finas de masa crujiente enrollada a mano con carne picada, queso artesanal, patatas, espinacas o tahini"},
    {"name": "Hojaldre Estilo Otomano (Su Böreği)", "description": "Capas de masa hervida estirada a mano, mantequilla fundida premium, queso blanco artesanal"},
    {"name": "Hojaldre Abierto de Mantequilla", "description": "Capas finas de masa crujiente enrollada a mano, mantequilla fundida premium. Se disfruta tradicionalmente con abundante azúcar en polvo."}
  ]},
  {"title": "Bebidas", "items": [
    {"name": "Cola Clásica", "description": ""},
    {"name": "Refresco Turco (Gazoz)", "description": "Clásico/Naranja"},
    {"name": "Zumo de Frutas", "description": "Melocotón/Guinda/Frutas Mixtas"},
    {"name": "Té Helado", "description": "Limón/Melocotón"},
    {"name": "Ayran (Refresco de yogur)", "description": ""},
    {"name": "Agua Mineral", "description": ""},
    {"name": "Agua", "description": ""},
    {"name": "Té Auténtico del Mar Negro", "description": ""},
    {"name": "Limonada Artesanal", "description": ""},
    {"name": "Café Turco", "description": ""}
  ]}
]

ar_sections = [
  {"title": "توصية الشيف", "items": [{"name": "بيدا البحر الأسود على شكل بلوط", "description": "عجينة رقيقة ومقرمشة، لحم بقر ريزي مطهو ببطء، زبدة، شكل بلوط، توصية الشيف"}]},
  {"title": "بيدا البحر الأسود", "items": [
    {"name": "بيدا باللحم المفروم", "description": "خلطة لحم مفروم مميزة على طريقة هنكار (إضافة بيض 10 ليرة تركية)"},
    {"name": "لحم مفروم وخضروات", "description": "خلطة لحم مفروم مميزة على طريقة هنكار، طماطم طازجة، فلفل أخضر مقرمش (إضافة بيض 10 ليرة تركية)"},
    {"name": "لحم مفروم وجبن", "description": "خلطة لحم مفروم مميزة على طريقة هنكار، جبن كاشار حرفي ذائب (إضافة بيض 10 ليرة تركية)"},
    {"name": "تشكيلة لحم مفروم فائقة", "description": "خلطة لحم مفروم مميزة على طريقة هنكار، جبن كاشار ذائب، طماطم طازجة، فلفل أخضر مقرمش (إضافة بيض 10 ليرة تركية)"},
    {"name": "بيدا اللحم البقري المشوي", "description": "لحم بقر ريزي مشوي ببطء فاخر (قاورما) (إضافة بيض 10 ليرة تركية)"},
    {"name": "لحم بقري مشوي وجبن", "description": "لحم بقر ريزي مشوي ببطء فاخر، جبن كاشار حرفي ذائب (إضافة بيض 10 ليرة تركية)"},
    {"name": "لحم بقري مشوي وخضروات", "description": "لحم بقر ريزي مشوي ببطء فاخر، طماطم طازجة، فلفل أخضر مقرمش (إضافة بيض 10 ليرة تركية)"},
    {"name": "تشكيلة لحم بقري مشوي وخضار ذائبة", "description": "لحم بقر ريزي مشوي ببطء فاخر، جبن كاشار ذائب، طماطم طازجة، فلفل أخضر مقرمش (إضافة بيض 10 ليرة تركية)"},
    {"name": "بيدا الجبن الذائب", "description": "جبن كاشار حرفي فاخر ذائب (إضافة بيض 10 ليرة تركية)"},
    {"name": "جبن وبيض طازج من المزرعة", "description": "جبن كاشار حرفي ذائب، بيض طازج من المزرعة (إضافة بيض 10 ليرة تركية)"},
    {"name": "جبن ذائب وخضروات", "description": "جبن كاشار حرفي ذائب، طماطم طازجة، فلفل أخضر مقرمش (إضافة بيض 10 ليرة تركية)"},
    {"name": "سجق بقري متبل وجبن ذائب", "description": "سجق لحم بقري تركي متبل (سجق)، جبن كاشار حرفي ذائب (إضافة بيض 10 ليرة تركية)"}
  ]},
  {"title": "بيدا وبوريك", "items": [
    {"name": "قير بيدا التقليدي", "description": "عجينة حرفية ناعمة مع اختيارك من اللحم المفروم المتبل، أو الجبن، أو البطاطس المتبلة"},
    {"name": "معجنات ملفوفة", "description": "طبقات من العجينة المقرمشة الملفوفة يدوياً مع لحم مفروم، جبن حرفي، بطاطس، سبانخ، أو طحينة"},
    {"name": "معجنات طبقات على الطريقة العثمانية", "description": "طبقات من العجينة المسلوقة الممدودة يدوياً، زبدة ذائبة فاخرة، جبن أبيض حرفي"},
    {"name": "معجنات الزبدة الهشة", "description": "طبقات من العجينة المقرمشة الملفوفة يدوياً، زبدة ذائبة فاخرة. تُستمتع بها تقليدياً مع رشّة سخية من السكر البودرة."}
  ]},
  {"title": "المشروبات", "items": [
    {"name": "كولا كلاسيكية", "description": ""},
    {"name": "صودا تركية", "description": "كلاسيك/برتقال"},
    {"name": "عصير فواكه", "description": "خوخ/كرز حامض/فواكه مشكلة"},
    {"name": "شاي مثلج", "description": "ليمون/خوخ"},
    {"name": "عيران", "description": ""},
    {"name": "مياه معدنية", "description": ""},
    {"name": "ماء", "description": ""},
    {"name": "شاي البحر الأسود الأصيل", "description": ""},
    {"name": "ليموناضة معدة يدوياً", "description": ""},
    {"name": "قهوة تركية", "description": ""}
  ]}
]

zh_sections = [
  {"title": "主厨推荐", "items": [{"name": "橡子形黑海皮塔饼", "description": "薄脆面团，正宗里泽慢烤牛肉，黄油，独特橡子形，主厨推荐"}]},
  {"title": "黑海皮塔饼", "items": [
    {"name": "肉末皮塔饼", "description": "招牌 'Hünkar 风格' 肉末混合物 (加鸡蛋 10 TL)"},
    {"name": "肉末与蔬菜", "description": "招牌 'Hünkar 风格' 肉末混合物，新鲜番茄，爽脆青椒 (加鸡蛋 10 TL)"},
    {"name": "肉末与手工奶酪", "description": "招牌 'Hünkar 风格' 肉末混合物，融化的 Kaşar 奶酪 (加鸡蛋 10 TL)"},
    {"name": "至尊什锦皮塔饼", "description": "招牌 'Hünkar 风格' 肉末混合物，融化的 Kaşar 奶酪，新鲜番茄，爽脆青椒 (加鸡蛋 10 TL)"},
    {"name": "慢烤牛肉皮塔饼", "description": "精选慢烤里泽牛肉 (Kavurma) (加鸡蛋 10 TL)"},
    {"name": "慢烤牛肉与奶酪", "description": "精选慢烤里泽牛肉 (Kavurma)，融化的手工 Kaşar 奶酪 (加鸡蛋 10 TL)"},
    {"name": "慢烤牛肉与蔬菜", "description": "精选慢烤里泽牛肉 (Kavurma)，新鲜番茄，爽脆青椒 (加鸡蛋 10 TL)"},
    {"name": "什锦慢烤牛肉蔬菜奶酪", "description": "精选慢烤里泽牛肉 (Kavurma)，融化的 Kaşar 奶酪，新鲜番茄，爽脆青椒 (加鸡蛋 10 TL)"},
    {"name": "融化奶酪皮塔饼", "description": "精选融化手工 Kaşar 奶酪 (加鸡蛋 10 TL)"},
    {"name": "奶酪与农场鲜蛋", "description": "融化的手工 Kaşar 奶酪，农场鲜蛋 (加鸡蛋 10 TL)"},
    {"name": "融化奶酪与蔬菜", "description": "融化的手工 Kaşar 奶酪，新鲜番茄，爽脆青椒 (加鸡蛋 10 TL)"},
    {"name": "香料牛肉肠与融化奶酪", "description": "土耳其香料牛肉肠 (Sucuk)，融化的手工 Kaşar 奶酪 (加鸡蛋 10 TL)"}
  ]},
  {"title": "皮塔饼 & 酥皮糕点", "items": [
    {"name": "传统烤皮塔饼 (Kır Pide)", "description": "柔软的手工面团，可选择调味肉末、奶酪或调味土豆"},
    {"name": "手工卷酥饼", "description": "手工卷制的薄脆面饼层，内含肉末、手工奶酪、土豆、菠菜或芝麻酱"},
    {"name": "奥斯曼式千层水酥饼", "description": "手工拉伸煮熟的面皮层，精选融化黄油，白手工奶酪"},
    {"name": "香酥黄油千层饼", "description": "手工卷制的薄脆面饼层，精选融化黄油。传统吃法是撒上厚厚的糖粉。"}
  ]},
  {"title": "各种饮料", "items": [
    {"name": "经典可乐", "description": ""},
    {"name": "土耳其苏打水", "description": "经典/橙子"},
    {"name": "果汁", "description": "桃子/酸樱桃/混合水果"},
    {"name": "冰茶", "description": "柠檬/桃子"},
    {"name": "咸酸奶饮料 (Ayran)", "description": ""},
    {"name": "矿泉水", "description": ""},
    {"name": "水", "description": ""},
    {"name": "正宗黑海茶", "description": ""},
    {"name": "手工制作柠檬水", "description": ""},
    {"name": "土耳其咖啡", "description": ""}
  ]}
]

it_sections = [
  {"title": "Consiglio dello Chef", "items": [{"name": "Pide del Mar Nero a Forma di Ghianda", "description": "Impasto Sottile e Croccante, Autentico Manzo Brasato di Rize, Burro, Forma di Ghianda, Consiglio dello Chef"}]},
  {"title": "Pide del Mar Nero", "items": [
    {"name": "Pide con Carne Macinata", "description": "Esclusivo mix di carne macinata in stile 'Hünkar' (Uovo extra 10 TL)"},
    {"name": "Carne Macinata e Verdure", "description": "Esclusivo mix di carne macinata in stile 'Hünkar', pomodori freschi, peperoni verdi croccanti (Uovo extra 10 TL)"},
    {"name": "Carne Macinata e Formaggio", "description": "Esclusivo mix di carne macinata in stile 'Hünkar', formaggio artigianale Kaşar fuso (Uovo extra 10 TL)"},
    {"name": "Mix Supremo", "description": "Esclusivo mix di carne macinata in stile 'Hünkar', formaggio Kaşar fuso, pomodori freschi, peperoni verdi croccanti (Uovo extra 10 TL)"},
    {"name": "Pide di Manzo Arrosto", "description": "Pregiato manzo di Rize arrostito a fuoco lento (Kavurma) (Uovo extra 10 TL)"},
    {"name": "Manzo Arrosto e Formaggio", "description": "Pregiato manzo di Rize arrostito a fuoco lento (Kavurma), formaggio artigianale Kaşar fuso (Uovo extra 10 TL)"},
    {"name": "Manzo Arrosto e Verdure", "description": "Pregiato manzo di Rize arrostito a fuoco lento (Kavurma), pomodori freschi, peperoni verdi croccanti (Uovo extra 10 TL)"},
    {"name": "Mix di Manzo Arrosto e Verdure al Formaggio", "description": "Pregiato manzo di Rize arrostito a fuoco lento (Kavurma), formaggio Kaşar fuso, pomodori freschi, peperoni verdi croccanti (Uovo extra 10 TL)"},
    {"name": "Pide al Formaggio Fuso", "description": "Pregiato formaggio artigianale Kaşar fuso (Uovo extra 10 TL)"},
    {"name": "Formaggio e Uovo di Fattoria", "description": "Formaggio artigianale Kaşar fuso, uovo fresco di fattoria (Uovo extra 10 TL)"},
    {"name": "Formaggio Fuso e Verdure", "description": "Formaggio artigianale Kaşar fuso, pomodori freschi, peperoni verdi croccanti (Uovo extra 10 TL)"},
    {"name": "Salsiccia di Manzo Speziata e Formaggio Fuso", "description": "Salsiccia di manzo turca speziata (Sucuk), formaggio artigianale Kaşar fuso (Uovo extra 10 TL)"}
  ]},
  {"title": "Pide & Börek", "items": [
    {"name": "Pide Kır Tradizionale", "description": "Morbido impasto artigianale con scelta di carne piccata speziata, formaggio o patate speziate"},
    {"name": "Sfoglia Arrotolata", "description": "Strati di impasto croccante stesi a mano con carne macinata, formaggio artigianale, patate, spinaci o salsa tahina"},
    {"name": "Sfoglia a Strati in Stile Ottomano", "description": "Strati di impasto bollito stesi a mano, burro fuso della migliore qualità, formaggio bianco artigianale"},
    {"name": "Sfoglia Friabile al Burro", "description": "Strati di impasto croccante stesi a mano, burro fuso della migliore qualità. Tradizionalmente gustata con un'abbondante spolverata di zucchero a velo."}
  ]},
  {"title": "Bevande", "items": [
    {"name": "Cola Classica", "description": ""},
    {"name": "Gassosa Turca (Gazoz)", "description": "Classico/Arancia"},
    {"name": "Succo di Frutta", "description": "Pesca/Amarena/Frutta Mista"},
    {"name": "Tè Freddo", "description": "Limone/Pesca"},
    {"name": "Ayran (Bevanda allo Yogurt)", "description": ""},
    {"name": "Acqua Minerale", "description": ""},
    {"name": "Acqua", "description": ""},
    {"name": "Autentico Tè del Mar Nero", "description": ""},
    {"name": "Limonada Artigianale", "description": ""},
    {"name": "Caffè Turco", "description": ""}
  ]}
]

fr_sections = [
  {"title": "Recommandation du Chef", "items": [{"name": "Pide de la Mer Noire en Forme de Gland", "description": "Pâte Fine et Croustillante, Bœuf Braisé de Rize Authentique, Beurre, Forme de Gland, Recommandation du Chef"}]},
  {"title": "Pide de la Mer Noire", "items": [
    {"name": "Pide à la Viande Hachée", "description": "Mélange exclusif de viande hachée façon 'Hünkar' (Œuf supplémentaire 10 TL)"},
    {"name": "Viande Hachée et Légumes", "description": "Mélange exclusif de viande hachée façon 'Hünkar', tomates fraîches, poivrons verts croquants (Œuf supplémentaire 10 TL)"},
    {"name": "Viande Hachée et Fromage", "description": "Mélange exclusif de viande hachée façon 'Hünkar', fromage artisanal Kaşar fondu (Œuf supplémentaire 10 TL)"},
    {"name": "Le Mixte Suprême", "description": "Mélange exclusif de viande hachée façon 'Hünkar', fromage Kaşar fondu, tomates fraîches, poivrons verts croquants (Œuf supplémentaire 10 TL)"},
    {"name": "Pide au Bœuf Rôti", "description": "Bœuf de Rize rôti lentement de première qualité (Kavurma) (Œuf supplémentaire 10 TL)"},
    {"name": "Bœuf Rôti et Fromage", "description": "Bœuf de Rize rôti lentement de première qualité (Kavurma), fromage artisanal Kaşar fondu (Œuf supplémentaire 10 TL)"},
    {"name": "Bœuf Rôti et Légumes", "description": "Bœuf de Rize rôti lentement de première qualité (Kavurma), tomates fraîches, poivrons verts croquants (Œuf supplémentaire 10 TL)"},
    {"name": "Mixte de Bœuf Rôti, Légumes et Fromage Fondu", "description": "Bœuf de Rize rôti lentement de première qualité (Kavurma), fromage Kaşar fondu, tomates fraîches, poivrons verts croquants (Œuf supplémentaire 10 TL)"},
    {"name": "Pide au Fromage Fondu", "description": "Fromage artisanal Kaşar premium fondu (Œuf supplémentaire 10 TL)"},
    {"name": "Fromage et Œuf Frais de la Ferme", "description": "Fromage artisanal Kaşar fondu, œuf frais de la ferme (Œuf supplémentaire 10 TL)"},
    {"name": "Fromage Fondu et Légumes", "description": "Fromage artisanal Kaşar fondu, tomates fraîches, poivrons verts croquants (Œuf supplémentaire 10 TL)"},
    {"name": "Saucisse de Bœuf Épicée et Fromage Fondu", "description": "Saucisse de bœuf turque épicée (Sucuk), fromage artisanal Kaşar fondu (Œuf supplémentaire 10 TL)"}
  ]},
  {"title": "Pide et Börek", "items": [
    {"name": "Pide Kır Traditionnelle", "description": "Pâte artisanale molle with au choix de la viande hachée assaisonnée, du fromage ou des pommes de terre assaisonnées"},
    {"name": "Pâtisserie Roulée", "description": "Couches de pâte croustillante roulées à la main avec viande hachée, fromage artisanal, pommes de terre, épinards ou tahini"},
    {"name": "Pâtisserie Superposée de Style Ottoman", "description": "Couches de pâte bouillie étirée à la main, beurre fondu de première qualité, fromage blanc artisanal"},
    {"name": "Pâtisserie Feuilletée au Beurre", "description": "Couches de pâte croustillante roulées à la main, beurre fondu de première qualité. Se déguste traditionnellement avec un généreux saupoudrage de sucre glace."}
  ]},
  {"title": "Boissons", "items": [
    {"name": "Cola Classique", "description": ""},
    {"name": "Soda Turc (Gazoz)", "description": "Classique/Orange"},
    {"name": "Jus de Fruits", "description": "Pêche/Cerise Griotte/Fruits Mixtes"},
    {"name": "Thé Glacé", "description": "Citron/Pêche"},
    {"name": "Ayran", "description": ""},
    {"name": "Eau Minérale", "description": ""},
    {"name": "Eau", "description": ""},
    {"name": "Thé Authentique de la Mer Noire", "description": ""},
    {"name": "Limonade Artisanale", "description": ""},
    {"name": "Café Turc", "description": ""}
  ]}
]

ru_sections = [
  {"title": "Рекомендация Шеф-Повара", "items": [{"name": "Черноморская Пита в Форме Желудя", "description": "Тонкое Хрустящее Тесто, Аутентичная Тушеная Говядина Ризе, Сливочное Масло, Форма Желудя, Рекомендация Шеф-Повара"}]},
  {"title": "Черноморская Пита", "items": [
    {"name": "Пита с Мясным Фаршем", "description": "Фирменная смесь мясного фарша в стиле 'Hünkar' (Дополнительное яйцо 10 TL)"},
    {"name": "Мясной Фарш и Овощи", "description": "Фирменная смесь мясного фарша в стиле 'Hünkar', свежие помидоры, хрустящий зеленый перец (Дополнительное яйцо 10 TL)"},
    {"name": "Мясной Фарш и Сыр", "description": "Фирменная смесь мясного фарша в стиле 'Hünkar', расплавленный ремесленный сыр Кашар (Дополнительное яйцо 10 TL)"},
    {"name": "Супер Микс с Фаршем", "description": "Фирменная смесь мясного фарша в стиле 'Hünkar', расплавленный сыр Кашар, свежие помидоры, хрустящий зеленый перец (Дополнительное яйцо 10 TL)"},
    {"name": "Пита с Жареной Говядиной", "description": "Говядина Ризе медленной обжарки премиум-класса (Кавурма) (Дополнительное яйцо 10 TL)"},
    {"name": "Жареная Говядина и Сыр", "description": "Говядина Ризе медленной обжарки премиум-класса (Кавурма), расплавленный ремесленный сыр Кашар (Дополнительное яйцо 10 TL)"},
    {"name": "Жареная Говядина и Овощи", "description": "Говядина Ризе медленной обжарки премиум-класса (Кавурма), свежие помидоры, хрустящий зеленый перец (Дополнительное яйцо 10 TL)"},
    {"name": "Микс: Жареная Говядина, Овощи и Сыр", "description": "Говядина Ризе медленной обжарки премиум-класса (Кавурма), расплавленный сыр Кашар, свежие помидоры, хрустящий зеленый перец (Дополнительное яйцо 10 TL)"},
    {"name": "Пита с Расплавленным Сыром", "description": "Расплавленный премиальный ремесленный сыр Кашар (Дополнительное яйцо 10 TL)"},
    {"name": "Сыр и Фермерское Яйцо", "description": "Расплавленный ремесленный сыр Кашар, свежее фермерское яйцо (Дополнительное яйцо 10 TL)"},
    {"name": "Расплавленный Сыр и Овощи", "description": "Расплавленный ремесленный сыр Кашар, свежие помидоры, хрустящий зеленый перец (Дополнительное яйцо 10 TL)"},
    {"name": "Пряная Говяжья Колбаса и Расплавленный Сыр", "description": "Пряная турецкая говяжья колбаса (Суджук), расплавленный ремесленный сыр Кашар (Дополнительное яйцо 10 TL)"}
  ]},
  {"title": "Пита и Бёрек", "items": [
    {"name": "Традиционная Кыр Пита", "description": "Мягкое ремесленное тесто с начинкой на ваш выбор: приправленный мясной фарш, сыр или приправленный картофель"},
    {"name": "Рулет из Теста", "description": "Слои тонкого хрустящего теста ручной раскатки с мясным фаршем, ремесленным сыром, картофелем, шпинатом или тахини"},
    {"name": "Слоеное Тесто в Османском Стиле", "description": "Слои вареного теста ручной раскатки, топленое масло премиум-класса, белый ремесленный сыр"},
    {"name": "Рассыпчатая Слойка с Маслом", "description": "Слои тонкого хрустящего теста ручной раскатки, топленое масло премиум-класса. Традиционно подается с щедрой посыпкой из сахарной пудры."}
  ]},
  {"title": "Напитки", "items": [
    {"name": "Классическая Кола", "description": ""},
    {"name": "Турецкая Газировка (Газоз)", "description": "Классический/Апельсиновый"},
    {"name": "Фруктовый Сок", "description": "Персиковый/Вишневый/Мультифрукт"},
    {"name": "Холодный Чай", "description": "Лимонный/Персиковый"},
    {"name": "Айран", "description": ""},
    {"name": "Минеральная Вода", "description": ""},
    {"name": "Вода", "description": ""},
    {"name": "Аутентичный Черноморский Чай", "description": ""},
    {"name": "Лимонад Ручной Работы", "description": ""},
    {"name": "Турецкий Кофе", "description": ""}
  ]}
]

fa_sections = [
  {"title": "پیشنهاد سرآشپز", "items": [{"name": "پیده دریای سیاه به شکل بلوط", "description": "خمیر نازک و ترد، گوشت گاو بریان شده اصیل ریزه، کره، شکل بلوط، پیشنهاد سرآشپز"}]},
  {"title": "پیده دریای سیاه", "items": [
    {"name": "پیده گوشت چرخ کرده", "description": "مخلوط گوشت چرخ کرده ویژه به سبک 'Hünkar' (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "گوشت چرخ کرده و سبزیجات", "description": "مخلوط گوشت چرخ کرده ویژه به سبک 'Hünkar'، گوجه فرنگی تازه، فلفل سبز ترد (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "گوشت چرخ کرده و پنیر", "description": "مخلوط گوشت چرخ کرده ویژه به سبک 'Hünkar'، پنیر ذوب شده دست‌ساز کاشار (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "پیده مخلوط ویژه", "description": "مخلوط گوشت چرخ کرده ویژه به سبک 'Hünkar'، پنیر ذوب شده کاشار، گوجه فرنگی تازه، فلفل سبز ترد (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "پیده با گوشت بریان", "description": "گوشت گاو بریان شده بسیار مرغوب ریزه (Kavurma) (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "گوشت بریان و پنیر", "description": "گوشت گاو بریان شده بسیار مرغوب ریزه (Kavurma)، پنیر ذوب شده دست‌ساز کاشار (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "گوشت بریان و سبزیجات", "description": "گوشت گاو بریان شده بسیار مرغوب ریزه (Kavurma)، گوجه فرنگی تازه، فلفل سبز ترد (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "مخلوط گوشت بریان و سبزیجات با پنیر در ذوب", "description": "گوشت گاو بریان شده بسیار مرغوب ریزه (Kavurma)، پنیر ذوب شده کاشار، گوجه فرنگی تازه، فلفل سبز ترد (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "پیده پنیر ذوب شده", "description": "پنیر بسیار مرغوب دست‌ساز و ذوب شده کاشار (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "پنیر و تخم مرغ مزرعه", "description": "پنیر ذوب شده دست‌ساز کاشار، تخم مرغ تازه مزرعه (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "پنیر ذوب شده و سبزیجات", "description": "پنیر ذوب شده دست‌ساز کاشار، گوجه فرنگی تازه، فلفل سبز ترد (تخم مرغ اضافی ۱۰ لیر)"},
    {"name": "سوسیس تند گاو و پنیر ذوب شده", "description": "سوسیس گوشت گاو ترکی تند (Sucuk)، پنیر ذوب شده دست‌ساز کاشار (تخم مرغ اضافی ۱۰ لیر)"}
  ]},
  {"title": "پیده و بورک", "items": [
    {"name": "کیر پیده سنتی", "description": "خمیر دست‌ساز نرم با انتخاب گوشت چرخ کرده طعم‌دار، پنیر یا سیب زمینی طعم‌دار"},
    {"name": "شیرینی لوله‌ای (رول)", "description": "لایه‌های خمیر ترد رول شده با دست با گوشت چرخ کرده، پنیر دست‌ساز، سیب زمینی، اسفناج یا ارده"},
    {"name": "شیرینی لایه‌ای به سبک عثمانی", "description": "لایه‌های خمیر جوشیده شده با دست، کره ذوب شده درجه یک، پنیر سفید دست‌ساز"},
    {"name": "شیرینی کره‌ای ورقه‌ای", "description": "لایه‌های خمیر ترد رول شده با دست، کره ذوب شده درجه یک. به طور سنتی با مقدار زیادی پودر قند لذت بخش است."}
  ]},
  {"title": "نوشیدنی‌ها", "items": [
    {"name": "نوشابه کاولا", "description": ""},
    {"name": "نوشابه گازدار ترکی", "description": "کلاسیک/پرتقالی"},
    {"name": "آبمیوه", "description": "هلو/آلبالو/مخلوط میوه‌ها"},
    {"name": "چای سرد", "description": "لیمو/هلو"},
    {"name": "دوغ (آیران)", "description": ""},
    {"name": "آب معدنی", "description": ""},
    {"name": "آب", "description": ""},
    {"name": "چای اصیل دریای سیاه", "description": ""},
    {"name": "لیموناد دست‌ساز", "description": ""},
    {"name": "قهوه ترک", "description": ""}
  ]}
]

# We must get TR sections dynamically from the original file 
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Match both constants
menu_regex = r'const MENU_DATA = (\{.*?\});'
images_regex = r'const IMAGES = (\{.*?\});'

menu_match = re.search(menu_regex, html_content, re.DOTALL)
images_match = re.search(images_regex, html_content, re.DOTALL)

if not menu_match or not images_match:
    print("Error: Could not find MENU_DATA or IMAGES constants in index.html")
    exit(1)

merged_data = json.loads(menu_match.group(1))

# Assign the base sections
def populate_prices(secs):
    item_idx = 1
    for s in secs:
        for i in s['items']:
            i['price'] = price_map[item_idx]
            item_idx += 1
    return secs

merged_data['tr']['sections'] = populate_prices(tr_sections)
merged_data['en']['sections'] = populate_prices(en_sections)
merged_data['es']['sections'] = populate_prices(es_sections)
merged_data['ar']['sections'] = populate_prices(ar_sections)
merged_data['zh']['sections'] = populate_prices(zh_sections)
merged_data['it']['sections'] = populate_prices(it_sections)
merged_data['fr']['sections'] = populate_prices(fr_sections)
merged_data['ru']['sections'] = populate_prices(ru_sections)
merged_data['fa']['sections'] = populate_prices(fa_sections)

# Update MENU_DATA in HTML
new_menu_json_str = json.dumps(merged_data, ensure_ascii=False)
html_content = html_content.replace(menu_match.group(0), f'const MENU_DATA = {new_menu_json_str};')

# Update IMAGES in HTML
try:
    with open('Menu_Generator_Source/images_base64.json', 'r', encoding='utf-8') as f:
        source_images = json.load(f)
    
    # Map the current TR names to the source image keys
    image_key_map = {
        "Palamut Pide": "Palamut Formunda Kapatılmış Karadeniz Pidesi",
        "Kıymalı Pide": "Kıymalı",
        "Kavurmalı Pide": "Kavurmalı",
        "Kaşarlı Pide": "Kaşarlı"
    }
    
    new_images = {}
    for section in tr_sections:
        for item in section['items']:
            name = item['name']
            source_key = image_key_map.get(name, name)
            if source_key in source_images:
                new_images[name] = source_images[source_key]
            else:
                print(f"Warning: Image not found for {name} (tried key: {source_key})")
    
    new_images_json_str = json.dumps(new_images, ensure_ascii=False)
    html_content = html_content.replace(images_match.group(0), f'const IMAGES = {new_images_json_str};')
    print("Images successfully synced and updated!")
except FileNotFoundError:
    print("Warning: Menu_Generator_Source/images_base64.json not found. Skipping image sync.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file successfully updated with new English baselines and synced images!")
