from celery import Celery, shared_task
from celery_once import QueueOnce

backend = "redis://192.168.223.127:6379"
broker = "redis://192.168.223.127:6379/0"

# app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')
# app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')
# app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app = Celery('tasks', backend=backend, broker=broker)
app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': broker,
        'default_timeout': 60 * 60
    }
}


@app.task
def add(x, y):
    return x + y


# @shared_task
@app.task(base=QueueOnce, once={'graceful': True, 'timeout': 5, 'keys': ['x']})
def minus(x, y):
    print(f"x: {x}, y: {y}")
    return x - y
    # return "minus"


if __name__ == '__main__':
    # result = add.delay(4, 4)
    # print(result.ready())
    # print(result.get())
    # print(result.ready())

    # result = minus.delay(5, 2)
    result = minus.apply_async((5, 4))
    print(result.ready())
    print(result.get())
    print(result.ready())
