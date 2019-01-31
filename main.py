import sys
import os
import string
import os.path
from src.init import init
from src.start import start
platform = sys.platform
if platform == 'win32':
    print('请等下一个版本的出现')
    os._exit(0)
elif platform == 'win64':
    print('请等下一个版本的出现')
    os._exit(0)
else:
    start.main()
    fo = open("/etc/profile", "w")
    huanjing='JAVA_HOME=/root/java/jdk1.8.0_152'
    if huanjing in fo:
        
    else:
        fo.write('JAVA_HOME=/root/java/jdk1.8.0_152')
        fo.close()