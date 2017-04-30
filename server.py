import os
import asyncio
import aiohttp_jinja2
import jinja2
from datetime import datetime, timedelta
from aiohttp import web
from pymongo import MongoClient

from app.models import Subscription
from keywords_search import generate_synonyms as gn

APP_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_DIR = os.path.join(APP_DIR, 'static')

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('static', './'))

@aiohttp_jinja2.template('index.html')
async def index(request):
    return

async def add_entry(request):
    print("wszedlem")
    data = await request.json()
    data['data']['offset'] = datetime.today() - timedelta(hours=24)
    data['data']['synonyms'] = list(gn.generate_synonyms(data['data']['keyword']))
    sub = Subscription(data['data'])
    print("po modelu")
    try:
        print(data['data']['synonyms'])
        print("przed zapisaniem")
        sub.m.save()
        print("ok zapisane")
        return web.json_response(status=200, data={'ok': True})
    except:
        return web.json_response(status=500, data={'ok': False})

app.router.add_post('/api/new', add_entry)
app.router.add_get('/', index)
app.router.add_static('/static', STATIC_DIR)

if __name__ == '__main__':
    db = MongoClient().echo

    web.run_app(app, host='127.0.0.1', port=8001)
