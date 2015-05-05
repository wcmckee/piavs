
# coding: utf-8

# script that changes colour on led lights depending on the cords 

# In[68]:

import os
import json
import socket
import getpass
import time
import unicornhat as uh


# In[ ]:

#uh.brightness(1)


# In[3]:

gethos = socket.gethostname()
#geusr = getpass.getuser()


# In[4]:

#geusr


# In[5]:

gethos


# In[33]:

lisdirz = '/home/wcmckee/sellcoffee/'


# In[34]:

os.listdir(lisdirz)


# In[38]:

optouch = open(lisdirz + 'touch.json', 'r')


# In[39]:

#(optouch.read())


# In[ ]:




# In[ ]:




# In[40]:

opjsza = json.loads(optouch.read())

print opjsza


# In[55]:

ycord = opjsza['y']


# In[56]:

ycord


# In[57]:

xcord = opjsza['x']


# In[58]:

zcord = opjsza['z']


# In[59]:

touchval = opjsza.values()


# In[60]:

for touchv in touchval:
    print touchv[:3]
    print opjsza.keys()


# In[ ]:

#turn into rgb 


# In[71]:

sycord = ycord[3]


# In[72]:

szcord = zcord[3]


# In[73]:

zycord = ycord[3]


# In[78]:

isyc = int(sycord)


# In[79]:

szrc = int(szcord)


# In[84]:

if isyc == 8 or 9:
    isyc = 7
    
if szrc == 8 or 9:
    szrc = 7


# In[85]:

isyc


# In[88]:

adzerp = str(isyc) + str(0) 


# In[91]:

zyarp = str(szrc) + str(0) 


# In[90]:

sycintz = int(adzerp)


# In[92]:

zycintz = int(zyarp)


# In[87]:

#uh.brightness(1)

#uh.set_pixel(isyc, szrc, 102, 63, 105)

#uh.show()


# In[93]:

uh.brightness(int('0.')+ szrc)

while 1 == 1:
    for ext in range(8):
            uh.set_pixel(ext,ext, sycintz, zycintz, 105)
            for supz in range(8):
                        uh.set_pixel(ext, ext, sycintz, zycintz, 105)

    #os.system('python /home/wcmckee/github/signinlca/usertime.py')
    uh.show()
    time.sleep(1)

#UH.show()
time.sleep(1)


# In[ ]:



