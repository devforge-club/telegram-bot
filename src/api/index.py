from fastapi import FastAPI

app = FastAPI

@app.get("/")
async def get_status():
    return {"status": "OK"}