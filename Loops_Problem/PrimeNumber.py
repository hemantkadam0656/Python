number = 68

prime = True

if number > 1:
    for i in range(2,number):
        if (number%i == 0):
            prime = False
            break
        
if prime == True:
    print(number," is prime number")
else:
    print(number," is NOT prime number") 

    
        

        
        


