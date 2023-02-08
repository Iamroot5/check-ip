                                                           
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
import os
print(os.system('ipconfig'))

# Importing random to generate
# random string sequence
import random
   
# Importing string library function
import string

def rand_pass(size):
        
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                        string.digits)
                                            for n in range(size)])
                            
    return generate_pass
   
# Driver Code 
password = rand_pass(10)
print(password)