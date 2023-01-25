from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return 'success'

@app.route('/hello/<banana>')
def hello(banana):
    return f"hello {banana}"




if __name__=="__main__":
        app.run(debug=True)