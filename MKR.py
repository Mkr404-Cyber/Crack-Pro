import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/link.has.been.error/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf GREEN64.so GREEN32.so')
except:
    pass
os.system('rm -rf GREEN.so GREEN32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('GREEN64.so'):
        os.system('curl -L https://github.com/X-R-404/tast/blob/main/GREEN64.cython-311.so?raw=true -o GREEN64.so') 
        os.system("python GREEN64")
    else:
        os.system("git clone https://github.com/X-R-404/tast && cd tast && python GREEN32.py")

elif bit == '32bit':
    if not os.path.isfile('GREEN32.so'):
        os.system('curl -L https://github.com/X-R-404/tast/blob/main/GREEN32.py?raw=true -o GREEN32.py') 
        os.system("python GREEN32.py")
    else:
        os.system("git clone https://github.com/X-R-404/tast && cd tast && python GREEN32.py")
