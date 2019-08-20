from celery import Celery

app = Celery('tasks',broker='redis://127.0.0.1:6379/0',backend='redis://localhost:6379/0')

@app.task
def add(x,y):
	return x/y
