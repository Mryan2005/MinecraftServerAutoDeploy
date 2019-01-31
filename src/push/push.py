import subprocess
sh = r'.\src\push\push.sh'
def main():
    child = subprocess.Popen(sh,shell=True)
    child.wait()