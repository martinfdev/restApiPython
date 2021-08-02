from flask import Flask, Request
from controllers.Home.HomeController import HomeController

app = Flask(__name__)

@app.route('/')
def index():
    home = HomeController(Request)
    return home.index()

if __name__ == "__main__":
    app.run(host="localhost", port=3000,  debug=True)