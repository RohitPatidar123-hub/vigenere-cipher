import os
##if __name__=="__main__":
## def choice_OfOoperation(choice)
##plaintext_to_cipher()
def choice_Of_operation(choice):
      match choice:
            case 1:
                   plaintext_to_ciphertext()
            case 2:
                   ciphertext_to_plaintext()
                          
            case 3:
                   print("Cryptanalysis Complete,Thank you")        
def plaintext_to_ciphertext():
        print("To convert Plaintext to cipher text you need to give Plaintext as well as their key :")
        str=input("Enter Your Plaintext :")
        str=str.upper()
        key=input("Enter your key : ")
        key=key.upper()
        str_length=len(str)
        key_length=len(key)
        cipher=''              
        i=0
        v=0
        for i in range(0,str_length):
                if  str[i]>='A' and str[i]<='Z':
                    l=ord(str[i]) -65                   
                    m= ord(key[(v)% key_length]) -65
                    c= chr((l+m)%26 +65)
                    cipher+=c
                    v+=1
                else:
                    cipher+=str[i] 
        print("Your Plaintext :",str)
        print("Your Ciphertext :",cipher)
        input()                             ##for hold comsole window
        os.system('cls')                    ##clear console window

        

def ciphertext_to_plaintext():
      print("Ciphertext to plaintext :")    
      
      

if __name__=="__main__" :
        choice=1
        while choice!=3:
            print("1.From Plaintext to Ciphertext")
            print("2 From Ciphertext to Plaintext")
            print("3 for exit")
            choice=int(input("Please Enter yput Choice[1,2,3]:"))
            choice_Of_operation(choice)

            
                
                    