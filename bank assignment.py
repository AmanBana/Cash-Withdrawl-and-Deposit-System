#!/usr/bin/env python
# coding: utf-8

# In[1]:


ba=['ravi','aman','anshul','lavina']
bb=[10000,15000,8000,13000]
user=input("enter your name :")
if user in ba:
    user_index=ba.index(user)
    print("holder account name:",user)
    print('holder account'+str(user_index))
    print('account balance',bb[user_index])
    print("account is active")
    print("please enter correct input below for deposit or withdrwal")
    operation=input('D for deposit and w for withdraw')
    if operation=="D" or operation=="d":
        depositamount=int(input("enter your amount"))
        bb[user_index]=bb[user_index]+depositamount
    print("my updated balance is"+str(bb[user_index]))
    if operation=="W" or operation=="w":
        withdrawlamount=int(input('enter your amount'))
        if withdrawlamount > bb[user_index]:
            print("your account doesn't have sufficient balance")
        else:
            print("my updated balance is"+str(bb[user_index]-withdrawlamount))
else:
    print("your account does not exist")


# In[ ]:




