from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/red')
def red():
    name = 'Marisol'
    return render_template('rainbow_template.html', colors = "red")

@app.route('/blue')
def blue():
    name = 'Marisol'
    return render_template('rainbow_template.html', colors = "blue")

@app.route('/yellow')
def yellow():
    name = 'Marisol'
    return render_template('rainbow_template.html', colors = "yellow")

@app.route('/violet')
def violet():
    name = 'Marisol'
    return render_template('rainbow_template.html', colors = "violet")

@app.route('/indigo')
def indigo():
    name = 'Marisol'
    return render_template('rainbow_template.html', colors = "indigo")

@app.route('/orange')
def orange():
    name = 'Marisol'
    return render_template('rainbow_template.html', color = "orange")

    if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')