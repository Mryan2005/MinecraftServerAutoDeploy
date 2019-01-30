#!/bin/bash
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
cd '/root'
git add .
git commit -m 'update'
git push origin