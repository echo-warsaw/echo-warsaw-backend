import asyncio
from aiohttp import web
from pymongo import MongoClient

from app.models import Subscription

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

async def add_entry(request):
    data = await request.json()
    print('data', data)
    sub = Subscription(**data)
    sub.m.save()
    return web.json_response({'ok': True})

app.router.add_post('/api/new', add_entry)

if __name__ == '__main__':
    db = MongoClient().echo

    web.run_app(app, host='127.0.0.1', port=8001)
