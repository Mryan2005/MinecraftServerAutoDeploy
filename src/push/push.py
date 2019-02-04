import subprocess
sh = r'.\src\push\push.sh'
def main(choose):
    if choose == 1:
        child = subprocess.Popen(sh,shell=True)
        child.wait()
    elif choose == 2:
        push_add = subprocess.Popen('git add .',shell=True)
        push_add.wait()
        push_commit = subprocess.Popen('git commit -m update',shell=True)
        push_commit.wait()
        push_start = subprocess.Popen('git push origin',shell=True)
if __name__ == "__main__":
    main(2)