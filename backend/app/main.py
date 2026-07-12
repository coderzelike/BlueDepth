from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "application": "BlueDepth",
        "version": "0.1.0",
        "status": "Development"
    }