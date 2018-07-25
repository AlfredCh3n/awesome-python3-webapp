import orm
import asyncio,sys
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, port=3306, user='strawchen', password='116115', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank', admin=False)

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()