from api import flask_app_instance

if __name__ == '__main__':
    flask_app_instance.run(host='0.0.0.0', debug=True, port=5007, use_reloader=True)