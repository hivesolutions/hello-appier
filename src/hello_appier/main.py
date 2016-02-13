#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from hello_appier import scheduler

class HelloApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            name = "hello"
        )
        self.scheduler = scheduler.Scheduler(self)

    def start(self):
        appier.WebApp.start(self)
        self.scheduler.start()

if __name__ == "__main__":
    app = HelloApp()
    app.serve()
