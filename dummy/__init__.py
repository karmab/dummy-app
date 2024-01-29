import functools
from dummy.bottle import Bottle, request, static_file, jinja2_view, response
import os


class Kdummy():

    def __init__(self):
        self.port = os.environ.get('DUMMY_PORT', 7000)
        self.url = os.environ.get('DUMMY_URL', 'http://127.0.0.1:7000/message')
        app = Bottle()
        basedir = os.path.dirname(Bottle.run.__code__.co_filename)
        view = functools.partial(jinja2_view, template_lookup=[f"{basedir}/templates"])

        @app.hook('after_request')
        def enable_cors():
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
            headers = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers['Access-Control-Allow-Headers'] = headers

        @app.route('/', method='OPTIONS')
        @app.route('/message', method='OPTIONS')
        def handle_options():
            return {}

        @app.route('/static/<filename:path>')
        def server_static(filename):
            return static_file(filename, root=f'{basedir}/static')

        @app.route('/')
        @view('index.html', method='GET')
        def index():
            return {'url': self.url}

        @app.route("/message", method='POST')
        def process_message():
            data = request.json
            return data

        self.app = app

    def run(self):
        self.app.run(host='0.0.0.0', port=self.port, debug=True)
