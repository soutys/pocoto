# -*- coding: utf-8 -*-


FROM python:3.6
MAINTAINER soutys
ADD . /pocoto
WORKDIR /pocoto
ENV SERVICE_CONFIGURATION dev
RUN pip install -r ./requirements/dev.txt
RUN tox -c ./tox.ini
RUN python ./manage.py check
RUN ./py_cleanup.sh


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
