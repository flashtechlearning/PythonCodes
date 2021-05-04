#Commiting Code to Github

import subprocess
import time

#os.system('cmd /k "date"')

#os.system('"C:/Program Files/Git/git-bash.exe')

#subprocess.call('C:\Program Files\Git\git-bash.exe')

args = ["C:\Program Files\Git\git-bash.exe "]

child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#child_proccess.stdin.write(b"git status")

#child_process_output = child_proccess.communicate()[0]
time.sleep(5)



#print(child_process_output)
