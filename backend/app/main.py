from fastapi import FastAPI

app = FastAPI(
    title="Outdoor Bosun API",
    description="Backend for the Outdoor Bosun trekking assistant",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Outdoor Bosun API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}