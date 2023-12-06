def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
        bitta belgilar qatori beriladi. Uni int turiga aylantiring, iloji bo'lmasa -1ni qaytaring.
     Args:
         s(str): parametr
     Qaytaradi:
         int: javob
    """
    if s:
        
        return int(s)
    if str(s):
        return str(s)

# Test qilish
test_string1 = "sew"


print(main(test_string1))  # 123

