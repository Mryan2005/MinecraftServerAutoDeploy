echo "开始安装jdk开始..."
echo "start install jdk"
mkdir /root/java
cd /root/java
echo "创建usr/local/java文件夹成功"
yum -y list java*
yum -y install java-1.8.0-openjdk*
echo '安装完成'
java -version
echo '请将JAVA_HOME=/root/java/jdk1.8.0_152写入profile'
vim /etc/profile
source /etc/profile