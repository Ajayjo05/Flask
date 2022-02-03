from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    # print()
    return render_template('index.html')
@app.route('/Contact')
def contact():
    return 'Contact me'

@app.route('/Aboutus')
def About_US():
    return "We are a brand since 1993"

if __name__ == '__main__':
    app.run()
