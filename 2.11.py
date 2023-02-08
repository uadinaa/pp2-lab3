def checking(WORD): 
    if WORD == WORD[::-1]: 
        return True 
    else: 
        return False 
 
 
WORD = input() 
print(checking(WORD))