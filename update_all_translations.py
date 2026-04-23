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

bs_sections = [
  {"title": "Šefova preporuka", "items": [{"name": "Crnomorski pide u obliku žira", "description": "Tanko hrskavo tijesto, autentična Rize kavurma, puter, oblik žira, preporuka šefa"}]},
  {"title": "Crnomorski pide", "items": [
    {"name": "Pide sa mljevenim mesom", "description": "Specijalni fil od mljevenog mesa na Hünkar način (Ekstra jaje 10 TL)"},
    {"name": "Mljeveno meso i povrće", "description": "Specijalni fil od mljevenog mesa na Hünkar način, svježi paradajz, hrskava zelena paprika (Ekstra jaje 10 TL)"},
    {"name": "Mljeveno meso i artisan sir", "description": "Specijalni fil od mljevenog mesa na Hünkar način, otopljeni artisan Kašar sir (Ekstra jaje 10 TL)"},
    {"name": "Vrhunski miješani pide", "description": "Specijalni fil od mljevenog mesa na Hünkar način, otopljeni Kašar sir, svježi paradajz, hrskava zelena paprika (Ekstra jaje 10 TL)"},
    {"name": "Pide sa pečenom govedinom", "description": "Vrhunska sporo pečena Rize govedina (Kavurma) (Ekstra jaje 10 TL)"},
    {"name": "Pečena govedina i artisan sir", "description": "Vrhunska sporo pečena Rize govedina (Kavurma), otopljeni artisan Kašar sir (Ekstra jaje 10 TL)"},
    {"name": "Pečena govedina i povrće", "description": "Vrhunska sporo pečena Rize govedina (Kavurma), svježi paradajz, hrskava zelena paprika (Ekstra jaje 10 TL)"},
    {"name": "Miješana govedina, povrće i sir", "description": "Vrhunska sporo pečena Rize govedina (Kavurma), otopljeni Kašar sir, svježi paradajz, hrskava zelena paprika (Ekstra jaje 10 TL)"},
    {"name": "Pide sa otopljenim artisan sirom", "description": "Otopljeni vrhunski artisan Kašar sir (Ekstra jaje 10 TL)"},
    {"name": "Artisan sir i svježe jaje", "description": "Otopljeni artisan Kašar sir, domaće svježe jaje (Ekstra jaje 10 TL)"},
    {"name": "Otopljeni sir i povrće", "description": "Otopljeni artisan Kašar sir, svježi paradajz, hrskava zelena paprika (Ekstra jaje 10 TL)"},
    {"name": "Začinjena goveđa kobasica i sir", "description": "Začinjena turska goveđa kobasica (Sucuk), otopljeni artisan Kašar sir (Ekstra jaje 10 TL)"}
  ]},
  {"title": "Pide & Pita", "items": [
    {"name": "Tradicionalni Kır pide", "description": "Meko artisan tijesto sa izborom začinjenog mljevenog mesa, sira ili krompira"},
    {"name": "Rolovana pita (Kol böreği)", "description": "Ručno rađeno hrskavo tijesto sa mljevenim mesom, artisan sirom, krompirom, špinatom ili tahinijem"},
    {"name": "Slojevita pita u osmanskom stilu", "description": "Ručno razvijeno kuhano tijesto (Su böreği), vrhunski puter, artisan bijeli sir"},
    {"name": "Prhka pita sa puterom", "description": "Ručno rađeno hrskavo tijesto, vrhunski puter. Tradicionalno se služi sa šećerom u prahu."}
  ]},
  {"title": "Pića", "items": [
    {"name": "Cola", "description": ""},
    {"name": "Gazirani sok", "description": "Klasični/Narandža"},
    {"name": "Voćni sok", "description": "Breskva/Višnja/Miješano"},
    {"name": "Ledeni čaj", "description": "Limun/Breskva"},
    {"name": "Ayran", "description": ""},
    {"name": "Mineralna voda", "description": ""},
    {"name": "Voda", "description": ""},
    {"name": "Autentični čaj", "description": ""},
    {"name": "Domaća limunada", "description": ""},
    {"name": "Turska kafa", "description": ""}
  ]}
]

sq_sections = [
  {"title": "Sugjerimi i shefit", "items": [{"name": "Pide e Detit të Zi në formë lisi", "description": "Brumë i hollë krokant, kavurmë autentike Rize, gjalpë, në formë lisi, sugjerimi i shefit"}]},
  {"title": "Pide e Detit të Zi", "items": [
    {"name": "Pide me mish të grirë", "description": "Mbushje speciale me mish të grirë sipas mënyrës Hünkar (Vezë ekstra 10 TL)"},
    {"name": "Mish i grirë dhe perime", "description": "Mbushje speciale me mish të grirë sipas mënyrës Hünkar, domate të freskëta, spec i gjelbër krokant (Vezë ekstra 10 TL)"},
    {"name": "Mish i grirë dhe djathë artizanal", "description": "Mbushje speciale me mish të grirë sipas mënyrës Hünkar, djathë kaçkavall artizanal i shkrirë (Vezë ekstra 10 TL)"},
    {"name": "Pide e përzier supreme", "description": "Mbushje speciale me mish të grirë sipas mënyrës Hünkar, djathë kaçkavall i shkrirë, domate të freskëta, spec i gjelbër krokant (Vezë ekstra 10 TL)"},
    {"name": "Pide me mish viçi të pjekur", "description": "Mish viçi Rize i pjekur ngadalë (Kavurma) (Vezë ekstra 10 TL)"},
    {"name": "Mish i pjekur dhe djathë artizanal", "description": "Mish viçi Rize i pjekur ngadalë (Kavurma), djathë kaçkavall artizanal i shkrirë (Vezë ekstra 10 TL)"},
    {"name": "Mish i pjekur dhe perime", "description": "Mish viçi Rize i pjekur ngadalë (Kavurma), domate të freskëta, spec i gjelbër krokant (Vezë ekstra 10 TL)"},
    {"name": "Mish i pjekur, perime dhe djathë", "description": "Mish viçi Rize i pjekur ngadalë (Kavurma), djathë kaçkavall i shkrirë, domate të freskëta, spec i gjelbër krokant (Vezë ekstra 10 TL)"},
    {"name": "Pide me djathë artizanal të shkrirë", "description": "Djathë kaçkavall artizanal i shkrirë (Vezë ekstra 10 TL)"},
    {"name": "Djathë artizanal dhe vezë fshati", "description": "Djathë kaçkavall artizanal i shkrirë, vezë fshati e freskët (Vezë ekstra 10 TL)"},
    {"name": "Djathë i shkrirë dhe perime", "description": "Djathë kaçkavall artizanal i shkrirë, domate të freskëta, spec i gjelbër krokant (Vezë ekstra 10 TL)"},
    {"name": "Salsiçe viçi me erëza dhe djathë", "description": "Salsiçe viçi turke me erëza (Sucuk), djathë kaçkavall artizanal i shkrirë (Vezë ekstra 10 TL)"}
  ]},
  {"title": "Pide & Byrek", "items": [
    {"name": "Pide Kır tradicionale", "description": "Brumë artizanal i butë me zgjedhjen tuaj të mishit të grirë, djathit ose patateve"},
    {"name": "Byrek i rrotulluar (Kol böreği)", "description": "Shtresa brumi krokant të rrotulluara me dorë me mish të grirë, djathë artizanal, patate, spinaq ose tahini"},
    {"name": "Byrek me shtresa i stilit osman", "description": "Shtresa brumi të ziera të punuara me dorë (Su böreği), gjalpë i shkrirë, djathë i bardhë artizanal"},
    {"name": "Byrek me gjalpë", "description": "Shtresa brumi krokant të punuara me dorë, gjalpë i shkrirë. Tradicionalisht shijohet me sheqer pluhur."}
  ]},
  {"title": "Pije", "items": [
    {"name": "Kola", "description": ""},
    {"name": "Pije me gaz", "description": "Klasike/Portokall"},
    {"name": "Lëng frutash", "description": "Pjeshkë/Qershi/I përzier"},
    {"name": "Iced Tea", "description": "Limon/Pjeshkë"},
    {"name": "Ajran", "description": ""},
    {"name": "Ujë mineral", "description": ""},
    {"name": "Ujë", "description": ""},
    {"name": "Çaj autentik", "description": ""},
    {"name": "Limonatë artizanale", "description": ""},
    {"name": "Kafe turke", "description": ""}
  ]}
]

de_sections = [
  {"title": "Empfehlung des Küchenchefs", "items": [{"name": "Schwarzmeer-Pide in Eichelform", "description": "Dünner knuspriger Teig, authentisches Rize-Kavurma, Butter, Eichelform, Empfehlung des Chefs"}]},
  {"title": "Schwarzmeer-Pide", "items": [
    {"name": "Pide mit Hackfleisch", "description": "Hünkar-Spezialmischung mit Hackfleisch (Extra Ei 10 TL)"},
    {"name": "Hackfleisch & Gemüse", "description": "Hünkar-Spezialmischung mit Hackfleisch, frische Tomaten, knackige grüne Paprika (Extra Ei 10 TL)"},
    {"name": "Hackfleisch & Käse", "description": "Hünkar-Spezialmischung mit Hackfleisch, geschmolzener Artisan-Kaşar-Käse (Extra Ei 10 TL)"},
    {"name": "Vrhunski Mixed Pide", "description": "Hünkar-Spezialmischung mit Hackfleisch, geschmolzener Kaşar-Käse, frische Tomaten, knackige grüne Paprika (Extra Ei 10 TL)"},
    {"name": "Pide mit Röstfleisch", "description": "Premium Rize-Kavurma (langsam geröstetes Rindfleisch) (Extra Ei 10 TL)"},
    {"name": "Röstfleisch & Käse", "description": "Premium Rize-Kavurma, geschmolzener Artisan-Kaşar-Käse (Extra Ei 10 TL)"},
    {"name": "Röstfleisch & Gemüse", "description": "Premium Rize-Kavurma, frische Tomaten, knackige grüne Paprika (Extra Ei 10 TL)"},
    {"name": "Mixed Röstfleisch & Gemüse", "description": "Premium Rize-Kavurma, geschmolzener Kaşar-Käse, frische Tomaten, knackige grüne Paprika (Extra Ei 10 TL)"},
    {"name": "Pide mit geschmolzenem Artisan-Käse", "description": "Geschmolzener Premium Artisan-Kaşar-Käse (Extra Ei 10 TL)"},
    {"name": "Käse & frisches Land-Ei", "description": "Geschmolzener Artisan-Kaşar-Käse, frisches Land-Ei (Extra Ei 10 TL)"},
    {"name": "Geschmolzener Käse & Gemüse", "description": "Geschmolzener Artisan-Kaşar-Käse, frische Tomaten, knackige grüne Paprika (Extra Ei 10 TL)"},
    {"name": "Würzige Rinderwurst & Käse", "description": "Würzige türkische Rinderwurst (Sucuk), geschmolzener Artisan-Kaşar-Käse (Extra Ei 10 TL)"}
  ]},
  {"title": "Pide & Börek", "items": [
    {"name": "Traditionelles Kır Pide", "description": "Weicher Artisan-Teig mit Hackfleisch-, Käse- oder Kartoffelfüllung"},
    {"name": "Gerolltes Gebäck (Kol böreği)", "description": "Handgerollte knusprige Teigschichten mit Hackfleisch, Käse, Kartoffeln, Spinat oder Tahini"},
    {"name": "Geschichtetes Gebäck nach osmanischer Art", "description": "Handgezogene gekochte Teigschichten (Su böreği), feine Butter, Artisan-Weißkäse"},
    {"name": "Blättriges Buttergebäck", "description": "Handgerollte knusprige Teigschichten, feine Butter. Traditionell mit Puderzucker serviert."}
  ]},
  {"title": "Getränke", "items": [
    {"name": "Cola", "description": ""},
    {"name": "Türkische Limonade", "description": "Klassisch/Orange"},
    {"name": "Fruchtsaft", "description": "Pfirsich/Sauerkirsche/Gemischt"},
    {"name": "Eistee", "description": "Zitrone/Pfirsich"},
    {"name": "Ayran", "description": ""},
    {"name": "Mineralwasser", "description": ""},
    {"name": "Wasser", "description": ""},
    {"name": "Authentischer Schwarzmeer-Tee", "description": ""},
    {"name": "Hausgemachte Limonade", "description": ""},
    {"name": "Türkischer Kaffee", "description": ""}
  ]}
]

bg_sections = [
  {"title": "Препоръка на главния готвач", "items": [{"name": "Черноморско пиде с форма на жълъд", "description": "Тънко хрупкаво тесто, автентична Риза кавурма, масло, форма на жълъд, препоръка на шефа"}]},
  {"title": "Черноморско пиде", "items": [
    {"name": "Пиде с кайма", "description": "Специална смес от кайма по стил Hünkar (Екстра яйце 10 TL)"},
    {"name": "Кайма и зеленчуци", "description": "Специална смес от кайма по стил Hünkar, пресни домати, хрупкави зелени чушки (Екстра яйце 10 TL)"},
    {"name": "Кайма и занаятчийско сирене", "description": "Специална смес от кайма по стил Hünkar, разтопено занаятчийско сирене Кашкавал (Екстра яйце 10 TL)"},
    {"name": "Върховно смесено пиде", "description": "Специална смес от кайма по стил Hünkar, разтопен кашкавал, пресни домати, хрупкави зелени чушки (Екстра яйце 10 TL)"},
    {"name": "Пиде с печено говеждо", "description": "Първокласно бавно печено говеждо Риза (Кавурма) (Екстра яйце 10 TL)"},
    {"name": "Печено говеждо и занаятчийско сирене", "description": "Първокласно бавно печено говеждо Риза (Кавурма), разтопено занаятчийско сирене Кашкавал (Екстра яйце 10 TL)"},
    {"name": "Печено говеждо и зеленчуци", "description": "Първокласно бавно печено говеждо Риза (Кавурма), пресни домати, хрупкави зелени чушки (Екстра яйце 10 TL)"},
    {"name": "Смесено печено говеждо и зеленчуци", "description": "Първокласно бавно печено говеждо Риза (Кавурма), разтопен кашкавал, пресни домати, хрупкави зелени чушки (Екстра яйце 10 TL)"},
    {"name": "Пиде с разтопено занаятчийско сирене", "description": "Разтопено първокласно занаятчийско сирене Кашкавал (Екстра яйце 10 TL)"},
    {"name": "Сирене и прясно селско яйце", "description": "Разтопено занаятчийско сирене Кашкавал, прясно селско яйце (Екстра яйце 10 TL)"},
    {"name": "Разтопено сирене и зеленчуци", "description": "Разтопено занаятчийско сирене Кашкавал, пресни домати, хрупкави зелени чушки (Екстра яйце 10 TL)"},
    {"name": "Пикантен говежди салам и сирене", "description": "Пикантен турски говежди салам (Суджук), разтопено занаятчийско сирене Кашкавал (Екстра яйце 10 TL)"}
  ]},
  {"title": "Пиде и Бюрек", "items": [
    {"name": "Традиционно Кър пиде", "description": "Меко занаятчийско тесто с избор от кайма, сирене или картофи"},
    {"name": "Навита баница (Kol böreği)", "description": "Ръчно навити хрупкави кори с кайма, занаятчийско сирене, картофи, спанак или тахан"},
    {"name": "Слоена баница в османски стил", "description": "Ръчно разточени варени кори (Su böreği), първокласно масло, занаятчийско бяло сирене"},
    {"name": "Маслена хрупкава баница", "description": "Ръчно навити хрупкави кори, първокласно масло. Традиционно се сервира с пудра захар."}
  ]},
  {"title": "Напитки", "items": [
    {"name": "Кола", "description": ""},
    {"name": "Турска газирана напитка", "description": "Класик/Портокал"},
    {"name": "Плодов сок", "description": "Праскова/Вишна/Микс"},
    {"name": "Студен чай", "description": "Лимон/Праскова"},
    {"name": "Айрян", "description": ""},
    {"name": "Минерална вода", "description": ""},
    {"name": "Вода", "description": ""},
    {"name": "Автентичен турски чай", "description": ""},
    {"name": "Ръчно правена лимонада", "description": ""},
    {"name": "Турско кафе", "description": ""}
  ]}
]

el_sections = [
  {"title": "Πρόταση του Σεφ", "items": [{"name": "Πίντε Μαύρης Θάλασσας σε σχήμα βελανιδιού", "description": "Λεπτή τραγανή ζύμη, αυθεντικό καβουρμά Ριζέ, βούτυρο, σχήμα βελανιδιού, πρόταση του σεφ"}]},
  {"title": "Πίντε Μαύρης Θάλασσας", "items": [
    {"name": "Πίντε με κιμά", "description": "Ειδικό μείγμα κιμά σε στυλ Hünkar (Έξτρα αυγό 10 TL)"},
    {"name": "Κιμάς & λαχανικά", "description": "Ειδικό μείγμα κιμά σε στυλ Hünkar, φρέσκια ντομάτα, τραγανή πράσινη πιπεριά (Έξτρα αυγό 10 TL)"},
    {"name": "Κιμάς & χειροποίητο κασέρι", "description": "Ειδικό μείγμα κιμά σε στυλ Hünkar, λιωμένο χειροποίητο κασέρι (Έξτρα αυγό 10 TL)"},
    {"name": "Πίντε Σουπρίμ ανάμεικτο", "description": "Ειδικό μείγμα κιμά σε στυλ Hünkar, λιωμένο κασέρι, φρέσκια ντομάτα, τραγανή πράσινη πιπεριά (Έξτρα αυγό 10 TL)"},
    {"name": "Πίντε με ψητό μοσχάρι", "description": "Εκλεκτό σιγοψημένο μοσχάρι Ριζέ (Καβουρμάς) (Έξτρα αυγό 10 TL)"},
    {"name": "Ψητό μοσχάρι & χειροποίητο κασέρι", "description": "Εκλεκτό σιγοψημένο μοσχάρι Ριζέ (Καβουρμάς), λιωμένο χειροποίητο κασέρι (Έξτρα αυγό 10 TL)"},
    {"name": "Ψητό μοσχάρι & λαχανικά", "description": "Εκλεκτό σιγοψημένο μοσχάρι Ριζέ (Καβουρμάς), φρέσκια ντομάτα, τραγανή πράσινη πιπεριά (Έξτρα αυγό 10 TL)"},
    {"name": "Ανάμεικτο ψητό μοσχάρι & λαχανικά", "description": "Εκλεκτό σιγοψημένο μοσχάρι Ριζέ (Καβουρμάς), λιωμένο κασέρι, φρέσκια ντομάτα, τραγανή πράσινη πιπεριά (Έξτρα αυγό 10 TL)"},
    {"name": "Πίντε με λιωμένο χειροποίητο κασέρι", "description": "Λιωμένο εκλεκτό χειροποίητο κασέρι (Έξτρα αυγό 10 TL)"},
    {"name": "Κασέρι & φρέσκο χωριάτικο αυγό", "description": "Λιωμένο χειροποίητο κασέρι, φρέσκο χωριάτικο αυγό (Έξτρα αυγό 10 TL)"},
    {"name": "Λιωμένο κασέρι & λαχανικά", "description": "Λιωμένο χειροποίητο κασέρι, φρέσκια ντομάτα, τραγανή πράσινη πιπεριά (Έξτρα αυγό 10 TL)"},
    {"name": "Πικάντικο μοσχαρίσιο λουκάνικο & κασέρι", "description": "Πικάντικο τούρκικο μοσχαρίσιο λουκάνικο (Σουτζούκι), λιωμένο χειροποίητο κασέρι (Έξτρα αυγό 10 TL)"}
  ]},
  {"title": "Πίντε & Μπουρέκι", "items": [
    {"name": "Παραδοσιακό Κιρ Πίντε", "description": "Μαλακή χειροποίητη ζύμη με επιλογή από κιμά, τυρί ή πατάτα"},
    {"name": "Τυλιχτή πίτα (Kol böreği)", "description": "Χειροποίητα τραγανά φύλλα με κιμά, χειροποίητο τυρί, πατάτα, σπανάκι ή ταχίνι"},
    {"name": "Πίτα με στρώσεις οθωμανικού τύπου", "description": "Χειροποίητα βραστά φύλλα (Su böreği), εκλεκτό βούτυρο, χειροποίητο λευκό τυρί"},
    {"name": "Τραγανή πίτα βουτύρου", "description": "Χειροποίητα τραγανά φύλλα, εκλεκτό βούτυρο. Παραδοσιακά σερβίρεται με άχνη ζάχαρη."}
  ]},
  {"title": "Ποτά", "items": [
    {"name": "Κόλα", "description": ""},
    {"name": "Τούρκικη γκαζόζα", "description": "Κλασική/Πορτοκάλι"},
    {"name": "Χυμός φρούτων", "description": "Ροδάκινο/Βύσσινο/Ανάμεικτος"},
    {"name": "Κρύο τσάι", "description": "Λεμόνι/Ροδάκινο"},
    {"name": "Αϊράνι", "description": ""},
    {"name": "Ανθρακούχο νερό", "description": ""},
    {"name": "Νερό", "description": ""},
    {"name": "Αυθεντικό τσάι", "description": ""},
    {"name": "Χειροποίητη λεμονάδα", "description": ""},
    {"name": "Τούρκικος καφές", "description": ""}
  ]}
]

ro_sections = [
  {"title": "Recomandarea Bucătarului", "items": [{"name": "Pide de la Marea Neagră în formă de ghindă", "description": "Aluat subțire crocant, kavurma autentică de Rize, unt, formă de ghindă, recomandarea bucătarului"}]},
  {"title": "Pide de la Marea Neagră", "items": [
    {"name": "Pide cu carne tocată", "description": "Amestec special de carne tocată în stil Hünkar (Ou extra 10 TL)"},
    {"name": "Carne tocată și legume", "description": "Amestec special de carne tocată în stil Hünkar, roșii proaspete, ardei verde crocant (Ou extra 10 TL)"},
    {"name": "Carne tocată și cașcaval artizanal", "description": "Amestec special de carne tocată în stil Hünkar, cașcaval artizanal topit (Ou extra 10 TL)"},
    {"name": "Pide mixt suprem", "description": "Amestec special de carne tocată în stil Hünkar, cașcaval topit, roșii proaspete, ardei verde crocant (Ou extra 10 TL)"},
    {"name": "Pide cu vită la cuptor", "description": "Vită de Rize premium gătită lent (Kavurma) (Ou extra 10 TL)"},
    {"name": "Vită la cuptor și cașcaval", "description": "Vită de Rize premium gătită lent (Kavurma), cașcaval artizanal topit (Ou extra 10 TL)"},
    {"name": "Vită la cuptor și legume", "description": "Vită de Rize premium gătită lent (Kavurma), roșii proaspete, ardei verde crocant (Ou extra 10 TL)"},
    {"name": "Mix de vită, legume și cașcaval", "description": "Vită de Rize premium gătită lent (Kavurma), cașcaval topit, roșii proaspete, ardei verde crocant (Ou extra 10 TL)"},
    {"name": "Pide cu cașcaval artizanal topit", "description": "Cașcaval artizanal premium topit (Ou extra 10 TL)"},
    {"name": "Cașcaval și ou proaspăt de țară", "description": "Cașcaval artizanal topit, ou proaspăt de țară (Ou extra 10 TL)"},
    {"name": "Cașcaval topit și legume", "description": "Cașcaval artizanal topit, roșii proaspete, ardei verde crocant (Ou extra 10 TL)"},
    {"name": "Cârnați de vită condimentați și cașcaval", "description": "Cârnați de vită turcești condimentați (Sucuk), cașcaval artizanal topit (Ou extra 10 TL)"}
  ]},
  {"title": "Pide & Börek", "items": [
    {"name": "Pide Kır tradițional", "description": "Aluat artizanal moale cu carne tocată condimentată, brânză sau cartofi"},
    {"name": "Plăcintă rulată (Kol böreği)", "description": "Foi crocante rulate manual cu carne tocată, brânză artizanală, cartofi, spanac sau tahini"},
    {"name": "Plăcintă cu straturi în stil otoman", "description": "Foi de plăcintă fierte, lucrate manual (Su böreği), unt premium, brânză albă artizanală"},
    {"name": "Plăcintă crocantă cu unt", "description": "Foi crocante lucrate manual, unt premium. Servită tradițional cu zahăr pudră."}
  ]},
  {"title": "Băuturi", "items": [
    {"name": "Cola", "description": ""},
    {"name": "Suc acidulat turcesc", "description": "Clasic/Portocale"},
    {"name": "Suc de fructe", "description": "Piersici/Vișine/Mix"},
    {"name": "Ceai rece", "description": "Lămâie/Piersici"},
    {"name": "Ayran", "description": ""},
    {"name": "Apă minerală", "description": ""},
    {"name": "Apă", "description": ""},
    {"name": "Ceai autentic", "description": ""},
    {"name": "Limonadă de casă", "description": ""},
    {"name": "Cafea turcească", "description": ""}
  ]}
]

az_sections = [
  {"title": "Şefin Tövsiyəsi", "items": [{"name": "Palıd formalı Qaradəniz pidesi", "description": "İncə xırtıldayan xəmir, həqiqi Rize qovurması, kərə yağı, palıd forması, şefin tövsiyəsi"}]},
  {"title": "Qaradəniz pidesi", "items": [
    {"name": "Qiyməli pide", "description": "Xüsusi 'Hünkar-üsulu' qiyməli içlik (Əlavə yumurta 10 TL)"},
    {"name": "Qiyməli və tərəvəzli", "description": "Xüsusi 'Hünkar-üsulu' qiyməli içlik, təzə pomidor, xırtıldayan yaşıl bibər (Əlavə yumurta 10 TL)"},
    {"name": "Qiyməli və artisan pendiri", "description": "Xüsusi 'Hünkar-üsulu' qiyməli içlik, ərinmiş artisan Kaşar pendiri (Əlavə yumurta 10 TL)"},
    {"name": "Vrhunski qarışıq pide", "description": "Xüsusi 'Hünkar-üsulu' qiyməli içlik, ərinmiş Kaşar pendiri, təzə pomidor, xırtıldayan yaşıl bibər (Əlavə yumurta 10 TL)"},
    {"name": "Qovurmalı pide", "description": "Xüsusi Rize qovurması (yavaş bişirilmiş mal əti) (Əlavə yumurta 10 TL)"},
    {"name": "Qovurmalı və artisan pendiri", "description": "Xüsusi Rize qovurması, ərinmiş artisan Kaşar pendiri (Əlavə yumurta 10 TL)"},
    {"name": "Qovurmalı və tərəvəzli", "description": "Xüsusi Rize qovurması, təzə pomidor, xırtıldayan yaşıl bibər (Əlavə yumurta 10 TL)"},
    {"name": "Qarışıq qovurmalı və tərəvəzli", "description": "Xüsusi Rize qovurması, ərinmiş Kaşar pendiri, təzə pomidor, xırtıldayan yaşıl bibər (Əlavə yumurta 10 TL)"},
    {"name": "Ərinmiş artisan pendirli pide", "description": "Ərinmiş yüksək keyfiyyətli artisan Kaşar pendiri (Əlavə yumurta 10 TL)"},
    {"name": "Pendir və təzə kənd yumurtası", "description": "Ərinmiş artisan Kaşar pendiri, təzə kənd yumurtası (Əlavə yumurta 10 TL)"},
    {"name": "Ərinmiş pendir və tərəvəz", "description": "Ərinmiş artisan Kaşar pendiri, təzə pomidor, xırtıldayan yaşıl bibər (Əlavə yumurta 10 TL)"},
    {"name": "Ədviyyatlı mal əti kolbasası və pendir", "description": "Ədviyyatlı türk mal əti kolbasası (Sucuk), ərinmiş artisan Kaşar pendiri (Əlavə yumurta 10 TL)"}
  ]},
  {"title": "Pide və Börək", "items": [
    {"name": "Ənənəvi Kır pidesi", "description": "Mövsümi qiyməli ət, pendir və ya kartof seçimi ilə yumşaq artisan xəmiri"},
    {"name": "Bükmə börək (Kol böreği)", "description": "Qiyməli ət, artisan pendiri, kartof, ispanaq və ya tahinli əl ilə açılmış xırtıldayan qat-qat xəmir"},
    {"name": "Osmanlı üslublu qat-qat börək", "description": "Əl ilə açılmış qaynadılmış xəmir qatları (Su böreği), yüksək keyfiyyətli kərə yağı, artisan ağ pendir"},
    {"name": "Kərə yağlı xırtıldayan börək", "description": "Əl ilə açılmış xırtıldayan xəmir qatları, yüksək keyfiyyətli kərə yağı. Ənənəvi olaraq üzərinə bol şəkər pudrası səpilərək yeyilir."}
  ]},
  {"title": "İçkilər", "items": [
    {"name": "Kola", "description": ""},
    {"name": "Türk qazlı suyu", "description": "Klassik/Portağal"},
    {"name": "Meyvə şirəsi", "description": "Şaftalı/Vişnə/Qarışıq"},
    {"name": "Soyuq çay", "description": "Limon/Şaftalı"},
    {"name": "Ayran", "description": ""},
    {"name": "Mineral su", "description": ""},
    {"name": "Su", "description": ""},
    {"name": "Həqiqi çay", "description": ""},
    {"name": "Ev yapımı limonad", "description": ""},
    {"name": "Türk qəhvəsi", "description": ""}
  ]}
]

# We must get TR sections dynamically from the original file 

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

# New languages
new_langs = {
    'bs': bs_sections,
    'sq': sq_sections,
    'de': de_sections,
    'bg': bg_sections,
    'el': el_sections,
    'ro': ro_sections,
    'az': az_sections
}

for l_code, l_sections in new_langs.items():
    if l_code not in merged_data:
        merged_data[l_code] = {"restaurantName": "Hünkar Pide Börek", "sections": []}
    merged_data[l_code]['sections'] = populate_prices(l_sections)

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
