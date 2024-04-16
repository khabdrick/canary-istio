import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        print(response.status)

async def send_requests(url, amount):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(amount)]
        await asyncio.gather(*tasks)

url = 'http://localhost/home/'#put the url here
amount = 500  # Number of requests to send

asyncio.run(send_requests(url, amount))
