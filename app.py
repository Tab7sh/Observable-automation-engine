from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'<h1>Muhammad Tabish Musheer</h1><p>Visitor Count: {count}</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)