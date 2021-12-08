#!/bin/sh

protoc -I=. --python_out=../share ./*.proto
