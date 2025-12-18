var = 'Marius are pere'
# print(var[0]) # ------> M
# print(var[1]) # ------> a
# print(var[-1]) # ------> e
# print(var[-2]) # ------> r
# print(var[-3]) # ------> e
# print(var[-4]) # ------> p

print (var[-4::1]) # -------> pere
print (var[0:5:1]) # -------> Marius

var1 = var[7:10] # or var1 = var[7:10:1]
print(var1) # -------> are