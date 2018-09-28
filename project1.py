'''
Created on Sep 26, 2018

@author: Lucas sadoulet
'''
name=input(str('What is your name?'))
phone=input(str('What is your phone number?'))
product=input(str('What do you want?'))
many=int(input('How many do you want?'))
cost=float(input('What is the cost?'))
money=cost*many
tax=money*0.06
print('''Name:''',name,'''
Contact:''',phone,'''
Purchase Information

Product:''',product,'''   Qty:''',many,'''   Product Cost: $''',cost,'''

Cost: $''',money,'''   Tax: $''',tax,'''   Final cost: $''',tax+money,)