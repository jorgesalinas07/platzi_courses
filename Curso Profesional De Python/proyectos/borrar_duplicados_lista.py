def remove_duplicates(some_list):
    without_duplicates=[]
    for element in some_list:
        #Not in significa: si el elemento no esta en la lista "without_duplicates"
        #La lista "without_duplicates" va ir almacenando los valores que no están repetidos
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates
    
def run():
    random_list=[1,1,2,2,4,"caballo","caballo"]
    print(remove_duplicates(random_list))

if __name__=="__main__":
    run()