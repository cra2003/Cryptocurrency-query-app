import logging
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from final_reply import final
from redis import Redis

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Query(BaseModel):
    session_id: str
    query: str
    source_language: str = "English"

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    ip_address = request.client.host
    key = f"rate_limit:{ip_address}"
    redis = Redis(host='localhost', port=6379, db=0)
    if redis.get(key) and int(redis.get(key)) >= 6:
        logger.warning(f"Rate limit exceeded for IP: {ip_address}")
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    redis.incr(key)
    redis.expire(key, 60)
    return await call_next(request)

@app.post("/query")
async def query_crypto(query: Query):
    try:
        response = final(query.session_id, query.query, query.source_language)
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
