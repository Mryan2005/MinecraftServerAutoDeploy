import subprocess
sh = r'.\src\pull\pull.sh'
child = subprocess.Popen(sh,shell=True)
child.wait()