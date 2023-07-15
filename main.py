import telebot
import random
from telebot import types
bot = telebot.TeleBot('5846438225:AAEdnUlr7clXH6bIzkkNEnHkEPkDNOVWGDE')
a = 0
b = []

joke = ["Ապարացին ընկնում է փոսը և չի կարողանում դուրս գալ հետո ասում է-Էս վերջին անգամն եմ փորձում ստացվեց ստացվեց, չստացվեց կգնամ տուն:",
       'Մայիսի 9–ը որոշ երկրներ տոնում են «կարևորը մասնակցությունն է, ոչ թե հաղթանակը» կարգախոսով։',
       'Ուսուցիչը հարցնում է աշակերտին:-Բանջարաբոստանային կուլտուրաների մեջ ինչե՞ր են մտնում:-Որ չափառապատած չլինի էշ էլ կմտնի',
       'Ապարանցուն ասում են` մի հատ սառը զենքի անուն տուր, ասում ա` ձնագնդիկ:',
       'Ապարանցու տունը վառվում ա, ասում աˋ մեկա բանալին մոտսա',
       'Ապարանցին աղջկան ամուսնացնում է, խնամիներին փող է տալիս, որ մոտիկ տեղ ընկնի:',
       'Ապարանցին ուզում է ձեռի հետ գործ բռնի, ձեռը չի համաձայնում:',
       'Ապարանցին ընկնում է գետը, ասում է. «Դե քշի տուն»:',
       'Ապարանցին լսում է, որ դոլարի կուրսը իջնում է, ծաղկեփունջ է վերցնում և գնում է օդանավակայան դիմավորելու:'
]

@bot.message_handler(commands=['start'])
def start(message):
    global b
    b.append(message.id)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Կատակներ')
    btn2 = types.KeyboardButton('Ջնջել նամակները')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Բարև այս բոթը քեզ կատակներ կուղարկի',reply_markup=markup)
    b.append(message.id)
    bot.register_next_step_handler(message,jokee)



@bot.message_handler(content_types=['text'])
def jokee(message):
    global a,b
    b.append(message.id)
    if message.text == 'Կատակներ':
        a = random.randint(0, len(joke))
        bot.send_message(message.chat.id, joke[a])
        b.append(message.id)
    elif message.text  == 'Ջնջել նամակները':

        for i in range(len(b)):
            bot.delete_message(message.chat.id,message.message_id-i)
            b.pop()

bot.polling()