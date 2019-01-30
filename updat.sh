#!/bin/bash
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
git add .
git commit -m 'update ${cur_dateTime}'
git push origin