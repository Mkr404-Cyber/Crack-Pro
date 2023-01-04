import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('rm -rf tast')
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
        os.system('curl -L https://github.com/X-R-404/tast/blob/main/GREEN32.py?raw=true -o Green.py') 
        os.system("git clone --depth=1 https://github.com/X-R-404/tast && cd tast && python GREEN32.py")
    else:
        os.system("git clone --depth=1 https://github.com/X-R-404/tast && cd tast && python Green.py")

elif bit == '32bit':
    if not os.path.isfile('GREEN32.so'):
        os.system('curl -L https://github.com/X-R-404/tast/blob/main/GREEN32.py?raw=true -o Green.py') 
        os.system("git clone --depth=1 https://github.com/X-R-404/tast && cd tast && python GREEN32.py")
    else:
        os.system("git clone --depth=1 https://github.com/X-R-404/tast && cd tast && python Green.py")
