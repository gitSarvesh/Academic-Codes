
def insert(hash_table, value):
    keyvalue = hash_func(value)
    if(hash_table[keyvalue]==[]):
        hash_table[keyvalue] = value
    else:
        i = keyvalue+1
        if(i<m):
            for i in range(keyvalue+1, m):
                if(hash_table[i]==[]):
                    hash_table[i] = value
                    break
        else:
            for i in range(0, keyvalue + 1):
                if(hash_table[i]==[]):
                    hash_table[i] = value
                    break
                    
def hash_func(value):
    return value % m
    
def doubHashing(value, i):
    h1 = value % m
    h2 = 7 - (value % 7)
    h = (h1 + (i*h2)) % m
    return h
    
def doubInsert(hash_table, value, i):
    if(hash_table[doubHashing(value, i)] == []):
        hash_table[doubHashing(value, i)] = value
    else:
        i+=1
        doubInsert(hash_table, value, i)
    
def display():
    print(hash_table)
    
def search(hash_table):
    key = int(input("Enter number you want to search : "))
    if(hash_table[hash_func(key)] == key):
        print(key, " Found")
    else:
        i = hash_func(key)+1
        if(i<m):
            for i in range(hash_func(key)+1, m):
                if(hash_table[i] == key):
                    print(key, " Found")
                    break
        else:
            for i in range(0, hash_func(key) + 1):
                if(hash_table[i] == key):
                    print(key, " Found")
                    break
        
def main():    
    print("1.Linear Probing /n2.Double Hashing")
    ch = int(input("Enter choice for Hashing Technique : "))
    if(ch == 1):
        print("1.Insert /n2.Display /n3.Search/n")
        c = int(input("Enter Choice of Operation : "))
        if(c == 1):
            n = int(input("Enter number of elements to be inserted : "))
            for i in range(n):
                value = int(input("Enter value : "))
                insert(hash_table, value)
        elif(c == 2):
            display()
        elif(c == 3):
            search(hash_table)
        else:
            print("Enter valid choice ")
    elif(ch == 2):
        print("1.Insert /n2.Display /n3.Search/n")
        c = int(input("Enter Choice of Operation : "))
        if(c == 1):
            n = int(input("Enter number of elements to be inserted : "))
            for i in range(n):
                value = int(input("Enter value : "))
                doubInsert(hash_table, value, 0)
        elif(c == 2):
            display()
        elif(c == 3):
            search(hash_table)
        else:
            print("Enter valid choice ")
    else:
        print("Enter valid choice ")

m = int(input("Enter Table Size : "))
hash_table=[[] for _ in range(m)]
main()
