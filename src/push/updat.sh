#!/bin/bash
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
git add .
git commit -m 'update'
git push origin