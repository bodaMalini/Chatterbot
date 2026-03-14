from chatterbot import ChatBot


bot=ChatBot("Units",logic_adapters=['chatterbot.logic.UnitConversion'])

while True:
    user_text1=input("ask a question about unit conversion:")
    print("ChatBot: "+str(bot.get_response(user_text1)))