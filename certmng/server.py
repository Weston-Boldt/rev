import traceback
import uuid
import sys

import flask
import flask.json
import gevent.pywsgi

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'

@app.route('/domains/<string:domain>', methods=["POST"])
def add_domain(domain):
    # write domain to db
    return

@app.route('/domains/<string:domain>', methods=["GET"])
def get_domain(domain):
    return

if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    from . import db
    db.init_app(app)

    http_server.serve_forever()
