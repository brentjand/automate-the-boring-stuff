def spam():
    global eggs 
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon'  #this is local

def ham():
    print(eggs)  #this is glonbal

eggs = 42 #this is the global
spam()
print(eggs)
