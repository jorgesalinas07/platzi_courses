


def discard_duplicates(list):
    my_set=set(list)
    return(my_set)



def run():
    my_list=[1,1,2,2,3,3,4,4,"burro","burro",True, True, False, False, "Hola","Hola"]
    print(discard_duplicates(my_list))


if __name__=="__main__":
    run()