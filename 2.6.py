def Reverse(sentence): 
    return " ".join(sentence.split()[::-1]) 
 
senten = input() 
senten = str(senten) 
print(Reverse(senten))