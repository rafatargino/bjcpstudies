# criando um site seguindo esse tutorial
#https://pages.hashtagtreinamentos.com/serie-criacaosites-flask-python?blog=1n4033rer&video=3dep762tr

#depois ler isso aqui
#https://medium.com/@moraneus/python-flask-a-comprehensive-guide-from-basic-to-advanced-fbc6ec9aa5f7

from flask import Flask, render_template

app = Flask(__name__)

# criar páginas do site
# toda página sempre tem um "route" e uma "função"
# route é o caminho que vai aparcer depois do /
# função é o que você quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/user/<username>")
def users(username):
    return render_template("user.html", username=username)
 
 

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #modo debug vai dando auto deploy
    #app.run()