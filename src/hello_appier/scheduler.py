#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class Scheduler(appier.Scheduler):

    def __init__(self, owner, timeout = 90.0, requests = 100, *args, **kwargs):
        appier.Scheduler.__init__(self, owner, timeout = timeout, *args, **kwargs)
        self.requests = appier.conf("HELLO_REQUESTS", requests, cast = int)
        self.bytes = 0

    def tick(self):
        appier.Scheduler.tick(self)
        self.logger.info("Running remote retrieval process ...")
        for _index in range(self.requests):
            result = appier.get("https://httpbin.org/image")
            self.bytes += len(result)
        self.logger.info("Current byte count is %d bytes" % self.bytes)
