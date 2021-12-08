from celery import shared_task

from proj.celery import app

@app.task
def add(x, y):
    return x + y

@shared_task
def minus(x, y):
    return x - y


if __name__ == '__main__':
    result_add = add.delay(4, 4)
    print(result_add)

    result_minus = minus.delay_async([5, 2])
    print(result_minus)
