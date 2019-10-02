
# function for checkhing strings are anagrams or not 
def checking(text1, text2): 
      
    # the sorted strings are checked  
    if(sorted(text1)== sorted(text2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
#s1 ="listen"
#s2 ="silent" 
text1 = input("string 1 : ")
text2 = input("string 2 : ")
checking(text1, text2) 
