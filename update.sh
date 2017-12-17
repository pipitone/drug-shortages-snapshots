#!/bin/bash
# Push latest snapshot
set -eu

cd $(dirname $(readlink -f $0))
echo $PWD

git pull -q -X theirs
venv/bin/python snapshot.py
git commit -qam "Export update `date`"
git push -q
