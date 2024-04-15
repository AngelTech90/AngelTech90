


#python 3.7

#we define a string var.
name = "Angelina"

#we define a num var.
numberOfVisits = 12

#we define a string var with iterals of other vars, using f for don't have any trouble 
welcoming = f"hi {name} is this the {numberOfVisits} time we see us yeah?"

#we delete our var.
print(welcoming)
print("-------------")#Indent

#we create an array
listt = [8,71,62,"have"]
print(listt[0])
print("-------------")#Indent
    #shows 8

#*Here we create a tuple.
sphere = (8,71,62,"have")
print(sphere[3])
print("-------------")#Indent
    #shows "have"

#for create a set
ballon = {8,71,62,"have"}
print(ballon)
print("-------------")#Indent

#shows 8,71,62,"have"

#for create a dictionary
Angel = {

'name':"Angel",
'second_name':"Molina",
'age':17,
'alone':True

}

print(Angel['name'])
print("-------------")#Indent
    #shows "Angel"aac


#Here an example of how works the amountofscopes in a Python dictionary 
amount_of_elements = 76

amount_scopes = amount_of_elements - 1
print(amount_scopes)
print("-------------")#Indent
    #this print 75


#Aritmetics operators

#plus and rest
plus = 12 + 54
rest = 8 - 68

#multiply and divsion
multiply = 12 * 2
division = 40 / 5

#module
module = 8 % 7
print(module)
print("-------------")#Indent
    #this shows 875

#entire of a number and exponent
entire = 6 // 8
exponent = 2 ** 3
print(entire,exponent)
print("-------------")#Indent
    #this shows 0 and 8
    
#we can see the type info
print(f"your data type is: {type(division)}")
    #*This prints "float".

#Combine excersizes

x = 20
y = 12
z = 31

combine_operation = x + y > z
print(combine_operation)
print("-------------")#Indent
    #*This prints true 
    
#little eccersize
mensual_income = 76
mensual_expense = 23

if mensual_income > 12000:
    print("You are right worldly economically")
    print("-------------")#Indent
    
    if mensual_expense > mensual_income:
        print("Your are rightly going for an economic ruin bro")
        print("-------------")#Indent

    else:
        print("You still fine bro")
        print("-------------")#Indent
    
elif mensual_income > 1200:
    print("You are right in latam")
    print("-------------")#Indent

elif mensual_income > 620:
    print("Your are right in Peru")
    print("-------------")#Indent

elif mensual_income > 320:
    print("You are right in Venezuela")
    print("-------------")#Indent
    
    
#STRING METHODS IN PYTHON

#*Vars for the methods examples:
name_welcome = "Hi!, I'm Angel"
welcome_blessing = "I'm Glad to meet you!"

#*DIR METHOD:

#We can use this python method like a function:
resolution = dir(name_welcome)
print(resolution)
print("-------------")#Indent
#*This show us every single posible method that we can use with our var, that in this example it's called resolution.


#*UPPERCASE METHOD:

#This prints in screen the string value changed to upper:
resolution = welcome_blessing.upper()
print(resolution)
print("-------------")#Indent
    #*This prints "I'M GLAD TO MEET YOU ".

#*LOWER METHOD:

#This prints in screen the string value changed to lower:
resolution = welcome_blessing.lower()
print(resolution)
print("-------------")#Indent
    #*This prints "i'm glad to meet you!".

#CAPITALIZE METHOD

#*This prints in screen the string value changing the first letter to upper:
resolution = name_welcome.capitalize()
print(resolution)
print("-------------")#Indent
    #*This prints "Hi!, i'm angel"

#FIND METHOD:

#*This prints the finded keywork inside our string var:
resolution = name_welcome.find("Hi!")
    #*This prints "0" in screen.

#*Here a little example:

print(resolution[0],resolution[1],resolution[2])
    #*This function works diferent of index, this directly find the key word and show us only the first position were our paramenter start.
    
#*INDEX METHOD:

#Basically this method works like Find:
resolution = name_welcome.index("!")
print(resolution)
print("-------------")#Indent
    #*This prints "10" in screen.

#*For example in this case:

print(resolution[10])
    #*This prints "!" in screen
    

#*ISNUMERIC METHOD:

#Basically this return true if the var were we aply the method it's numeric, and false if it isn't:
resolution = welcome_blessing.isnumeric()
print(resolution)
print("-------------")#Indent
    #*This prints false.


#*ISALPHA METHOD :


#This method work seeing if every char in string is inside a to z chars, if it's right it returns true, if it's not, returns false:
resolution = name_welcome.isalpha()
print(resolution)
print("-------------")#Indent
    #*This prints false
    

#*COUNT METHOD:

#example 1:
resolution = welcome_blessing.count("i")
print(resolution)
print("-------------")#Indent
    #*This show us the amount of i letters inside our string.

#*example 2:
resolution = name_welcome.count("Angel")
print(resolution)
print("-------------")#Indent
    #*This prints "1", because the amount of words called "Angel" is 1.

#*LEN FUNCTION:

#We use this for count how many chars have a string.
resolution = len(name_welcome)
print(resolution)
print("-------------")#Indent
    #*This prints "14".

#*Example:

if resolution == 14:
    
    while resolution > 0:
        
        print(f"There's your element of your pharse: {name_welcome} , number {resolution - 1}:")
        print(name_welcome[resolution-1])
        resolution =- 1
        
#*We can see in the example that the total amount of elements of name welcome is 1 number less because the arrays start to save elements to 0


#*STARTSWITH METHOD:

#*If our string starts with the method's parameter it will return True, if it isn't, returns False:
resolution = name_welcome.startswith("I")
print(resolution)
print("-------------")#Indent
    #*This prins "True".


#*ENDSWITH METHOD:

#*This method returns a true bolean value if the used parameter is equal to last char of chain of chars of the string were we aplied the method:
resolution = name_welcome.endswith("you")
print(resolution)
print("-------------")#Indent
    #*This prints "True"


#*REPLACE METHOD:

#With this method we can replace a piece of a string with other data that we want:
resolution = welcome_blessing.replace("you","u")
print(resolution)
print("-------------")#Indent
    #*This prints   "I'm Glad to meet u!".

#This method works taking the first parameter's value for find a coincidence inside the string were we aplied the method, and if that coincidence exist it will be replaced with the next parameter of the method.


#*SPLIT METHOD:

#Just like in JS this method returns an array with every separate char of a string, it could be an unic position array or an array with the every single char of the string separate.

#*LITTLE CORECTION:well, th explaining isn't 100% wrong, but this method don't return an array, only separate all the elements that have in middle the parameter used in the split() method. 

resolution = name_welcome.split(",")
print(resolution)
    #*This prints resolution divided for ",".

#This method could be used of differents ways, just like separate a string taking like parameter the scopes (",") inside.


#*LISTS METHODS:

#List for work:
liste = ["fa",13,True,2.34,"Palo",12]

#*LIST FUNCTION:

#This method create a list "list()".
resolution = list(["",2,False,90.34,True,2,"Hi","Peter"])
print(resolution)
print("-------------")#Indent

#*Is important see that this function only can take like parameter a list with his new elements inside.

#*TRICK: A good use for this funtion is for create a void list.

#*LITTLE CORRECTION:This method can take like parameter nothing, because by default this method returns a void list.


#*LEN METHOD:

#Just like we use it in string for see the amount of elements inside we use this in lists for see the amount of positions inside

resolution = len(liste)
print(resolution)   
    #*This prints "6".
print("-------------")#Indent


#*APPEND METHOD:

#We use this method for append elements to a list
liste.append(45)
print(liste)
print("-------------")#Indent
    #Now the list have "45" new element
    
    
#*INSERT METHOD:

#This method works inserting info finding the position number inside the first parameter of the method, and then the method insert the info in the next parameter.

liste.insert(2,False)
print(liste)
print("-------------")#Indent
    #This prints the modified list in the 2 position, so the "True" element, changes to "False".
    

#*EXTEND METHOD

#This method let us put many elements at the same time inside a list. It works using like parameter a list with the elements that we want to put inside a list

liste.extend([1,2,"erer",False])
print(liste)
print("-------------")#Indent


#*POP METHOD 

#This method let us delete elements of a list, using his first parameter for find the position of the element that we will delete

liste.pop(-1)

#Curiosly we can access in a negative order for the positions of the array, -1 is the last position, and it will be advaced in a oposed way in the array


#*REMOVE METHOD

#This method find the exactly info of the list position in first parameter inside of the list and remove it:
liste.remove(1)
print(liste)
print("-------------")#Indent
    #*This will prints our list without our 1 element.


#*CLEAR METHOD:

#This method remove all the data inside a list:
listo = [323,"cada",False,True,2.32]
print(f"Entire List: {listo}")
print("-------------")#Indent

listo.clear()
print(f"Void List: {listo}")
print("-------------")#Indent


#*SORT METHOD:

#This a method that only works with number and bolean data list, and sort the number of minus to bigger:
num_list = [34,213,45,24,63,False,True]
print(f"Unsortered List {num_list}")
print("-------------")#Indent

num_list.sort()
print(f"Sortered list {num_list}")
print("-------------")#Indent

#*See too that the "False" list value be sorted in first array´s position, and the "True" list value and then the rest of list.

#*REVERSE METHOD

#This method works sorting the values taking first the bigger number and then the smaller number:
print(f"Unreversed List {num_list}")
print("-------------")#Indent

num_list.reverse()
print(f"Reversed list {num_list}")
print("-------------")#Indent

#*See too that the "False" list value be sorted in last array´s position, then "True" list value and then the rest of list.

#*---------------------------------------------------
#*Is interesting see that his method runs using like first reference the numbers inside the list for sort or reverse the list's order, with sort the boleans of our list will always be first, in reverse our boleans always will been last.
#*---------------------------------------------------

#*TUPLES METHODS:

#*INDEX METHOD:

#This method works for find a specific positions comparing with the first parameter used with the info inside every position for find it.

tuple_ex = (21,3,"Hi",True)
print(f"Your number finded position it's {tuple_ex.index("Hi")}")   

print(tuple_ex.index("Hi"))
    #*This will print "2".
print("-------------")#Indent



#*USEFUL FUNCTION

#*SET FUNCTION:

#This function let use create a set:

print(f"Here's your new set: {set(["Hi","BRea"])}")
print("-------------")#Indent

#It's important to know that we only can remove and extract elements of a set, nothing more.

#*For see this better we can aply "dir()" function for that:
print(dir(set([1.32,242,2*2,1+2,"da",True,False])))
    #This prints all the posible methods with a set.
    
    
    
#*DICT METHODS:

#Example dicts:

example_string_dict = {
    
    'key1':'box_1',
    'key2':'box_2',
    'key3':'box_3',
    'key4':'box_4',
    'key5':'box_5',
    'key6':'box_6',
    'key7':'box_7'
    
}

example_number_dict = {
    
    1:3231,
    2:32,
    3:7465,
    4:93,
    5:534,
    6:2344,
    7:123
    
}

example_erased_dict = {
    
    "bye world":'Bye buddy'
    
}

#*KEYS METHOD:

#This method works taking the key name of a dict.

print(f"Here the keys of your boxes: {example_string_dict.keys()}")
    #This prints every keys of the dict.
    
print("-------------")#Indent

#*This method is useful too for aply it by a iterative way to work with the keys and they info. For example make an array with all the keys.s.


#*GET METHODS:

#This method works taking the data for the key writed in the first parameter.

print(f"Here's your first box: {example_string_dict.get('key1')}")
    #This prints 'box1'.
    
print("-------------")#Indent

#*LITTLE TRICK:

#The correct way of access to a dict it's with get because don't exist the chance that our program could be stopped for an exception.

print(f"Here's your first box: {example_number_dict.get(1)}")
    #This prints "3231".
    
print("-------------")#Indent


#*CLEAR METHOD:

#Just that we know with list, this method delete all inside the dict.

print(f"This dict will be erased: {example_erased_dict}")
    #This prints the entire dict.
    
print("-------------")#Indent

print(f"Know that dict not exist anymore:_ {example_erased_dict}")
    #This prints the void dict.
    
print("-------------")#Indent


#*POP METHOD:

#This method del a single element of a dict using the key name of the element that we want to del.

print(f"Here is your entire dict: {example_number_dict}")
    #This prints the entire list.
    
print("-------------")#Indent

example_number_dict.pop(3)
print(f"This your incomplete dict: {example_number_dict}")
    #This prints the incomplete list.

print("-------------")#Indent

#*ITEMS METHOD:

#Is an iterative method that let us abstract the entire dict and manipulate it with loops:

print(example_string_dict.items())

print("-------------")#Indent



#*DATA INPUTS:


#*INPUT FUNCTION:
#It's a function that let us ask for data to the user and save it in a specific var:

input_prove = input("Give some data bro: ")
print(input_prove)



#*BASIC MID PART COURSE:

#*UNPACKING VARS:

#*This basically means that we can create te access keys of a list with simple info just creating new vars like propertiesfor every single element of that list:

listejs = list(["jshsjsh","jahsjsbs"])
tuluojs,jopo = listejs
print(tuluojs)
    #*this pritns "jshsjsh"

#This works on tuples and sets too:.

loton = (72,726,7273,75273)
hola,papa,tu,como = loton
print(hola)
    #*this printw 72

tuteca = {"jshdu",True,7263,183,82,False}
estas,cuanto,tiempo,verdad,mi,pana,tu = tuteca
print(tiempo)
    #*This prints "7263"

#*NEW FUNCTION
pepes = tuple((7272,7263,7277))
print(pepes)

#With this we can create tuples


#*PACKING VARS 
#We aply the inverse like unpacking vars:

tutle = 72,62,"false",True
print(tutle)
    #*This prints a tuple

#*We can create vars like this, but we are tuples actually

#*For create tuples with a single element we do this:
single_tuple = "pepe",
print(single_tuple)
    #*This prints a tuple

#*FROZENSET FUNCTION:
#*This id basically the way that we can create a set inside a tuple:

prove_set = frozenset([62,62,"hahd"])

unmutable_set = {prove_set,173,"hola",True}

#Basically we only can do this because inside a set we can't put mutable information, so we only can create set with other sets inside using a frozen set 

#*ISSUBSET METHOD:

#This method works with set theory, basically we wiil se if a set have elements of other set, but, if once of them have some elements than other we will call subset the set with less amount of elements.

set_A = {9,6,7,1,98}
set_B = {98,6,7}

resuly = set_B.issubset(set_A)
print(resuly)
    #*This will return "True"

#Other way of do this it's aply this conditions
resuly = set_B <= set_A
print(resuly)
    #*This returns "True"


#*ISSUPERSET METHOD:

#This method works with set theory, basically we wiil se if a set have elements of other set, but, if once of them have some elements than other we will call superset the set with more amount of elements.

resuly = set_A.issuperset(set_B)
print(resuly)
    #*This prints "True"

#*For make the same with logic operators:
resuly = set_A >= set_B
print(resuly)
    #*This prints "True".

#And for check if some set have a different elements inside we have:

#*ISDISJOINT METHOD:

#This will return "True" if no one element in the sets are equal, in the case that at least one element be equal the method will return "False"

resuly = set_A.isdisjoint(set_B)
print(resuly)
    #*This prints "False".

set_C = {2,4,5,56,81}

resuly = set_A.isdisjoint(set_C)
print(resuly)
    #*This prints "True".



#*DICT METHODS 2.0:


#*DICT FUNCTION:

#*This method let us create a dict with the keys and ibfo like this:

new_dict = dict({"tail":123,"head":89})
print(new_dict)
#*This prints the dict

#*NOTE:We can see that we only can create void dicts, void lists and void sets like this:

void_set = set()
void_dict = dict()
void_list = list()
void_tuple = tuple()

print(void_dict, void_set, void_list, void_tuple)
    #*This prints a void set,a void list and a void dict.

#*It's fine to see that we can use tuples like keys of a dict, because the keys cannot be mutable:

prove_dict = {

    ('pepe','reyes'):"hi bro"

}

#*We can use too a frozen set,that is a non mutable element:

frozen_set = frozenset([126,'id'])

prove_dict_two = {

    frozen_set:'Julio'

}


#*FROMKEY METHOD:

#This method works taking in the first parameter an iterable that will be used for define the keys of the dict were we are aplying the method, the second and next parameters works like the value of the keys in first parameter

resulpe = dict.fromkey(['hi','bro'],"Angel","Molina")
print(resulpe)
    #*This prints the dict with the keys and other values.



#*FOR LOOP:

#*In python this loop sybtax work like this:

new_list = [837,827,72,936]


for i in new_list:
    print(i)

#By default our iteration amount will be one by one, so this show us every element inside the list,and will take the element in the position equal to iteration.

#*Exameple:

for num in new_dict:
    resulo = num + 7
    print(resulo)

#ZIP FUNCTION:

#This is for iterate two list with the same amount of elements at the same time:

#*Example:

string_list = ["jsh","ushdh","ksboabd","isjdk"]

for num,stri in zip(string_list,new_list):
    print(num)
    print(stri)

#We can put the range of elements were we want to move inside of our list with for loop:

for num in range(7,10):
    print(num)
    #*This returns 7,8,9
    
#*Little trick for go in an array:a

for num in enumerate(new_list):
    print(num)

#*In this example we can see that the value that return our enumerate function are tuples that they first value are the position lf the list, and the second value are the value in list position.

#*This is very useful because we can acces directly for the index or the value of a list because we can know exactly were we have the info:

#*Here we see index:
for num in enumerate(new_list):
    print(num[0])

#*Here we see value:
for num in enumerate(new_list):
    print(num[1])
    
#*Here a better example for it:

for num in enumerate(new_list):
    print(f"The index it's: {num[0]}")
    print(f"The value it's: {num[1]}")

#*Little code challenge:

for num,i in enumerate(new_list):
    num,i = new_list
    print(num,i)

#*ELSE IN FOR:

#This let us review if our for loop finish, or basically see if the condition of our loop stop of be true:

for i in num_list:
    print(f"Here our nums {i}")
else:
    print(f"your loop it's over")

#*Every single method here works with tuples and sets, except the range function 



#*DICT FOR LOOPS:

#Here we access a dict using the firsr param of our loop for acces for every key inside the dict 

for key in new_dict:
    print(key)


#But this don't works if we want to access keys and values we will use "items()" method for that:

for keys in new_dict.items():
    key = keys[0]
    value = keys[1]
    print(f"Your key is {key}")
    print(f"Your value is {value}")

#*This way return a tuple with the key and value of every part of the dict


#*INTERESTING NEW TRICK:

#*Here we have a way for make exceptions in our elements iteration with for loops we can use an if continue for that:

for i in new_list:
    if i == new_list[0]:
      continue
    print(i)


#*OTHER TRICK:

#*We have other way were we can stop our loop if some specific condition it's True:

for ia in new_list:
    print(ia)
    if i == new_list[1]:
      break 

print(f"Your loop it's over")

#*We iterate our for loop to the second element of our list.


#*Manipulating strings with for loops:

#*We Only will works exactly like a list:

for char in string_list:
    print(char)


#*NEW INTERESTING TRICK:

#We could see that we can manipulate directly all the elements of a list with a for:

for io in new_list:
    print(io*2)

#*In this case we are dupling the values

#*But here we have other way for that

new_list_two = [x*2 for x in new_list]

#*How we do this: We only use x like an expression for manipulate the iteration x element were we'll change, in this case the new list two.

#*Take in count that we only can do this with simple things 




#*WHILE LOOPS:

#*The syntax is something like this:

i = 0 

while i != 10:
    i + 1



#*BUILT-IN FUNCTIONS:

#The built in functions are the normal functions that python have by default, just like "type()", "enumerate()" or "list()"

#*It's important to see that in python we have the abstraction concept, that basically is were we know how a function affect our program and whst have to do we don't really know how works out program

#*New interesting built-in functions:

#*Max and Min functions:

max_number = max(new_list)
print(max_number)
    #*This function works finding the highest number in one iterable