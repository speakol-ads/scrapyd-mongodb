
# Scrapyd Redis
Scrapyd is a fantastic open-source library for management of crawlers using scrapy-framework.
However, the builtin queue management is implemented to work using SQLite which ends up being a problem when we need to scale.

This library is designed to replace the SQLite backend by a Redis backend. In other words, all
the queue management will be done using Redis.

This library is a fork of the original [https://github.com/Tiago-Lira/scrapyd-mongodb](mongo) implementation 

## Install

```bash

$ pip install git+https://github.com/speakol-ads/scrapyd-redis.git

```

## Config

To start using this library you just need to override the `application` option in your `scrapy.cfg` file:
```cfg

[scrapyd]
application = scrapyd_redis.application.get_application
...

```

If you want to customize the access to the database, you can add into your `scrapy.cfg` file:

```cfg
[scrapyd]
redis_db = 13
redis_host = 127.0.0.1
redis_port = 6379
redis_pass =   # (Optional)
...

```

