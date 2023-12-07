from flask import Flask
import emojis

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask"


@app.route('/tortuga')
def tortuga():
    return f"<h1>{emojis.encode(':turtle:')}</h1>"




if __name__ == '__main__':
    app.run()
