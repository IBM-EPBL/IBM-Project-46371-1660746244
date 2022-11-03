import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization="mkgfko"
deviceType="raspberrypi"
deviceId="12345"
authMethod="token"
authToken="12345678" 

try:
    deviceOptions={"org": organization,"type": deviceType,"id": deviceId,"auth-method": authMethod,"auth-token": authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("caught exception connecting device:%s" % str(e))
    sys.exit()
    
deviceCli.connect()
while True:
          #in data 
          lattitude=11.7345;
          longtitude=78.2020;

          #out data
          #lattitude=12.7345;
          #longtitude=79.2020;
          
          data={'lattitude':lattitude,'longtitude':longtitude}
          def myOnPublishCallback():
            print("published lattitude=%d" %lattitude,"longtitude=%d" %longtitude,"to ibm watson")
          
        
          success=deviceCli.publishEvent("IotSensor","json",data,qos=0,on_publish=myOnPublishCallback)
          if not success:
              print("Not connected to IoTF")
          time.sleep(3)
deviceCli.disconnect()




















                
