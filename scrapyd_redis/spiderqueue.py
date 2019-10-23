# -*- coding: utf-8 -*-

from zope.interface import implementer
from scrapyd.interfaces import ISpiderQueue
from scrapyd.spiderqueue import SqliteSpiderQueue

from scrapyd_redis.redis import RedisPriorityQueue


@implementer(ISpiderQueue)
class RedisSpiderQueue(SqliteSpiderQueue):

    def __init__(self, config, collection):
        self.q = RedisPriorityQueue(config, collection)
