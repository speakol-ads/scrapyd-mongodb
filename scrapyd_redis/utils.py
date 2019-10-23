# -*- coding: utf-8 -*-

from scrapyd.utils import get_project_list

from scrapyd_redis.spiderqueue import RedisSpiderQueue


def get_spider_queues(config):
    """Return a dict of Spider Quees keyed by project name"""
    queues = {}
    for project in get_project_list(config):
        queues[project] = RedisSpiderQueue(config, project)
    return queues
