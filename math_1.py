from chatterbot import ChatBot

bot= ChatBot("Math",logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("----------Math Chat Bot----------")
while True:
    user_text=input("Type the math equation that you4    want to solve:")
    print("ChatBot: "+str(bot.get_response(user_text)))
