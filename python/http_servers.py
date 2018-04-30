from flask import Flask


app = Flask(__name__, static_folder='/Users/msyoun/', static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/echo/<thing>')
def echo(thing):
    return "Say Hello to my little friend: %s!" % thing


if __name__ == "__main__":
    app.run(port=9999, debug=True)