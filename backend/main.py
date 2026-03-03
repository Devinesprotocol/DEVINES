from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "CHAOS online"}

@app.get("/health")
async def health():
    return {"status": "ok"}
