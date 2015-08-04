#!/usr/bin/env python
# -*- coding: utf-8 -*-


from timeit import timeit
from json2insert import json2insert
from blobs import upload
import argh



def main():
    p = argh.ArghParser()
    p.add_commands([timeit, json2insert, upload])
    p.dispatch()


if __name__ == '__main__':
    main()
