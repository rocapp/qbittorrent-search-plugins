#!/usr/bin/env sh

# download-all-plugins.sh

mkdir -p ./plugins && \
    xargs -a ./ALL_PLUGINS.txt -n 1 -P 4 wget -P ./plugins/
