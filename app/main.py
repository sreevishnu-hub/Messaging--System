# app/main.py
import asyncio
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

# Fix event loop issue (WSL + uvicorn)
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

app = FastAPI()

# Health check route
@app.get("/")
async def root():
    return {"message": "FastAPI app is running!"}

# /action route for sending emails
@app.get("/action")
async def action(sendmail: str = Query(..., description="Email address to send to")):
    # Here you would call your Celery task, e.g.
    # tasks.send_email.delay(sendmail)
    return JSONResponse({"message": f"Email task submitted for {sendmail}"})

# Optional: run uvicorn directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8001,  # or your preferred free port
        reload=True,
        loop="asyncio",
        workers=1
    )
