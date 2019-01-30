import subprocess
sh = r'.\src\push\push.sh'
child = subprocess.Popen(sh,shell=True)
child.wait()