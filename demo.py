str=input("Enter your Cipher text:")
str=str.upper()
print(str)
freq_table=[]                         ##to store Alphabet , frequency,frequency-1,(frequency*frequency-1)
freq_count=0                          ## total valid letters n
freq_total=0                          ## sum of all ni*ni-1
for i in range(0,26) :
     V=[]
     ch=chr(65+i)
     n=str.count(ch)
     n1=n-1
     total=n*n1
     V.append(ch)
     V.append(n)
     V.append(n1)
     V.append(total)
     freq_table.append(V)
     freq_count=freq_count+n                        ## total valid letters n
     freq_total=freq_total+total                    ## sum of all ni*ni-1
V=[]
V.append('Total')  
V.append(freq_count)
V.append('Null')
V.append(freq_total) 
freq_table.append(V)   
for i in freq_table:
    print(i)    


    