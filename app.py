from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    #A = form[]
    #n = form[]
    #i = form []
    #D = (((1+i)^n)-1) / (i(1+i)^n)
    #P = round(A/D, 2)

    return 'Your loan payment is'

if __name__ == '__main__':
    app.run(debug=True)
