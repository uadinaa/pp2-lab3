def rev_words(s): 
    s = s.split() 
    s.reverse() 
    return ' '.join(s) 
s = input() 
print(rev_words(s)) 
 