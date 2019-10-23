# -*- coding: utf-8 -*-

import json
import redis
from configparser import NoOptionError


class RedisPriorityQueue(object):

    def __init__(self, config, collection):
        database_name = config.get('redis_db', 0)
        database_host = config.get('redis_host', 'localhost')
        database_port = config.getint('redis_port', 27017)
        database_user = self.get_optional_config(config, 'redis_user')
        database_pwd = self.get_optional_config(config, 'redis_pass')

        self.conn = redis.StrictRedis(
            host=database_host,
            port=int(database_port),
            charset="utf-8", 
            decode_responses=True,
            db=int(database_name), 
            password=database_pwd
        )

        self.queue = "scrapyd-redis.queue.{}".format(collection)

    @staticmethod
    def get_optional_config(config, name):
        try:
            return config.get(name).replace('\'', '').replace('"', '')
        except NoOptionError:
            return None

    def put(self, message, priority=0.0):
        self.conn.zincrby(self.queue, priority, self.encode(message))

    def pop(self):
        try:
            _item = self.conn.zrevrange(self.queue, 0, 0)[0]
            if self.conn.zrem(self.queue, _item) == 1:
                return self.decode(_item)
        except IndexError:
            pass

    def remove(self, func):
        count = 0
        for msg in self.conn.zrange(self.queue, 0, -1):
            if func(self.decode(msg)):
                self.conn.zrem(self.queue, msg)
                count += 1
        return count

    def clear(self):
        self.conn.delete(self.queue)

    def __len__(self):
        return self.conn.zcard(self.queue)

    def __iter__(self):
        return ((self.decode(obj[0]), obj[1]) for obj in self.conn.zrange(name=self.queue, start=0, end=-1, withscores=True))

    def encode(self, obj):
        return json.dumps(obj)

    def decode(self, text):
        return json.loads(text)
