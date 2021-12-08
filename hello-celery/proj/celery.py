import celery

app = celery('proj', include=['proj.tasks'])

app.config_from_object('proj.config')

if __name__ == '__main__':
    app.start()
