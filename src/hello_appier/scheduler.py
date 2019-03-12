#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gc
import threading

import appier

try: import guppy
except ImportError: guppy = None

try: import objgraph
except ImportError: objgraph = None

try: import psutil
except ImportError: psutil = None

class Scheduler(appier.Scheduler):

    def __init__(
        self,
        owner,
        timeout = 90.0,
        enabled = True,
        requests = 100,
        asset = "https://httpbin.org/image",
        *args,
        **kwargs
    ):
        appier.Scheduler.__init__(self, owner, timeout = timeout, *args, **kwargs)
        self.enabled = appier.conf("HELLO_ENABLED", enabled, cast = bool)
        self.requests = appier.conf("HELLO_REQUESTS", requests, cast = int)
        self.asset_url = appier.conf("HELLO_ASSET", asset)
        self.leak = appier.conf("HELLO_LEAK", False, cast = bool)
        self.gc = appier.conf("HELLO_GC", False, cast = bool)
        self.heap = None
        self.bytes = 0

    def tick(self):
        appier.Scheduler.tick(self)
        if not self.enabled: return
        self._init_leak()
        self.logger.info("Running remote retrieval process ...")
        for _index in range(self.requests):
            result = appier.get(self.asset_url)
            self.bytes += len(result)
            del result
        self.logger.info("Current byte count is %d bytes" % self.bytes)
        self._run_gc()
        self._status_leak()

    def _init_leak(self):
        if not self.leak: return
        if self.heap: return
        if self.gc: gc.set_debug(gc.DEBUG_LEAK)
        if guppy:
            self.heap = guppy.hpy()
            self.heap.setrelheap()

    def _status_leak(self):
        if not self.leak: return
        pid = os.getpid()
        print("%d active threads" % threading.activeCount())
        if guppy:
            print(self.heap.heap())
        if psutil:
            process = psutil.Process(pid)
            if hasattr(process, "open_files"): print(process.open_files())
            if hasattr(process, "connections"): print(process.connections())
            if hasattr(process, "num_fds"): print(process.num_fds())
            if hasattr(process, "memory_info_ex"): print(process.memory_info_ex())
            if hasattr(process, "memory_maps"): print(process.memory_maps())
        if objgraph:
            print("%d objects leaking" % len(objgraph.get_leaking_objects()))

    def _run_gc(self):
        if not self.leak: return
        gc.collect()
