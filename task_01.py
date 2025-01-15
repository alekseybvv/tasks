def is_palindrome(string):
    if string is None:
        return False
    
    string = str(string)
    
    string = string.lower()
    empty_string = ""
    for char in string:
        if char.isalnum():  
            empty_string += char
    
    return empty_string == empty_string[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))  
print(is_palindrome("Madam, I'm Adam!"))                 
print(is_palindrome(333))                                
print(is_palindrome(None))                               
print(is_palindrome("Abracadabra"))                      
