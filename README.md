# Hello Appier

Simple hello world application for [Appier](http://appier.hive.pt).

## Configuration

| Name | Type | Description |
| ----- | ----- | ----- |
| **HELLO_ENABLED** | `bool` | If the async HTTP client requests started as scheduler should be enabled (defaults to `True`). |
| **HELLO_REQUESTS** | `int` | Number of HTTP client requests to be performed as part of the initial scheduler (defaults to `100`). |
| **HELLO_ASSET** | `str` | The HTTP URL that is going to be used for the initial client testing (defaults to `https://httpbin.org/image`). |
| **HELLO_LEAK** | `bool` | If HTTP client memory leaking metrics should be gathered (defaults to `False`). |
| **HELLO_GC** | `bool` | If a garbage collection operation should be performed after execution of the HTTP client operations (defaults to `False`). |
| **HELLO_UNSAFE** | `bool` | If the unsafe operation should be allowed (defaults to `False`). |
