from fastapi import FastAPI
from makecal import make_calendar

app = FastAPI()
@app.get("/")
async def main():
    return {"hello":"world"}

@app.get("/capstone.ics")
async def mycal():
    return make_calendar()
