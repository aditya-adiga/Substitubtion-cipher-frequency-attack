# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:31:26 2021

@author: Aditya Adiga
"""
def find_key(encoded_text):
    freq={}
    dkey={}
    count=0
    sum=0
    characters='etaoinsrhdlucmfywgpbvkxqjz'
    for i in "".join(encoded_text.split()):
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1
    res = {key: val for key, val in sorted(freq.items(), key = lambda ele: ele[1], reverse = True)}
    for i in res:
        dkey[i]=characters[count]
        count+=1
    dkey[' ']=' '
    dkey['.']='.'
    dkey[',']=',' 
    dkey['\n']='\n'    
    return dkey
def change_key(dkey):
    change=input("enter the letter in the decoded text that you want to change:")
    letter=input("enter the letter you want to change it with:")
    for i in dkey:
        if(dkey[i]==change):
            a=i
        if(dkey[i]==letter):
            b=i
    try:
        dkey[a]=letter
        dkey[b]=change
    except UnboundLocalError:
        dkey[a]=letter
        
    return dkey
def decoded_message(encoded_text,key):
    decrypted_message=''
    for i in encoded_text:
        decrypted_message+=(key[i])
    return decrypted_message
encoded_text=input("Enter the text that you want to decode")
dkey=find_key(encoded_text)
print(dkey)
print(decoded_message(encoded_text,dkey))
change=input("enter anything to change the key on the basis of manual analysis or press 0 to stop:")
while(change!=0):
    dkey=change_key(dkey)
    print("after changing the key text looks like:")
    print(decoded_message(encoded_text,dkey))
    change=input("enter anything to change the key on the basis of manual analysis or press 0 to stop:")

    