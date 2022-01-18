from flask import Flask
from flask_wtf.csrf import csrf

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps - Daniel Nantes"

if __name__ == '__main__':
    app.run()