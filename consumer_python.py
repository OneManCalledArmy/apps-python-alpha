import pika, sys, os
import redis

redis_client = redis.Redis(host='127.0.0.1', port=6379)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='q1')
    
    idx = 0
    
    def callback(ch, method, properties, body):
        nonlocal idx
        
        redis_client.set(idx, body.decode())
        redis_client.expire(idx, 60)
        idx += 1
    
    channel.basic_consume(queue='q1', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)