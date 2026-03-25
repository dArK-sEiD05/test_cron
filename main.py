from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from GAE"}


@app.get("/cron-task")
def cron_task():
    """Endpoint called by the cron job."""
    print("Cron job executed")
    return {"status": "success", "message": "Cron task completed"}
