import subprocess
c = subprocess.Popen(['sudo','yum','install','git','-y'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
grep_stdout = c.communicate(input='root')[0]
print(grep_stdout)
