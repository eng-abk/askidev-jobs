import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Job Analyzer API")

# Your existing API code here...
@app.get("/")
async def root():
    return {"message": "Job Analyzer API Running on Railway!"}

@app.get("/api/v1/jobs")
async def get_jobs():
    return {"jobs": "Your job data will be here"}

# Add this for Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
