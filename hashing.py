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