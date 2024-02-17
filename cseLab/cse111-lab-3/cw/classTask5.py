import math

# Driver Code
# Subtask 1: Write the CellPackage Class
class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback, validity):
        self.data = int(data.split(' ')[0]) * 1024
        self.talk_time = talk_time
        self.messages = messages
        self.validity = validity
        self.price = price
        self.cashback = math.floor((int(cashback[0:-1]) / 100) * price)

        # if self.data != 0: print(f"Data = {self.data} MB")
        # if self.talk_time != 0: print(f"Talktime = {self.talk_time} Minutes")
        # if self.messages != 0: print(f"SMS/MMS = {self.messages}")
        # if self.validity != 0: print(f"Validity = {self.validity} Days")
        # if self.price != 0: print(f"--> Price = {self.price} tk")
        # if self.cashback != 0: print(f"Buy now to get {self.cashback} tk cashback.")

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('===========Package 1=============')
# Subtask 2: Check each attribute and print
if pkg.data != 0: print(f"Data = {pkg.data} MB")
if pkg.talk_time != 0: print(f"Talktime = {pkg.talk_time} Minutes")
if pkg.messages != 0: print(f"SMS/MMS = {pkg.messages}")
if pkg.validity != 0: print(f"Validity = {pkg.validity} Days")
if pkg.price != 0: print(f"--> Price = {pkg.price} tk")
if pkg.cashback != 0: print(f"Buy now to get {pkg.cashback} tk cashback.")

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('===========Package 2=============')
# Subtask 3: Check each attribute and print
if pkg2.data != 0: print(f"Data = {pkg2.data} MB")
if pkg2.talk_time != 0: print(f"Talktime = {pkg2.talk_time} Minutes")
if pkg2.messages != 0: print(f"SMS/MMS = {pkg2.messages}")
if pkg2.validity != 0: print(f"Validity = {pkg2.validity} Days")
if pkg2.price != 0: print(f"--> Price = {pkg2.price} tk")
if pkg2.cashback != 0: print(f"Buy now to get {pkg2.cashback} tk cashback.")

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============Package 3============')
# Subtask 4: Check each attribute and print
if pkg4.data != 0: print(f"Data = {pkg4.data} MB")
if pkg4.talk_time != 0: print(f"Talktime = {pkg4.talk_time} Minutes")
if pkg4.messages != 0: print(f"SMS/MMS = {pkg4.messages}")
if pkg4.validity != 0: print(f"Validity = {pkg4.validity} Days")
if pkg4.price != 0: print(f"--> Price = {pkg4.price} tk")
if pkg4.cashback != 0: print(f"Buy now to get {pkg4.cashback} tk cashback.")
