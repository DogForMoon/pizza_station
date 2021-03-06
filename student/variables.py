from telebot.async_telebot import AsyncTeleBot


TOKEN = "TOKEN"
bot = AsyncTeleBot(TOKEN)
pizza_id = list()
"""
pizza = [("Маргарита", "mar543"),
         ("Пепперони", "pep054"),
         ("Пицца четыре сыра", "fch345")]
"""

pizza_cat = {"nut": [("Смесь орехи и фрукты Здравушка 50г", "mnf457"),
                       ("Смесь орехи, ягоды и фрукты Здравушка 50г", "nbf138")],

             "pur": [("Пюре TM ФрутоKids 90г", "pfk711"),
                      ('Пюре "ФрутоНяня" яблочное 90гр', "pfn699"),
                      ('Пюре "ФрутоНяня" груша 90гр', "pfn636"),
                      ('Пюре "ФрутоНяня" яблочное 90гр', "pfn846")],

             "wat": [('Вода питьевая без газа "Черноголовская" для детей 500мл"', "wch127"),
                      ('Вода питьевая без газа "Акваника" для детей 500мл"', "wak913")],

             "fal": [('Морс "МунБерри" 500мл', "fdm172"),
                                ('Лимонад "Свежесть"', "cum901")],

             "coc": [('Коктель молочный ФРУТОKIDS 200мл', "cmf803"),
                         ('Коктель со злаками "Easy Смузи" яблоко 250мл', "ces526"),
                         ('Коктель со злаками "Easy Смузи" манго 250мл', "ces579")],

             "jui": [('Сок "Мой" 200 мл', "jmy335"),
                      ('Сок "Дары Кубани" 200мл', "jdk148"),
                      ('Сок "Фрукт - Драйв" яблочный 200мл', "jfd863"),
                      ('Сок "Фрукт - Драйв" яблочно-грушевый 200мл', "jfd989"),
                      ('Сок "Фрукт - Драйв" яблочно-персиковый 200мл', "jfd955"),
                      ('Сок "Добрый" яблоко 200мл', "jga612"),
                      ('Сок "Добрый" мультифрукт 200мл', "jgm848"),
                      ('Сок "Добрый" апельсин 200мл', "jgo816"),
                      ('Сок "Добрый" яблоко-персик 200мл', "jgp141")],

             "bar": [('Злаковый батончик "Литра" с вишней, семенами тыквы и черносливом', "cbl380"),
                           ('Злаковый батончик "Физкульт" с кокосом, ананасом, курагой и изюмом', "cbf554"),
                           ('Злаковый батончик "Матан" с клюквой, семенами льна и тыквой', "cbm206"),
                           ('Гематоген молочный 20гр', "hem126"),
                           ('Батончик злаковый "EGO KIDS" сливочный пломбир 25гр', "bek529"),
                           ('Батончик злаковый "EGO KIDS" citrus lemonade 25гр', "bek778"),
                           ('Батончик злаковый "EGO KIDS" клубничный десерт 25гр', "bek354"),
                           ('Финиковый батончик 40гр', "dab998")],

             "muf": [('Пшеничные палочки с мёдом "Лопе Лопе" 12гр', "wsh187"),
                       ('Рисовые палочки с мёдом "Лопе Лопе" 12гр', "rsh108"),
                       ('Мини хлебцы "Спелый банан" рисовые 30гр', "mlb730"),
                       ('Мини хлебцы "Сочное яблоко" рисовые 30гр', "mla654"),
                       ('Печенье сдобное "Полезный завтрак" 32гр', "bcb134")],

             "mar": [('Мармелад с соком "DOFF" 50гр', "mwj237"),
                          ('Мармелад с соком "Натуральный продукт" чёрная смородина 45гр', "mnp876"),
                          ('Мармелад с соком "Натуральный продукт" Вишня 45гр', "mnp513"),
                          ('Мармелад с соком "Натуральный продукт" клюква 45гр', "mnp399"),
                          ('Мармелад с соком "Харибо" 70гр', "mjh290"),
                          ('Мармелад с соком "Фрутелла" 70гр', "mjf851")],

             "pas": [('Пастилки фруктовые "Кидс" "Вишнёвая лента" 25гр', "pfk714"),
                         ('Пастилки фруктовые "Кидс" "Сливовая лента" 25гр', "pfk728"),
                         ('Пастилки фруктовые "Кидс" "Яблочная лента" 25гр', "pfk663")],

             "san": [('Сэндвич с колбасой и овощами', "ssv429"),
                         ('Сэндвич с ветчиной и сыром', "shc674")],

             "bak": [('Пицца "Школьная" с колбасой 100гр', "pss714"),
                         ('Сосиска в тесте 100гр', "sid580"),
                         ('Слойка с вишней 90гр', "chp233"),
                         ('Плюшка эстонская с сыром 75гр', "eiv639")],

             "fru": [('Апельсин', "orange"),
                        ('Яблоко', "app552")]}
 
pizza_association = {"nut": "орехи",
                     "pur": "пюре",
                     "wat": "вода",
                     "fal": "морс и лимонад",
                     "coc": "коктели",
                     "jui": "соки",
                     "bar": "батончики",
                     "muf": "сдоба",
                     "mar": "мармелад",
                     "pas": "пастила",
                     "san": "сэндвичи",
                     "bak": "выпечка",
                     "fru": "фрукты"}

pizza_ids = {"mnf457", "nbf138",
             "pfk711", "pfn699",
             "pfn636", "pfn846",
             "wch127", "wak913",
             "fdm172", "cum901",
             "cmf803", "ces526",
             "ces579", "jmy335",
             "jdk148", "jfd863",
             "jfd989", "jfd955",
             "jga612", "jgm848",
             "jgo816", "jgp141",
             "cbl380", "cbf554",
             "cbm206", "hem126",
             "bek529", "bek778",
             "bek354", "dab998",
             "wsh187", "rsh108",
             "mlb730", "mla654",
             "bcb134", "mwj237",
             "mnp876", "mnp513",
             "mnp399", "mjh290",
             "mjf851", "pfk714",
             "pfk728", "pfk663",
             "ssv429", "shc674",
             "pss714", "sid580",
             "chp233", "eiv639",
             "orange", "app552"}

pizza_in_progress = {}
sticker = "CAACAgIAAxkBAAEDptlh2y0YYtVROH-2OuGj\
-AETTs77hgACMQADTGrIFxOa-QgbeyCZIwQ"
