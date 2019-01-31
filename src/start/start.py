import subprocess
sh = r'.\src\start\start.sh'
def main():
    start = subprocess.Popen(sh,shell=True)
    start.wait()