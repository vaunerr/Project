from gc import callbacks

import telebot
from telebot import types
import emoji

bot = telebot.TeleBot("8085889161:AAFa-keP9B8D2l8j6GbAYYRb5yY0xjmiNFU")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/menu':
        obj = types.InlineKeyboardMarkup()
        bttn1 = types.InlineKeyboardButton('Начало',callback_data='start')
        bttn2 = types.InlineKeyboardButton('Базовые операции',callback_data='operations')
        bttn3 = types.InlineKeyboardButton('Переменные и типы данных', callback_data='data')
        bttn4 = types.InlineKeyboardButton('Условные операторы', callback_data='operators')
        bttn5 = types.InlineKeyboardButton('Циклы', callback_data='cycles')
        bttn6 = types.InlineKeyboardButton('Конец', callback_data='end')
        obj.row(bttn1)
        obj.row(bttn2,bttn3)
        obj.row(bttn4, bttn5,)
        obj.row(bttn6)
        bot.send_message(message.from_user.id, f"\U0001F44BПривет, @{message.from_user.first_name} !\n\n\U0001f9d1\u200D\U0001f3ebЯ,\
 @PythonNavigatorUser_Bot , помогу тебе изучить основы программирования на python\n\n\
\U00002757Чтобы начать, нажми на любую кропку, представленную ниже",reply_markup=obj)
    else:
        bot.send_message(message.from_user.id, "Чтобы начать, напиши команду /menu")

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    obj1 = types.InlineKeyboardMarkup()
    obj2 = types.InlineKeyboardMarkup()
    obj3 = types.InlineKeyboardMarkup()
    obj4 = types.InlineKeyboardMarkup()
    obj5 = types.InlineKeyboardMarkup()
    obj6 = types.InlineKeyboardMarkup()
    if callback.data == 'start':
        bttn11 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='start1')
        obj1.row(bttn11)
        bot.edit_message_text('\U0001F40DДля начала давайте разберёмся по порядку. Что же такое Python? Python\
 – это высокоуровневый язык программирования, который широко используется в разных областях. Он отличается своей легкостью в изучении и\
 универсальностью, благодаря чего многие начинающие программисты выбирают его в качестве первого для изучения языка. В этом чат-боте состоится наше знакомство с языком программирования Python.',callback.message.chat.id,callback.message.message_id,reply_markup=obj1)
    elif callback.data == 'operations':
        bttn11 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operations1')
        obj1.row(bttn11)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebИтак, перед тем как углубляться в более сложные конструкции, предлагаю для начала разобраться с самыми базовыми.\
 Первым делом давайте рассмотрим комментарии. Комментарии в коде используются для пояснения текста программы. Интерпретатором они игнорируются и предназначены исключительно для разработчиков.\
\nЧтобы создать комментарий нужно добавить символ решётки (#) перед участком кода, который мы хотим закомментировать.\
Если нужно закомментировать большой участок кода, то удобнее всего будет прописать три апострофа перед и после участка кода.\nПример:\
\n______________________\n#Комментарий\nprint("Hello World!")\nВывод: Hello World!\n______________________\n',callback.message.chat.id,callback.message.message_id,reply_markup=obj1)
    elif callback.data == 'data':
        bttn11 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='data1')
        obj1.row(bttn11)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebПеременные используются для хранения данных. Чтобы создать\
 переменную нужно придумать ей имя на латинском\
 (имя может состоять только из цифр, букв и символов подчеркивания)\
 и присвоить ей значение с помощью оператора =. \nПо сути, переменная является своего рода коробкой, в которую мы можем\
 складывать данные и потом их оттуда вытаскивать. Тип переменной указывать не обязательно, ведь он определяется автоматически.\
 Это делает язык более гибким и удобным для использования.',callback.message.chat.id,callback.message.message_id,reply_markup=obj1)
    elif callback.data == 'operators':
        bttn11 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operators1')
        obj1.row(bttn11)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebДля начала, что такое условные операторы? Условные операторы, они же ветвления, дают возможность исполнять\
 различные фрагменты кода в зависимости от того, истинны или ложны определенные условия.\
\nДля создания условия используют оператор if. После него следует само условие и двоеточие на конце. С новой строки с отступом начинается код.\nПример работы:\n_____________________________\nage = int(input())\nif age >= 18:\
\n  print("Вы совершеннолетний")\n_____________________________', callback.message.chat.id, callback.message.message_id,reply_markup=obj1)
    elif callback.data == 'cycles':
        bttn11 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='cycles1')
        obj1.row(bttn11)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebИногда программу нужно заставить повторять одно``` и то же действие несколько раз. Но как это сделать?\
 На помощь нам приходят циклы. В Python есть всего два цикла: for и while.\nЦикл for позволяет выполнять операцию установленное количество раз.\
 Структура цикла for выглядит следующим образом: for + перменная + in + функция range(количество повторений) + :.\
 С новой строки с отступом начинается код\n\U0001F6A9Важно! range(n) возвращает последовательность целых чисел от 0 до n, не включая n. Например: range(5) вернёт последовательность:\
0,1,2,3,4.\n\U000026AA Мы можем установить, с какого числа хотим начать. Например: range(1,5) вернёт последовательность целых чисел: 1,2,3,4.\
Также можно поменять шаг цикла, установив третий аргумент в функцию. Например: range(1,10,2) вернёт последовательность целых чисел: 1,3,5,7,9.',callback.message.chat.id,callback.message.message_id,reply_markup=obj1)
    elif callback.data == 'end':
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebСпасибо большое за прохождение бота!\n Надеюсь Вы получили новые знания и провели время с пользой! ',callback.message.chat.id,callback.message.message_id)


    if callback.data == 'start1':
        bttn21 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='start2')
        obj2.row(bttn21)
        bot.edit_message_text('\U0001F468\U0000200D\U0001F4BB Python, как и на других языках программирования, пишется в интегрированных средах разработки, или IDE(Integrated Development Environment).\
В них разработчики пишут, проверяют, тестируют и запускают код. Одной из такой среды разработки является IDLE(Integrated Development and Learning Environment), на которой мы будем писать.\
Она появляетя вместе с Python и подходит для новичков, однако Вы всегда можете поменять программу на ту, в которой Вам будет удобнее всего работать.',callback.message.chat.id,callback.message.message_id,reply_markup=obj2)
    elif callback.data == 'operations1':
        bttn21 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operations2')
        obj2.row(bttn21)
        bot.edit_message_text('Вы уже заметили, что в прошлом примере использовалась функция print(), предлагаю её рассмотреть.\
\nPrint() - встроенная функция в Python, с помощью которой можно вывести различную информацию в консоль или терминал. Для вызова функции следует использовать скобки, как и в любой другой функции.\
 Несколько значений прописываются через запятую. Важно! Строки всегда заключаются в кавычках. Если переменная или число заключены в кавычках, то они будут считаться за строку.\
\nЕсли Вы попробовали прописать несколько значений через запятую, то вы заметили, что между значениями присутствуют пробелы, то есть разделители. Чтобы их убрать или заменить, следует установить в конце свойство sep='' и указать внутри кавычек строку, которая будет разделять каждый элемент. Если оставить \
кавычки пустыми, то все значения будут выводиться без пробелов.\nПример:\n__________________________________\nprint("Hello World!",1,2,3,sep="")\nВывод: Hello World!123\n__________________________________',callback.message.chat.id,callback.message.message_id,reply_markup=obj2)
    elif callback.data == 'data1':
        bttn21 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='data2')
        obj2.row(bttn21)
        bot.edit_message_text('Раз уж мы упомянули типы данных, то следует уточнить, что это и с чем его едят.\nТипы данных — это \
 базовые категории, указывающие, какой вид информации может быть сохранён и обработан в программе. \nОсновные типы данных:\
 \nint: целые числа\nfloat: числа с плавающей точкой\nstr: строки\nbool: логические значения (True или False)\nlist: списки\ntuple: кортежи\ndict: словари\nset: множества\
 \nПеременные в Python могут изменять свой тип данных. Мы можем сначала присвоить ему одно значение, а затем изменить его на другое.',callback.message.chat.id,callback.message.message_id,reply_markup=obj2)
    elif callback.data == 'operators1':
        bttn21 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operators2')
        obj2.row(bttn21)
        bot.edit_message_text('\U000026AAКонструкция if-else даёт возможность выполнять два различных блока кода: для истинных и ложных условий.\
 Это позволяет управлять поведением программы в\
 зависимости от входных данных и состояний.\
\n\nif описывает, что делать программе, если условие истинно, а else — если это условие ложно.\
 После else нельзя указать другое условие: просто ставится двоеточие. Следующий блок кода начинается с отступа, как и в случае с if.',callback.message.chat.id,callback.message.message_id,reply_markup=obj2)
    elif callback.data == 'cycles1':
        bttn21 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='cycles2')
        obj2.row(bttn21)
        bot.edit_message_text('Цикл while позволяет ввыполнять операцию до тех пор, пока условие не будет выполнено.\
 Структура цикла while выглядит следующим образом:\nwhile + условие + :\nТак же, как и в случае с циклом for, с новой строки с отступом начинается код.',callback.message.chat.id,callback.message.message_id,reply_markup=obj2)



    if callback.data == 'start2':
        bot.edit_message_text('Чтобы запустить IDLE нужно зайти в меню Пуск и ввести название. При запуске первым делом вы увидете перед собой окно в интерактивном режиме. Всё, что вы пишете в нём будет сразу же выполнено. Интерактивный режим может быть полезен для\
 быстрого тестирования работоспособности кода, однако он не подходит для больших программ, из-за чего пользуются им довольно редко.\
 \nЧтобы открыть окно в режиме редактора следует создать новый файл или открыть старый. Для этого в главном меню выбираем File ---> New file или File ---> Open, после чего октроется окно редактора кода. Этот режим включает все возможности интерактивного режима',callback.message.chat.id,callback.message.message_id)
    if callback.data == 'operations2':
        bttn31 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operations3')
        obj3.row(bttn31)
        bot.edit_message_text('Теперь предлагаю рассмотреть операторы - специальные символы, которые выполняют операции над значениями и переменными.\
\nАрифметические операторы, как ни странно, используются для выполнения математических операций:\n__________________________________\nСложение: +\nВычитание: -\nУмножение: *\nДеление: /\nЦелочисленное деленое: //\nОстаток от деления: %\nВозведение в степень: **\n__________________________________',callback.message.chat.id,callback.message.message_id,reply_markup=obj3)
    if callback.data == 'data2':
        bttn61 = types.InlineKeyboardButton('\U0001f4ceСтрока', callback_data='true')
        bttn62 = types.InlineKeyboardButton('\U0001f4ceЦелое число', callback_data='false')
        bttn63 = types.InlineKeyboardButton('\U0001f4ceСловарь', callback_data='false')
        bttn64 = types.InlineKeyboardButton('\U0001f4ceСписок', callback_data='false')
        obj6.row(bttn62, bttn61)
        obj6.row(bttn63, bttn64)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebЧтобы закрепить полученные знания, давай попробуем ответить на вопрос: какому типу данных принадлежит переменная?\n\U00002757Выбери ответ из представленных ниже вариантов \
\n_____________\na = "4"\n_____________',callback.message.chat.id,callback.message.message_id,reply_markup=obj6)
    if callback.data == 'operators2':
        bttn31 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operators3')
        obj3.row(bttn31)
        bot.edit_message_text('\U000026AAКонструкция if-elif-else используется для проверки нескольких условий и выполнения только подходящего кода.\
 if — проверяет первое условие,elif (сокращение от else if) — проверяет следующие условия, если предыдущее условие ложно,\
а else — выполняет блок кода, если все предыдущие условия ложны.\nПример работы:',callback.message.chat.id,callback.message.message_id,reply_markup=obj3)
    if callback.data == 'cycles2':
        bttn61 = types.InlineKeyboardButton('\U0001f4ce11', callback_data='false')
        bttn62 = types.InlineKeyboardButton('\U0001f4ce9', callback_data='false')
        bttn63 = types.InlineKeyboardButton('\U0001f4ce10', callback_data='true')
        bttn64 = types.InlineKeyboardButton('\U0001f4cenum', callback_data='false')
        obj6.row(bttn62, bttn61)
        obj6.row(bttn63, bttn64)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebЧтобы закрепить полученные знания, давай попробуем ответить на вопрос: что будет выводить код?\n\U00002757Выбери ответ из представленных ниже вариантов \
\n_________________\nnum = 0\nfor i in range(10):\n num = num + 1\nprint(num)\n_________________',callback.message.chat.id,callback.message.message_id,reply_markup=obj6)
    if callback.data == 'end2':
        bttn31 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='end3')
        obj3.row(bttn31)
        bot.edit_message_text('Конец2',callback.message.chat.id,callback.message.message_id,reply_markup=obj3)

    if callback.data == 'operations3':
        bttn41 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operations4')
        obj4.row(bttn41)
        bot.edit_message_text('Операторы присваивания используются для присваивания значений перменным:\n__________________________________\
\nПрисваивание: =\nСложение с присваиванием: +=\nВычитание с присваиванием: +=\nУмножение с присваиванием: *=\nДеление с присваиванием: /=\nОстаток от деления с присваиванием: %=\nВозведение в степень с приваиванием: **=\n__________________________________', callback.message.chat.id, callback.message.message_id, reply_markup=obj4)

    if callback.data == 'operations4':
        bttn51 = types.InlineKeyboardButton('Дальше \U000027A1', callback_data='operations5')
        obj5.row(bttn51)
        bot.edit_message_text('Операторы сравнения позволяют сравнивить два значения/две переменных и возвращают True или False:\n__________________________________\nНе равно: !=\nБольше чем: >\nМеньше чем: <\nБольше или равно: >=\nМеньше или равно: <=\n__________________________________', callback.message.chat.id, callback.message.message_id, reply_markup=obj5)

    if callback.data == 'operators3':
        bttn61 = types.InlineKeyboardButton('\U0001f4ceВы можете переходить дорогу', callback_data='true')
        bttn62 = types.InlineKeyboardButton('\U0001f4ceПредупреждение о смене сигнала', callback_data='false')
        bttn63 = types.InlineKeyboardButton('\U0001f4ceПереходить дорогу запрещено', callback_data='false')
        bttn64 = types.InlineKeyboardButton('\U0001f4ceОшбика', callback_data='false')
        obj6.row(bttn62, bttn61)
        obj6.row(bttn63, bttn64)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebЧтобы закрепить полученные знания, давай попробуем ответить на вопрос: что выведет программа?\n\U00002757Выбери ответ из представленных ниже вариантов \
\n_____________________________________________\nlight = "Зелёный"\nif light == "Зелёный":\n    print("Вы можете переходить дорогу")\nelif light == "Жёлтый"\n  print("Предупрежение о смене сигнала"):\nelse\n   print("Переходить дорогу запрещено")\n_____________________________________________',callback.message.chat.id,callback.message.message_id,reply_markup=obj6)








    if callback.data == 'operations5':
        bttn61 = types.InlineKeyboardButton('\U0001f4ce2', callback_data='true')
        bttn62 = types.InlineKeyboardButton('\U0001f4ce2,14...', callback_data='false')
        bttn63 = types.InlineKeyboardButton('\U0001f4ce3', callback_data='false')
        bttn64 = types.InlineKeyboardButton('\U0001f4ceОшибка', callback_data='false')
        obj6.row(bttn62, bttn61)
        obj6.row(bttn63,bttn64)
        bot.edit_message_text('\U0001f9d1\u200D\U0001f3ebЧтобы закрепить полученные знания, давай попробуем ответить на вопрос: что выведет программа?\n\U00002757Выбери ответ из представленных ниже вариантов \
\n__________________\nprint(15//7)\n__________________', callback.message.chat.id, callback.message.message_id, reply_markup=obj6)



    if callback.data == 'true':
        bot.edit_message_text('\U00002705Правильно! \U0001F600\nВижу ты хорошо разобрался с темой, так держать!\nЕсли хочешь продолжить изучать другие темы, напиши команду /menu', callback.message.chat.id, callback.message.message_id,)
    elif callback.data == 'false':
        bot.edit_message_text('\U0000274CНеправильно. \U00002639\n Попробуй перейти в меню и выбрать тему заново, чтобы ознакомиться с ней получше. Для этого напиши команду /menu', callback.message.chat.id, callback.message.message_id,)







bot.infinity_polling(timeout=90, long_polling_timeout = 5)

