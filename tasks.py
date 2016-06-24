from celery import Celery

app = Celery('tasks', broker='mongodb://localhost:9001/celeryDemo')

@app.task
def add(x, y):
    return x + y


