def igpay(word):  
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:  
        print(word + "way")  
    else:  
        print(word[1:] + word[0] + "ay" )

igpay("pig")