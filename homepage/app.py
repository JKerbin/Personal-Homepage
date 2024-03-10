from flask import Flask, render_template
from gevent import pywsgi

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wechat')
def wechat():
    return render_template('wechat.html')


@app.route('/qq')
def qq():
    return render_template('qq.html')


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 80), app)
    server.serve_forever()
