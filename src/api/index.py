from fastapi import FastAPI

app = FastAPI(title="Main App")

@app.get("/")
async def get_status():
    return {"status": "OK"}