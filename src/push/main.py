import subprocess
sh = r'.\src\push\updat.sh'
child = subprocess.Popen(sh,shell=True)
child.wait()