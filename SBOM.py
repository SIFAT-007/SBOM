import os
try:
    os.system("git pull")
    __import__('SBOM').api_choose()
except:
    pass
