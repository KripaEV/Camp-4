#phonebook dictionary
phonebookdict={"JKL":34567,"ABC":12345,"DEF":98765}

from collections import OrderedDict 
def sort():
    for i in sorted(phonebookdict):
        print(i,phonebookdict[i])

def add():
    newname=input("Enter the new name:")
    newno=input("Enter the new phone no:")
    newdict={newname:newno}
    phonebookdict.update(newdict)
    print(phonebookdict)

def delete():
    delname=input("Enter the name to be deleted:")
    del phonebookdict[delname]
    print(phonebookdict)

def searchname():
    flag=0
    sname=input("Enter the name to search:")
    for name,no in phonebookdict.items():
        if sname==name:
            print("Name:",sname,"\nPhone no:",phonebookdict.get(sname))
            flag=1
    if(flag!=1):
        print("Record not found")

def searchno():
    flag=0
    sno=int(input("Enter the no to search:"))
    for name,no in phonebookdict.items():
        if sno==no:
            print("Name:",name,"\nPhone no:",sno)
            flag=1 
            break
    if flag!=1:
        print("Record not found")


while(1):
    print('''
    1.List all contacts
    2.Add a new content 
    3.Delete a contact
    4.Search by name
    5.Search by number
    6.Exit''')
    ch=input("Enter your choice:")
    match(ch):
        case '1':
            print(sort())
        case '2':
            print(add())
        case '3':
            print(delete())
        case '4':
            print(searchname())
        case '5':
            print(searchno())
        case '6':
            break