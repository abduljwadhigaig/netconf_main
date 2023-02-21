from ncclient import manager
from dev_info import *
import threading
import time
start = time.perf_counter()
lock = threading.Lock()

def configure_device(xml_payload,**dev_inf):
    # Start a network-wide transaction
    lock.acquire()  
    global dic_name
    
    with manager.connect(**dev_inf,hostkey_verify=False,timeout=200) as m:
        # Change the hostname of the device
        m.edit_config(xml_payload,target='running')
        
    print(" configuration successful",dic_name)
        # for i in range(1,254):
        # # Change the hostname of the device
        #     xml_payload1= open("loopback.xml").read().format(name=i,ip_address= i )
        #     m.edit_config(xml_payload1,target='running')
        #     print(" configuration Loobback ",i, "successful",dic_name)
    lock.release()
    


threads = []

# Connect to each device concurrently
dev=["ciscoA"]#,"ciscoB","ciscoC","R21","R22","R11"]
for i in dev :
    xml_file_name=str(i)+".xml"
    dic_name=i
    threads.append(threading.Thread(target=configure_device,args=[open(xml_file_name).read()],kwargs=eval(dic_name)))
print(threads)

# Start all the threads
for t in threads:
    t.start()

# Wait for all the threads to finish
for t in threads:
    t.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')