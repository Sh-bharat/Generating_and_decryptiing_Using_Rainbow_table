def decrypthash(encrypted_hash):
    file=open("hashes.txt","r")
    for line in file:
        
        if(encrypted_hash==line[0:line.find(":")]):
            print("Key found : ",line[line.find(":")+1:])
            return True  
    print("key not Found :try with bigger Rainbow table")
    return False
            
encrypted_hash=input("Enter MD5 Hash : ")
decrypthash(encrypted_hash)