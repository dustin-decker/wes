import flask
from flask import render_template
import argparse
import os
import sys

wesDir = os.path.realpath(os.path.join(__file__, "..", ".."))
sys.path.append(wesDir)
from wes.api.v1 import api_v1

app = flask.Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

# Removing web interface until Indeed specific components are removed
# @app.route('/')
# def index():
#     """
#     The default route that renders the index.html with the datatable
#     :return: The index.html template
#     """
#     # render the data table page
#     return render_template('index.html')

def console():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', action='store',
                        help='The port to run the server on.',
                        default=5000)
    parser.add_argument('-i', '--host', action='store',
                        help='The interface to run the server on.',
                        default='127.0.0.1')
    args = parser.parse_args()

    """
    Runs the flask app
    """
    app.run(host=args.host, port=args.port)

if __name__ == '__main__':
    console()
