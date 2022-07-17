from flask import Flask, request
import pika

app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

@app.route('/')
def greeting():
    return 'Running.'


@app.route('/add', methods = ['POST'])
def process():
    if request.method == 'POST':
        data = request.json
        channel = connection.channel()
        channel.queue_declare(queue='q1')
        channel.basic_publish(exchange='', routing_key='q1', body=str(data))
        return data


if __name__ == '__main__':
    app.run(debug = True)
