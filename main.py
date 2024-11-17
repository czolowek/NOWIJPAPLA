from flask import Flask,render_template
import db

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    students = [
        {"name": "марко", "last_name":"аирович", "rost": 166},
        {"name": "игорь", "last_name": "амбасадор", "rost":177 },
        {"name": "макс", "last_name": "аркадий", "rost":107 }
   ] 
    return render_template("menu.html",students=students)

if __name__ == "__main__":
    app.run(debug=True, port=80)
