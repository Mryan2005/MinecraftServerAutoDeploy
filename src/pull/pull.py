import subprocess
if __name__ == "__main__":
    sh = r'.\src\pull\pull.sh'
    child = subprocess.Popen(sh,shell=True)
    child.wait()
if __package__ == __spec__