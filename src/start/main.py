import subprocess
sh = r'.\src\start\start.sh'
start = subprocess.Popen(sh,shell=True)
child.wait()