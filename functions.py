#celery -A functions worker --loglevel=info
#celery -A functions worker --loglevel=debug
from config import celery_app

@celery_app.task()
def fun(name):
    print("helloworld :",name)


#task = celery_app.send_task('functions.fun')