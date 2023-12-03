def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
        Bir nechta belgilardan iborat qator o'zgaruvchisi berilgan. Birinchi va oxirgi belgini qo'shing va qaytaring.
     Args:
         s(str): parametr
     Qaytaradi:
         str: javob
    """
    A = s[0]
    B = s[-1]
    javob = A + B
    return javob

# Misol uchun
s = "good"
natija =main(s) 
print(natija)  # Natija: "H!"  
   
