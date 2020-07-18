import re

#Function to check if number is valid or not
def valid(n):
    #check for length of number
    if(len(n) != 10):
        return False
    
    #structure of mobile number
    model = re.compile("[7-9][0-9]{9}");
    return model.match(n);

n = input() #take input from user

#check for validity
if(valid(n)):
    print("VALID")
else:
    print("NOT VALID")
