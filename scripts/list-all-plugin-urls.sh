#!/usr/bin/env sh

# list-all-plugins-urls.sh
# creates the file ./ALL_PLUGINS.txt if it doesn't already exist.

ALL_PLUGINS=$(cat Unofficial-search-plugins.mediawiki | grep -i "search-plugin" | python -c $'import sys; print("\\n".join([(line.split(".py ")[0] + ".py").strip("| [") for line in sys.stdin.readlines() if ".py" in line]))')

echo "${ALL_PLUGINS}" | tee ./ALL_PLUGINS.txt
