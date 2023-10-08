from fastapi import FastAPI
import asyncio
import schedule
import time
import httpx

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

async def fetch_data():
    print('asdads')
    async with httpx.AsyncClient() as client:
        response = await client.get("https://twofer-server.onrender.com/category/allcategory")
    print("hello", time.strftime("%Y-%m-%d %H:%M:%S"))

def run_scheduler():
    schedule.every(30).seconds.do(lambda: asyncio.run(fetch_data()))

if __name__ == "__main__":
    run_scheduler()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
