var1 = var2 = True
var3 = var4 = var5 = False
result1 = result2 = result3 = True
result4 = result5 = False
var1 = 4 > 3 - 1    #4 > 2 = True
var2 = False and var1   #False and True = False
var3 = True
var4 = False
var5 = not(var3 or var4)    #not(True or False) = not(True) = False
result1 = (var1 or var2) and (8 * 10 > 45)  #(True or False) and (80 > 45) = True and True = True
result2 = (var1 or var2) and (result1 and False)    #(True or False) and (False and False) = False
result3 = (var1 and not result1) or result2 #(True and not False) or False = (True and False) or False = False or False = False
result4 = (var1 or var2) or not((var5 and var1) and False)  #(True or False) or not((False and True) and False) = True or not(False and False) = True or True = True
result5 = (not var1 and var4) and (result3 or var3) #(not True and False) and (True or True) = (False and False) and (True) = False and True = False

print(result1, result2, result3, result4, result5)