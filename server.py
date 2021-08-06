from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def home_page():
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods = ['post'])
def process():
    choice = request.form['choice']
    session['color'] = 'green'
    if choice == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        session['activities'].append(f'<p>Earned {gold} golds from the {choice}! ({datetime.now()})</p>')
    elif choice == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        session['activities'].append(f'<p>Earned {gold} golds from the {choice}! ({datetime.now()})</p>')
    elif choice == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        session['activities'].append(f'<p>Earned {gold} golds from the {choice}! ({datetime.now()})</p>')
    else:
        gold = random.randint(-50,50)
        session['gold'] += gold
        if gold < 0:
            session['activities'].append(f'<p style="color: red">Lost {gold} golds from the {choice}! OOOOPS ({datetime.now()})</p>')
        else:
            session['activities'].append(f'<p>Earned {gold} golds from the {choice}! ({datetime.now()})</p>')

    print(request.form['choice'])

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)