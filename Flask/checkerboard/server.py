from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<int:number>')
def number(number):
    return render_template('number.html', number = number)

@app.route('/4')
def four():
    return render_template("four.html")


if __name__=="__main__":
        app.run(debug=True)