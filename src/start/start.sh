server_name=
# 服务器名
# 服务器文件会放在root文件夹
server_version=
# 服务器核心版本
# 例如：PaperSpigot_1.8.8
if [[ ! -d "$server_name" ]]; then
    echo "文件夹不存在"
    echo '正在clone'   
	git clone https://github.com/superserver/$server_version.git /root/$server_name
    echo 'clone完成'
else
	echo "文件夹存在"
    cd /root/$server_name
fi
echo '开始服务器'
java -Xmx768M -Xms512M -jar /root/$server_name