divpath='G:\\japan-div'
mypath='C:\\Users\\pRodigy\\Desktop\\kyoto-facebook'
finalpath='G:\\final-hd-kyoto'

import os
import shutil
from os import listdir
from os.path import isfile, join
myfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
divfiles = [ f for f in listdir(divpath) if isfile(join(divpath,f)) ]

for m in myfiles:
  if m in divfiles:
    print 'YES copy', os.path.join(divpath, m), ' to ', os.path.join(finalpath, m)
    shutil.copy(os.path.join(divpath, m), finalpath)
  else:
    print 'NO copy', os.path.join(mypath, m), ' to ', os.path.join(finalpath, m)
    shutil.copy(os.path.join(mypath, m), finalpath)
