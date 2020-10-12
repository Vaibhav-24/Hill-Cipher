#Function to multiply Key inverse matrix with the characters index obtained
def mul(Kinv,d):
    res=[0,0,0,0]
    res[0]=(Kinv[0][0]*d[0])+(Kinv[0][1]*d[1])+(Kinv[0][2]*d[2])+(Kinv[0][3]*d[3])
    res[1]=(Kinv[1][0]*d[0])+(Kinv[1][1]*d[1])+(Kinv[1][2]*d[2])+(Kinv[1][3]*d[3])
    res[2]=(Kinv[2][0]*d[0])+(Kinv[2][1]*d[1])+(Kinv[2][2]*d[2])+(Kinv[2][3]*d[3])
    res[3]=(Kinv[3][0]*d[0])+(Kinv[3][1]*d[1])+(Kinv[3][2]*d[2])+(Kinv[3][3]*d[3])
    res[0]=(res[0]%73)
    res[1]=(res[1]%73)
    res[2]=(res[2]%73)
    res[3]=(res[3]%73)
    return res
    

#Function to find charater index in the given character set s
def ind(a):
    s=['0','1','2','3','4','5','6','7','8','9',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','\'','.','!','?','*','\"','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',';','\n']
    f=False
    for i in range(0,73):
        if(s[i]==a):
            f=True
            return i
    if(f==False):
        return 72


#Function to find modulo inverse of a with respect to m
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

#Function to print the 4 character obtained after decrypting
def printer(k):
    s=['0','1','2','3','4','5','6','7','8','9',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','\'','.','!','?','*','\"','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',';','\n']
    for i in range(0,4):
        p=k[i]
        print(s[p],end='')



#Store your 4X4 key inverse matrix in Kinv    
Kinv=[[288,34927,36370,20],[65,6003,18,215325],[115936,2,165138,17],[25396,39,19,47468]]
#Store your 4X4 modulus    
m=modInverse(2458156,73)
for i in range(0,4):
    for j in range(0,4):
        Kinv[i][j]=(m*Kinv[i][j])%73

s=['0','1','2','3','4','5','6','7','8','9',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','\'','.','!','?','*','\"','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',';','\n']
count=0
x=0
d=[]

#Specify the number of lines (separated by \n ) in input text
no_of_lines = 45
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"

print("\n Decyphered Code :-")
ending=False
s=lines
for i in range(0,len(s),4):
    if(ending==False):
        x=0
        d=[]
        k=[]
        for j in range(i,i+4):
            d.append(ind(s[j]))
            x=x+1;
            if(i==len(s)-1):
                ending=True
                break
        
        
        
    k=mul(Kinv,d)
    printer(k)
    

    
#This code was contributed by Vaibhav Tripathi
#Contact me my mailing to vaibhavtripthi2420@gmail.com for any queries or suggestions


