def main(s, n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
        s string o'zgaruvchisi berilgan. n Indeksdagi belgini qaytaring, aks holda False qiymatini qaytaring.
     Args:
         s(str): parametr
     Qaytaradi:
         str: javob
    """
    if n < len(s):
        
        return s[n]
    else:
        return False
Z= main("good", 3)
print(Z)  
    
