# pkg-kyotocabinet
RPM packaging of Kyoto Cabinet for Sailfish

## Howto build

* Clone this repository

* cd into it and run `./download.sh`

* cd into source directory

* build by running 
```
export SFARCH=armv7hl; mb2 -t SailfishOS-$SFARCH -s ../kyotocabinet.spec build
```
in MER SDK.

* RPMs are under RPMS directory.

Please let me know if there are some errors (missing dependencies, for
example) during building by opening an issue for this repository.
