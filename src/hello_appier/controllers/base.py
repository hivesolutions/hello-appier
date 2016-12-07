#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import appier

class BaseController(appier.Controller):

    @appier.route("/", "GET", json = True)
    @appier.route("/index", "GET", json = True)
    def index(self):
        return self.redirect(
            self.url_for("base.headers")
        )

    @appier.route("/headers", "GET", json = True)
    def headers(self):
        return self.json(
            self.request.in_headers,
            sort_keys = True
        )

    @appier.route("/environ", "GET", json = True)
    def environ(self):
        return self.json(
            dict(os.environ),
            sort_keys = True
        )
