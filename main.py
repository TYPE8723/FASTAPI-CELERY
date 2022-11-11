from fastapi import FastAPI, BackgroundTasks
from config import celery_app

app = FastAPI()

@app.get("/")
async def root():
    #task = fun.apply_async(queue='low_priority')
    task = celery_app.send_task('functions.fun', args=['alen'])
    print("currently added task",task)
    return {"message": "Word received"}

    