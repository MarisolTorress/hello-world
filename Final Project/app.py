from flask import Flask, render_template, request, current_app as app

app = Flask(__name__)

@app.route('/')
def website():
    return  render_template('Website.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    response = request.form['response']
    return render_template('success.html', response=response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')