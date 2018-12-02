from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route('/')
def hello():
	redis.incr('hits')
	visits = redis.get('hits')
	return 'Hello Docker Book reader! I have been seen {0} times'.format(visits)


if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)