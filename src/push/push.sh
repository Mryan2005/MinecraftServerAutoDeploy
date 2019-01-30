#!/bin/bash
source ./setting.config
server_name=$server_name
cur_dateTime="`date +%Y-%m-%d,%H:%m:%s`"
cd '/root'
if [[ ! -d "$server_name" ]]; then
	echo "文件夹不存在"
else
	echo "文件夹存在"
fi
git add .
git commit -m 'update'
git push origin