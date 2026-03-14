from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask,render_template, request

app=Flask(__name__)
bot=ChatBot("chatbot",read_only=False,
            logic_adapters=[
                {
                    "import_path":"chatterbot.logic.BestMatch",
                    "default_response":"sorry i dont have answer",
                    "maximum_similarity_threshold":0.9 
                }
                ])
trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
# trainer=ListTrainer(bot)
# trainer.train([
#     "hi",
#     "hello",
#     "how are you?",
#     "i am fine, thank you",
#     "what is your name?",
#     "my name is chatbot",
#     "what can you do?",
#     "i can chat with you and answer your questions",
#     "bye",
#     "goodbye"
# ])
@app.route("/")
def main():
    return render_template("index.html")

# while True:
#     user_response=input("User: ")
#     print("ChatBot:"+str(bot.get_response(user_response)))

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))

if __name__=="__main__":
    app.run(debug=True)