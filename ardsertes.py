
# coding: utf-8

# In[1]:

import serial


# In[2]:

ser = serial.Serial('/dev/ttyUSB0', 9600)


# In[ ]:

ser.write('5')


# In[ ]:

try:  
    arduino = serial.Serial('/dev/ttyUSB0', 9600)  
except:  
    print "Failed to connect on /dev/ttyUSB0"  
    
    
try:  
    arduino.write('Y')  
    time.sleep(1)  
    print arduino.readline()  
except:  
    print "Failed to send!"  


# In[3]:

#from arduino import Arduino
#import time

#b = Arduino('/dev/ttyUSB0')
#pin = 9

#declare output pins as a list/tuple
#b.output([pin])

#for x in range(10):
#    b.setHigh(pin)
#    time.sleep(1)
#    print b.getState(pin)
#    b.setLow(pin)
#    print b.getState(pin)
#    time.sleep(1)

#b.close()


# In[ ]:



