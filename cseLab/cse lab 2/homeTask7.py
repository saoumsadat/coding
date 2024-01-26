var1 = False
var2 = False
var3 = False
var4 = False
var5 = False
var6 = False
result1 = False
result2 = False
result3 = False
result4 = False
result5 = False
result6 = False
result7 = False
result8 = False
result9 = False
result10 = False
var1 = ((not True) or True) and False   #False
var2 = var1 and False   #False
var3 = True and not False   #True
var4 = False
var5 = True
var6 = var3 and False   #False
result1 = (var1 and var2) and (40 % 3) > 45 or (var5 and var6)  #False
#(False and False) and False or (True and False)
#False and False or False = False
result2 = (var1 or var2) or (result1 and False) #False
#False or False = False
result3 = (var1 and result1) or result2 or var5 #True
#False or False or True = True
result4 = (var1 or var2) or ((var3 and var1) and False) #False
#False or False = False
result5 = (var1 and var2) and (result3 or var1) #False
#False and True = False
result6 = ((var3 or (not var2)) and (result5)) or True  #True
#True
result7 = (var4 and result1) and ((result1 and False) or True)  #False
result8 = ((var1 and result3) and ((not var5) or var6)) and True    #False
result9 = ((result2 and var2) or ((not result7) and var1)) and not False  #False  
result10 = not(var1 and True)   #True

print("var1:", var1)
print("var2:", var2)
print("var3:", var3)
print("var4:", var4)
print("var5:", var5)
print("var6:", var6)
print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
print("result5:", result5)
print("result6:", result6)
print("result7:", result7)
print("result8:", result8)
print("result9:", result9)
print("result10:", result10)

