from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/pro/<int:idk>")    
def product_page(idk):
        return render_template('index.html',id=idk)    
if __name__ =="__main__":
        app.run(port=5000)    