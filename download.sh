#!/bin/bash

set -e

wget http://fallabs.com/kyotocabinet/pkg/kyotocabinet-1.2.77.tar.gz
tar zxvf kyotocabinet-*.tar.gz

cd kyotocabinet-1.2.77
patch < ../rm_native_optimization.patch
