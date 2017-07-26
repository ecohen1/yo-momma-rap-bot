from flask import Flask, render_template, send_from_directory
import rap

def create_app(config=None, import_name=None):
    app = Flask(__name__, static_url_path='')
    rap.init()

    @app.route('/rap')
    def get_rap():
        rap_string = 'error'
        success = False
        num_tries = 0
        while not success and num_tries < 10:
            try:
                rap_string = rap.get_lines(4)
                success = True
            except:
                num_tries += 1
        return rap_string

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('templates/js', path)

    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('templates/css', path)

    @app.route('/fonts/<path:path>')
    def send_fonts(path):
        return send_from_directory('templates/fonts', path)

    @app.route('/img/<path:path>')
    def send_img(path):
        return send_from_directory('templates/img', path)

    return app
