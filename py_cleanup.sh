#!/bin/bash
# -*- coding: utf-8 -*-


cd "`dirname ${0}`"

rm -rf ./.cache ./.tox ./.coverage
find . -name '__pycache__' -exec rm -rf {} \;
find . -name '*.py[co]' -exec rm -f {} \;


# vim: ts=4:sw=4:noet:fdm=indent:ff=unix
