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

def search(hash_table):
    key = int(input("Enter number you want to search : "))
    if(hash_table[doubHashing(key)] == key):
        print(key, " Found")
    else:
        i = doubHashing(key)+1
        if(i<m):
            for i in range(doubHashing(key)+1, m):
                if(hash_table[i] == key):
                    print(key, " Found")
                    break
        else:
            for i in range(0, doubHashing(key) + 1):
                if(hash_table[i] == key):
                    print(key, " Found")
                    break

def display():
    print(hashTable)

def main():
        print("1.Insert /n2.Display /n3.Search/n")
        c = int(input("Enter Choice of Operation : "))
        if(c == 1):
            n = int(input("Enter number of elements to be inserted : "))
            for i in range(n):
                value = int(input("Enter value : "))
                doubInsert(hashTable, value, 0)
        elif(c == 2):
            display()
        elif(c == 3):
            search(hashTable)
        else:
            print("Enter valid choice ")

m = int(input("Enter Table Size : "))
hashTable = [[] for _ in range(m)]
main()