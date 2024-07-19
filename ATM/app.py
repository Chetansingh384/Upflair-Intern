# ATM logic
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
av_amount = 5000

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('task', name=name))
    return render_template('index.html')

@app.route('/task/<name>', methods=['GET', 'POST'])
def task(name):
    if request.method == 'POST':
        task = int(request.form['task'])
        if task == 1:
            return redirect(url_for('balance'))
        elif task == 2:
            return redirect(url_for('deposit'))
        elif task == 3:
            return redirect(url_for('withdraw'))
    return render_template('task.html', name=name)

@app.route('/balance')
def balance():
    global av_amount
    return render_template('balance.html', amount=av_amount)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    global av_amount
    if request.method == 'POST':
        dep_amount = int(request.form['dep_amount'])
        if dep_amount > 500:
            av_amount += dep_amount
            return redirect(url_for('balance'))
        else:
            return render_template('deposit.html', error="Please bring more amount.")
    return render_template('deposit.html', error=None)

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    global av_amount
    if request.method == 'POST':
        wid_amount = int(request.form['wid_amount'])
        if av_amount < wid_amount:
            return render_template('withdraw.html', error="You cannot withdraw, your balance is low.", amount=av_amount)
        else:
            av_amount -= wid_amount
            return redirect(url_for('balance'))
    return render_template('withdraw.html', error=None, amount=av_amount)

if __name__ == '__main__':
    app.run(debug=True)
