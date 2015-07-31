#!/usr/bin/env python
# -*- coding: utf-8 -*-


from timeit import timeit
from json2insert import json2insert
import argh



def main():
    p = argh.ArghParser()
    p.add_commands([timeit, json2insert])
    p.dispatch()


if __name__ == '__main__':
    main()
