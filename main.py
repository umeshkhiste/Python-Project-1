from flask import Flask, render_template

app=Flask(__name__)

@app.route('/login')
def login():
    return render_template('/login.html')
    

@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/register')
def register():
    return render_template('/register.html')


@app.route('/deposit')
def deposit():
    return render_template('/deposit.html')


@app.route('/loan')
def loan():
    return render_template('/loan.html')


@app.route('/about')
def about():
    return render_template('/about.html')


@app.route('/contact')
def contact():
    return render_template('/contact.html')


@app.route('/services')
def services():
    return render_template('/services.html')


if __name__ == '__main__':
    app.run(debug=True)
