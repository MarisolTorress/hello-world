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

@app.route('/buttonPressed/<btn>')
def press(btn):
  print('button ' + str(btn) + 'was pushed')
  return render_template('accomplished.html')

@app.route('/tasks')
def tasks():
  conn = sqlite3.connect('./static/data/appTasks.db')
  curs = conn.cursor()
  tasks = []
  rows = curs.execute("SELECT * from tasks")
  for row in rows:
    message = {'reminder': row[0], 'date': row[1], 'rowid': row[2]}
    print (message)  
    tasks.append(message)
    sense.show_message(message) 
  conn.close()
  return render_template('app.html', reminder=reminder, date=date, accomplished=tasks)



@app.route('/accomplished', methods=['GET', 'POST'])
def accomplished():
    response = request.form['response']
    response2 = request.form['response2']
    print(response)
    print(response2)
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
