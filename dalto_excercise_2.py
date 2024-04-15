#Excercise 2:

#A second is equal to 2 words

#Ask to use that say whatever text and:
#   -Calculate, how many words says?.
#   -Calculate, how many time takes to say that word?.

#If takes more than a minute:
#   Say to them, "Para flaco no me digas un testamento".

#Dalto talks 30% faster, how many time he takes in say the word?.


second = 0
word = ""


if second > 60:
    
    print("Para flaco no me digas un testamento")
    
else:
    
    #Normal dalto's speaking:
    word = 100 * (word / 30) - word

