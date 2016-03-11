from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/list")
def list():
    books = ["book1", "book2", "book3"]
    return render_template("list.html", items=books)

@app.route("/index")
def index():
    return render_template("index.html") 
 
app.run()
