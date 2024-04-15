import random

def password_generator(range_password):
    
    chars = "1234567890!#$%&/()=?¡¡¿¨*[][]{+´<>.,-_;:qazwsxedcrfvtgbyhnujmikolpñ?" 
    
    password = ''.join(random.choice(chars) for _ in range(password_range))
    
    return password
    


password_range = int(input("Give the range for generate a new password: "))

print(password_generator(password_range))