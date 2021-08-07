from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'very secret key'

gold_choice = ['(earns 10-20 golds)', '(earns 5-10 golds)', '(earns 2-5 golds)', '(earns/takes 0-50 golds)']



def appendActivities(gold, choice):
    session['gold'] += gold
    session['activities'].append(f'<p>Earned {gold} golds from the {choice}! ({datetime.now()})</p>')

#routes
@app.route('/')
def home_page():
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []

    if 'buildings' not in session:
        session['buildings'] = ['Farm', 'Cave', 'House', 'Casino']

    if 'gold_choice' not in session:
        session['gold_choice'] = ['(earns 10-20 golds)', '(earns 5-10 golds)', '(earns 2-5 golds)', '(earns/takes 0-50 golds)']

    return render_template('index.html')

@app.route('/process', methods = ['post'])
def process():
    gold_dictionary = {
    'Farm': random.randint(10,20),
    'Cave': random.randint(5,10),
    'House': random.randint(2,5),
    'Casino': random.randint(-50,50)
    }
    choice = request.form['choice']
    session['color'] = 'green'
    gold = gold_dictionary[choice]

    if gold < 0:
        session['gold'] += gold 
        session['activities'].append(f'<p style="color: red">Lost {gold} golds from the {choice}! OOOOPS ({datetime.now()})</p>')
    else:
        appendActivities(gold,choice)

    print(request.form['choice'])

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)