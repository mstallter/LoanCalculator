from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        A = float(form["amt"])
        n = float(form["payments"]) * 12
        i = float(form["intrate"]) / 12
        D = (((1+i)**n)-1)/(i*(1+i)**n)
        P = round(A/D, 2)
        final = 'Your loan payment is $' + str(P)
        return render_template('index.html', display=final, pageTitle='loanCalc')   
    return render_template('index.html', pageTitle='loanCalc' )
if __name__ == '__main__':
    app.run(debug=True)
