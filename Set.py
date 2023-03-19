def create():
    global set1
    set1 = set()
    n = int(input("Enter total number of elements in the set Set1 : "))
    for i in range(n):
        x = int(input("Enter element : "))
        set1.add(x)
    print("Given set Set1 is : ", set1)

def Add():
    n = int(input("Enter total number of elements to be added in the Set1 : "))
    for i in range(n):
        x = int(input("Enter element : "))
        set1.add(x)
    print("New set Set1 is : ", set1)

def Remove(key):
    if(len(set1)==0):
        print("The set Set1 is empty ")
    elif(key in set1):
        set1.remove(key)
    else:
        print(key, " is not present in the set Set1 ")

def size():
    print("Size of the set Set1 is : ", len(set1))

def search(key):
    flag = 0
    for i in set1:
        if (key in set1):
            flag = 1
        else:
            flag = 0
    if(flag == 1):
        print(key, "is present in the set Set1 ")
    else:
        print(key, "is not present in the set Set1 ")
    
def Union():
    global union
    union = set1
    global set2
    set2 = set()
    n = int(input("Enter total number of elements in the set Set2 : "))
    for i in range(n):
        x = int(input("Enter element : "))
        set2.add(x)
    print("Given set Set2 is : ", set2)
    for i in set2:
        if(i not in union):
            union.add(i)
    print("Union of the two sets Set1 and Set2 is : ", union)

def Ints():
    global ints
    ints = set1.intersection(set2)
    # for i in set2:
    #     if(i in set1):
    #         ints.add(i)
    print("Intersection of the two sets Set1 and Set2 is : ", ints)

def Symdif():
    symdif = set()
    for i in union:
        if(i not in ints):
            symdif.add(i)
    print("Symmettric Difference of the two sets Set1 and Set2 is : ", symdif)

def Sub():
    sub = union
    for i in set2:
        if(i in union):
            sub.remove(i)
    print("Subtraction of the two sets Set1 and Set2 is : ", sub)

def main():
    create()
    Add()
    a = int(input("Enter element to be deleted : "))
    Remove(a)
    key = int(input("ENter element you want to search : "))
    search(key)
    size()
    Union()
    Ints()
    Symdif()
    Sub()
main()