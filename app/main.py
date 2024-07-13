from fastapi import FastAPI, Query
from pydantic import EmailStr
from datetime import datetime
import logging
from .tasks import send_email
import os

app = FastAPI()

logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

@app.get("/")
async def root(sendmail: EmailStr = Query(None), talktome: bool = Query(False)):
    if sendmail:
        send_email.delay(sendmail)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Email task queued for {sendmail} at {current_time} to be sent")
        return {"message": f"Email task queued for {sendmail} to be sent"}
    
    if talktome:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Current time logged: {current_time}")
        return {"message": "Current time logged"}
    
    return {"message": "Request processed, but no action was taken"}

@app.get("/logs")
async def get_logs():
    if os.path.exists('/var/log/messaging_system.log'):
        with open('/var/log/messaging_system.log', 'r') as log_file:
            log_entries = log_file.readlines()
        formatted_logs = [{"log": entry.strip()} for entry in log_entries]
        return {"logs": formatted_logs}
    else:
        return {"message": "Log file not found"}
