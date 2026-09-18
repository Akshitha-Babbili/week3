from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    year = request.form['year']
    return render_template('success.html',
                           name=name, email=email, year=year)

app.run(debug=True)