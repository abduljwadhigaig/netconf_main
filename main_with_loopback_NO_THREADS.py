from ncclient import manager
from dev_info import *
import threading
import time
start = time.perf_counter()


def configure_device():
    
    # Start a network-wide transaction
    dev=["ciscoA","ciscoB","ciscoC","R21","R22","R11"]
    for i in dev :
        xml_file_name=str(i)+".xml"
        dic_name=i
        xml_payload=open(xml_file_name).read()
    
        with manager.connect(**eval(dic_name),hostkey_verify=False) as m:
        # Change the hostname of the device
             m.edit_config(xml_payload,target='running')
             time.sleep(3)
             print(" configuration successful",dic_name)
             for i in range(1,254):
        # Change the hostname of the device
                 xml_payload1= open("loopback.xml").read().format(name=i,ip_address= i )
                 m.edit_config(xml_payload1,target='running')
                 print(" configuration Loobback ",i, "successful",dic_name)
 
    




# Connect to each device concurrently

configure_device()



finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')