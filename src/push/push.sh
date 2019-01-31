#!/bin/bash
server_name=
# 服务器名
# 服务器文件会放在root文件夹
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
cd /root/${server_name}
git add .
git commit -m 'update'
git push origin