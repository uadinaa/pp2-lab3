def uni_list(lt): 
    unique = [] 
    for i in lt: 
        if i not in unique: 
            unique.append(i) 
    return unique 
 
 
print(uni_list([1, 456, 76, 335, 456, 1, 1, 45, 76]))