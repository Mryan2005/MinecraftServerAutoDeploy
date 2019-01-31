import subprocess
sh = r'.\src\init\init.sh'
start = subprocess.Popen(sh,shell=True)
child.wait()