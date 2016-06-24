import os
from celery import Celery

BROKER_URI = os.environ.get("BROKER_URI", "mongodb://localhost:9000/celeryDemo")

app = Celery('tasks', broker=BROKER_URI)

@app.task
def add(x, y):
    return x + y


