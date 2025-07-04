import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/encrypted/{plain_text}")
async def encrypted_string(plain_text: str): ...


@app.get("/secret/{secret_id}")
async def secret(secret_id: str):
    return {"secret": secret_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
