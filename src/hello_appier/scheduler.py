#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class Scheduler(appier.Scheduler):

    def __init__(self, owner, timeout = 90.0, requests = 100, *args, **kwargs):
        appier.Scheduler.__init__(self, owner, timeout = timeout, *args, **kwargs)
        self.requests = appier.conf("HELLO_REQUESTS", requests, cast = int)

    def tick(self):
        appier.Scheduler.tick(self)
        for _index in range(self.requests):
            appier.get("https://httpbin.org/image")
