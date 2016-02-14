#!/usr/bin/python
# -*- coding: utf-8 -*-

import guppy
import threading

import appier

class Scheduler(appier.Scheduler):

    def __init__(self, owner, timeout = 90.0, requests = 100, *args, **kwargs):
        appier.Scheduler.__init__(self, owner, timeout = timeout, *args, **kwargs)
        self.requests = appier.conf("HELLO_REQUESTS", requests, cast = int)
        self.asset_url = appier.conf("HELLO_ASSET", "https://httpbin.org/image")
        self.leak = appier.conf("HELLO_LEAK", False, cast = bool)
        self.heap = None
        self.bytes = 0

    def tick(self):
        appier.Scheduler.tick(self)
        if self.leak and not self.heap:
            self.heap = guppy.hpy()
            self.heap.setrelheap()
        self.logger.info("Running remote retrieval process ...")
        for _index in range(self.requests):
            result = appier.get(self.asset_url)
            self.bytes += len(result)
            del result
        self.logger.info("Current byte count is %d bytes" % self.bytes)
        if self.leka:
            state = self.heap.heap()
            print("%d active threads" % threading.activeCount())
            print(state)
