import subprocess
sh = r'.\src\init\init.sh'
def main():
    start = subprocess.Popen(sh,shell=True)
    child.wait()