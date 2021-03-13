from flask import Flask, render_template, current_app as app
app = Flask(__name__)

@app.route('/')
def index():
    return' Tell me what is you favorite food or desert '
@app.route('/food')
def food():
    return  render_template('Website.html')
@app.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')