import subprocess
sh = r'.\src\pull\pull.sh'
def main():
    child = subprocess.Popen(sh,shell=True)
    child.wait()
