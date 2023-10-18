#Bharat Sharma 23MDT1051 
#-----------------------Rainbow tables for MD5 hash 
import time
import hashlib
import itertools

# taking input from user
Characterset=input("Enter Character Set : ")
length=int(input("Enter length of Plain text : "))


#cleaning Character set
Characters_list=[]
for Character in Characterset:
    if Character not in Characters_list:
        Characters_list.append(Character)
Characterset=''.join(Characters_list)


file=open("hashes.txt","w")
start = time.time() 

#Generating Rainbowtable
for p in itertools.product(Characterset, repeat=length):
    passphrase=''.join(p)
    result=hashlib.md5(passphrase.encode()).hexdigest()+":"+passphrase
    file.write(result+"\n")
end = time.time()
print("\nRainbow table Generated Successfully.\nThe time of execution of above program is :",(end-start) * 10**3, "ms")
file.close()
