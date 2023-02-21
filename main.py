from ncclient import manager
from dev_info import *
import time

start = time.perf_counter()
if __name__ == '__main__':
    with manager.connect(**ciscoA,hostkey_verify=False) as m:
        add=open("ciscoA.xml").read()
        response = m.edit_config(add, target="running")
        print("\n CiscoA was successfully configured \n" )
        
    with manager.connect(**ciscoB,hostkey_verify=False) as m:
         add_ciscoB=open("ciscoB.xml").read()
         m.edit_config(add_ciscoB, target="running")
         print("\n CiscoB was successfully configured \n" )

    with manager.connect(**ciscoC,hostkey_verify=False) as m:
         add_ciscoC=open("ciscoC.xml").read()
         a=m.edit_config(add_ciscoC, target="running")
         print(a )

    with manager.connect(**R21,hostkey_verify=False) as m:
         add_R21=open("R21.xml").read()
         m.edit_config(add_R21, target="running")
         print("\n R21 was successfully configured \n" )

    with manager.connect(**R11,hostkey_verify=False) as m:
         add_R11=open("R11.xml").read()
         m.edit_config(add_R11, target="running")
         print("\n R11 was successfully configured \n" )
     
    with manager.connect(**R22,hostkey_verify=False) as m:
         add_R22=open("R22.xml").read()
         m.edit_config(add_R22, target="running")
         print("\n R22 was successfully configured \n" )
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')