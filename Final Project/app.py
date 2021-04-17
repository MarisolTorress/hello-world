from flask import Flask, render_template, request, current_app as app
from sense_emu import SenseHat
import sqlite3

sense = SenseHat()
sense.show_message("Enter a Response")

app = Flask(__name__)

@app.route('/')
def website():
    return  render_template('Website.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    response = request.form['response']
    response2 = request.form['response2']
     
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages (message1, message2) VALUES(?,?)",(response, response2))
    conn.commit()

    conn.close()
    
    print (response2)  
    sense.show_message(response2) 
    return render_template('success.html', response=response, response2=response2)

    @app.route('/all')
    def all():
        conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
       messgae = {'message2' : row[0], 'message2':row[1]}
       message.append(message)
       conn.close()
       return render_template('all.html', messages = messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
