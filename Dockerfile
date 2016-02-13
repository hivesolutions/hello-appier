FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV MONGOHQ_URL mongodb://localhost:27017
ENV PYTHONPATH /src

ADD requirements.txt /
ADD src /src

RUN pip install -r /requirements.txt && pip install --upgrade netius

CMD ["/usr/bin/python", "/src/hello_appier/main.py"]
