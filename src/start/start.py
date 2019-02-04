import subprocess
import os
sh = r'.\src\start\start.sh'
def main(choose):
    if choose == 1:
        start = subprocess.Popen(sh,shell=True)
        start.wait()
    elif choose == 2:
        os.c
if __name__ == "__main__":
    main()