#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket

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

    @appier.route("/addresses", "GET", json = True)
    def addresses(self):
        addresses = socket.getaddrinfo(socket.gethostname(), None)
        return self.json(
            dict(addresses = addresses),
            sort_keys = True
        )

    @appier.route("/geo", "GET", json = True)
    def geo(self):
        address = self.request.get_address()
        result = appier.GeoResolver.resolve(address)
        return self.json(
            result,
            sort_keys = True
        )

    @appier.route("/retrieve", "GET", json = True)
    def retrieve(self):
        unsafe = appier.conf("UNSAFE", False, cast = False)
        appier.verify(
            unsafe,
            message = "Unsafe operations are not allowed",
            code = 401
        )
        url = self.field("url", mandatory = True)
        contents = appier.get(url)
        return contents
