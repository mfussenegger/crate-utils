#!/bin/bash

bin/cr8 timeit "$1" "$2" | jq 'del(.client_runtimes) | del(.server_runtimes)' | bin/cr8 json2insert benchmarks "$3"
