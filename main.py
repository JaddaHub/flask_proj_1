from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
