from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['WTF_CSRF_SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps - Daniel Nantes"

if __name__ == '__main__':
    app.run()