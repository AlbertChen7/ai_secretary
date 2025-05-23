
from fastapi import FastAPI, Query
from app.router import handle_message

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Please let me know your request"}

@app.get("/sms")
@app.post("/sms")
async def receive_sms(text: str = Query(...), msisdn: str = Query(...)):
    response, intent, name, role = await handle_message(text, msisdn)
    return {"status": "ok", "message": response, "intent": intent, "name": name, "role": role}