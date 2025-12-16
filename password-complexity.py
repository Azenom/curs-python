# # long analitical version
# ---------------------------------------- 
# # create list for special characters
# pool_special = [ '!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , ',' , '-' , '.' , '/' , ':' , ';' , '<' , '=' , '>' , '?' , '@' , '^' , '_' , '' , '|' , '~' ]

# # create list for letters
# pool_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

# # create list for digits
# pool_digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

# # ask user to enter the password following the mentioned rules
# print("The password's lenght must be grater than 10 and contain at least one letter, one special character and one digit")
# password = input('Type your password : ')

# # the key varriable turns true if the password meet the requirements
# # start the loop as if the password doesn't meet the requirements
# key = False
# flag_special = False
# flag_letters = False
# flag_digits = False
# flag_len = False

# while key == False :    
#     for p in password :
#         for s in pool_special :
#             if s == p :
#                 flag_special = True
#                 break
#         for l in pool_letters :
#             if l == p or l.upper() == p :
#                 flag_letters = True
#                 break
#         for d in pool_digits :
#             if d == p :
#                 flag_digits = True
#                 break
#     if len(password) > 9 :
#         flag_len = True
#     if flag_special and flag_letters and flag_digits and flag_len :        
#         key = True
#     else :
#         # print status to check and reset all flags in order to avoid partial checks
#         print ('Special :', flag_special, 
#                '---- Letter :',flag_letters, 
#                '---- Digits :', flag_digits, 
#                '---- Length :', flag_len)
#         flag_special = False
#         flag_letters = False
#         flag_digits = False
#         flag_len = False
#         print('Requirements not met ')
#         password = input('Re-Type your password : ')

# if key == True :
#     print('Your password is : ' + password)
# else :
#     print('Errrrr.....')
# ----------------------------------------

# # optimised version
# ---------------------------------------- 
# def password_check(password) :
#     if len(password) < 9 :
#         print ('Not long enough')
#         return False
    
#     big = any(c.isupper() for c in password)
#     small = any(c.islower() for c in password)
#     digit = any(c.isdigit() for c in password)
#     alfanum = any(not c.isalnum() for c in password)

#     return all([big, small, digit, alfanum])

# password = input ("Enter password : ")

# if password_check(password) :
#     print("All good ✅ : ", password)
# else:
#     print("Not good enough ❌")
# ----------------------------------------