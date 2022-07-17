from flask import Flask
import redis


redis_client = redis.Redis(host='127.0.0.1', port=6379)

app = Flask(__name__)


@app.route('/size')
def get_size():
    return f"{redis_client.dbsize()}"


if __name__ == '__main__':
    app.run(debug = True, port=5001)