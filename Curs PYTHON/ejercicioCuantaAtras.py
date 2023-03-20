import time

for x in range(10,-1,-1):
    if x !=0:
    #print(x)
        print(f"\r{x}",end=" ")
        time.sleep(1)
    else:
        print(f"\r{x}",end=" ")
        print("Fin cuenta atras")