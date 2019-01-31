#!/bin/bash
source ./setting.config
server_name=$server_name
server_version=$server_version
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
cd /root/${server_name}
git add .
git commit -m 'update'
git push origin