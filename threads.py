from ncclient import manager
from dev_info import *
import threading
import time
start = time.perf_counter()
def configure_device(xml_payload,**dev_inf):
    # Start a network-wide transaction
    global dic_name
    with manager.connect(**dev_inf,hostkey_verify=False) as m:
        r = m.edit_config(xml_payload,target='running')
        print(r,dev_inf["host"])


threads = []

# Connect to each device concurrently
dev=["ciscoA","ciscoB","ciscoC","R21","R22","R11"]
for i in dev :
    xml_file_name=str(i)+".xml"
    dic_name=i
    threads.append(threading.Thread(target=configure_device,args=[open(xml_file_name).read()],kwargs=eval(dic_name)))


# Start all the threads
for t in threads:
    t.start()

# Wait for all the threads to finish
for t in threads:
    t.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
