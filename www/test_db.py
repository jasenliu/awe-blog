import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='jsliu', password='dm2018*', db='awe_blog')
    u = User(name='test2', email='test2@qq.com',
             password='123456', image='about:blank2')
    await u.save()
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
