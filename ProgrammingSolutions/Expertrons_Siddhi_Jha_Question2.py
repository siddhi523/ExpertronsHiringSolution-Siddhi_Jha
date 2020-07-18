'''
Assumption: Output must contain only unique users even if List_A or List_B has duplicate users
eg->
A: ['ram', 'ram', 'ram', 'raju']
B: ['ram', 'raj']
output: ['raj', 'raju'] not ['ram', 'ram', 'raj', raju']
'''
#Function to remove duplicates from both list
def func(A, B):
    
    set_a = set(A) #convert list A to set
    set_b = set(B) #convert list B to set
    
    #subtract intersection of sets from their union 
    return (set_a.union(set_b) - set_a.intersection(set_b))

#take input from user
A = input() 
A = A.split(" ") #store in a list
B = input()
B = B.split(" ") #store in a list

print(list(func(A, B)))