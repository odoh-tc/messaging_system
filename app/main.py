from fastapi import FastAPI, Query
from datetime import datetime
import logging
from .tasks import send_email

app = FastAPI()

logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)
logging.info("Manual logging test")

@app.get("/")
async def root(sendmail: str = Query(None), talktome: bool = Query(False)):
    if sendmail:
        send_email.delay(sendmail)
        return {"message": f"Email task queued for {sendmail}"}
    
    if talktome is not False:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Current time logged: {current_time}")
        return {"message": "Current time logged"}
    
    return {"message": "Request processed, but no action was taken"}