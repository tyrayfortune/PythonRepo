from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print(request.form)
#     return redirect("/result")	 
    


@app.route('/result', methods=['post'])
def show_user():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session ['comment'] = request.form['comment']
    return render_template('user.html', name_on_template=session['username'])

if __name__=="__main__":
        app.run(debug=True)