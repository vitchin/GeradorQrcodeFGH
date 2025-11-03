from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html')

if __name__ == '__main__':
    app.run(debug=True)