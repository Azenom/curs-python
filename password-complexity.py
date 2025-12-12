# create list for special characters
pool_special = [ '!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , ',' , '-' , '.' , '/' , ':' , ';' , '<' , '=' , '>' , '?' , '@' , '^' , '_' , '' , '|' , '~' ]

# create list for alfa numeric charcters
pool_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

# ask the user to enter the password following the mentioned rules
print('The password must contain at least one letter, special character, numer and the lenght grater than 10 characters in total ')
password = input('Type your password : ')

# the key varriable turns true if the password meets the minimium requirements
# start the loop as if the password meets the requirments
key = True
while key == True :
    if len(password) <= 9 :
        print('Password too short !!! ')
        password = input('Type your password : ')
        key = False
    else :
        for c in password :
            for i in pool_special :
                if i != c :
                    print ("There's no special characters")
                    password = input('Type your password : ')
                    key = False
                else :
                    for x in pool_letters:
                        if x != c & x != c.upper() :
                            print ("There's no letter")
                            password = input('Type your password : ')
                            key = False
                        else :
                            print('Your password is : ' + password)
                            key = True


