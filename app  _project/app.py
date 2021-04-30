from flask import Flask, render_template, request, current_app as app
from flask_apscheduler import APScheduler
from sense_emu import SenseHat
import sqlite3

sense = SenseHat()
sense.show_message("Enter your reminder")

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def show_reminder():
  return render_template('app.html')


@app.route('/accomplished', methods=['GET', 'POST'])
def accomplished():
    response = request.form['response']
    response2 = request.form['response2']
    conn = sqlite3.connect('./static/data/appTasks.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks (reminder, date) VALUES(?,?)",(response, response2))
    conn.commit()

    conn.close()
    
    print (response2)  
    sense.show_message(response2) 
     
    return render_template('accomplished.html', response=response, response2=response2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
