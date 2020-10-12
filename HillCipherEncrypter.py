#Hill Cipher Character Set of size 73
hc_Char=['0','1','2','3','4','5','6','7','8','9',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','\'','.','!','?','*','\"','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',';','\n']

#Function to multiply matrix and get its modulous 
def multiMatrix(chrMatrix,keyMatrix):
    K=keyMatrix
    d=chrMatrix
    res=[0,0,0,0]
    res[0]=(K[0][0]*d[0])+(K[0][1]*d[1])+(K[0][2]*d[2])+(K[0][3]*d[3])
    res[1]=(K[1][0]*d[0])+(K[1][1]*d[1])+(K[1][2]*d[2])+(K[1][3]*d[3])
    res[2]=(K[2][0]*d[0])+(K[2][1]*d[1])+(K[2][2]*d[2])+(K[2][3]*d[3])
    res[3]=(K[3][0]*d[0])+(K[3][1]*d[1])+(K[3][2]*d[2])+(K[3][3]*d[3])
    
    res[0]=(res[0]%73)
    res[1]=(res[1]%73)
    res[2]=(res[2]%73)
    res[3]=(res[3]%73)
    
    return res
#Primary Hill Cipher Function
def HillCipher(string,key):
    keyMatrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,0]]
    encryptStr=""
    k=0
    for i in range(0,4):
        for j in range(0,4):
            d=hc_Char.index(key[k])
            keyMatrix[i][j]=d
            k=k+1
    if(len(string)%4!=0):
        string=string+("x"*(4-(len(string)%4)))
    chrMatrix=[]
    
    for i in range(0,len(string),4):
        chrMatrix=[]
        for j in range(i,i+4):
            d=hc_Char.index(string[j])  
            chrMatrix.append(d)
           
        res=multiMatrix(chrMatrix,keyMatrix)
        tempStr=hc_Char[res[0]]+""+hc_Char[res[1]]+""+hc_Char[res[2]]+""+hc_Char[res[3]]
        encryptStr+=tempStr

    return encryptStr

string=input("Enter the text to be encrypted\n")
key=input("Enter Key Of 16 Characters\n")
print("Text after Hill Cipher\n",HillCipher(string,key))

        
        
            
                  
                  
                  
                  
        
