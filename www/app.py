import logging;logging.basicConfig(level=logging.DEBUG)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web, web_runner

async def index(request):
    return web.Response(body = b"<h1>awe-blog</h1>", headers = {"content-type": "text/html"})

def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:9000...')
    web.run_app(app, host='127.0.0.1', port=9000)

init()