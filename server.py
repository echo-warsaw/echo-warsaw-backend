import os
import asyncio
import argparse
import aiohttp_jinja2
import jinja2
from datetime import datetime, timedelta
from aiohttp import web
from pymongo import MongoClient

from app.models import Subscription

APP_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_DIR = os.path.join(APP_DIR, 'static')

parser = argparse.ArgumentParser()
parser.add_argument('--port')

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('static', './'))

@aiohttp_jinja2.template('index.html')
async def index(request):
    return

async def add_entry(request):
    data = await request.json()
    print('data', data)
    data['data']['offset'] = datetime.today() - timedelta(days=3)
    sub = Subscription(data['data'])
    try:
        sub.m.save()
        return web.json_response(status=200, data={'ok': True})
    except:
        return web.json_response(status=500, data={'ok': False})

app.router.add_post('/api/new', add_entry)
app.router.add_get('/', index)
app.router.add_static('/static', STATIC_DIR)

if __name__ == '__main__':
    db = MongoClient().echo

    args = parser.parse_args()
    port = int(args.port) if args.port else 8001
    web.run_app(app, host='127.0.0.1', port=port)
