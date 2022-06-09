import platform
r =platform.architecture()
print(r)

import os,sys

os.chdir(sys.path[0]);
dir_name = os.path.abspath(os.path.join(os.getcwd(),"."))
print(dir_name)