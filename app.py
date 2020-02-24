from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        A = request.form["amt"]
        n = request.form["payments"]
        i = request.form["intrate"]
        D = (((1+i)^n)-1) / (i(1+i)^n)
        P = round(A/D, 2)
        return 'Your loan payment is ' + P

if __name__ == '__main__':
    app.run(debug=True)
