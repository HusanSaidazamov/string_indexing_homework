def main(s,n):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
        Besh uzunlikdagi qator berilgan. "*" belgisining indeksini qaytaring, agar mavjud bo'lmasa, False qiymatini qaytaring.
     Args:
         s(str): parametr
     Qaytaradi:
         int: javob
    """
    if n < len(s):
        
        return s[n]
    else:
        return False
Z= main("2*44", 1)
print(Z)  

        