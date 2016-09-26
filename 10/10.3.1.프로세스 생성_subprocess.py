import subprocess

#ret = subprocess.getoutput('date')
ret = subprocess.getoutput('date -u | wc')
print (ret)

print(subprocess.call('date'))