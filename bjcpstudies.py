# criando um site seguindo esse tutorial
#https://pages.hashtagtreinamentos.com/serie-criacaosites-flask-python?blog=1n4033rer&video=3dep762tr

from flask import Flask

app = Flask(__name__)

# criar páginas do site
# toda página sempre tem um "route" e uma "função"
# route é o caminho que vai aparcer depois do /
# função é o que você quer exibir naquela página

@app.route("/")
def homepage():
    return "Hello, world!"

@app.route("/")
def homepage():
    return "Hello, world!"


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #modo debug vai dando auto deploy
    #app.run()