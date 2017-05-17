import random
import time

from flask import Flask, Response

app = Flask(__name__)

@app.route('/stream')
def stream():
    def generate():
        while True:
            items = random.randint(2, 10)
            for i in range(items):
                yield '{"item": "' + str(i) + '", "ms'
                time.sleep(random.random())
                yield 'g": "this is an item"}\n'
            time.sleep(3)

    return Response(generate(), content_type='application/json')

if __name__ == "__main__":
    app.run(host='localhost', port=8000)
