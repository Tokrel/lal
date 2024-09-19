def create_chocolate_bar(a, b):
    chocolate_bar = []
    for i in range(1, a + 1):
        rad = []
        for c in range(1, b + 1): 
            rad.append(f"{i}{c}")  
        chocolate_bar.append(rad)
    return chocolate_bar



def  print_chocolate_bar(a):
    for i in range(len(a)):
        print(" ".join(a[i]))



def chomp(list,rad,kolumn):
    for i in range(rad, len(list)):
            del list[i][kolumn:] 
    return list


