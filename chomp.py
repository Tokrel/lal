def create_chocolate_bar(rader, kolumnner):
    chocolate_bar = []
    for i in range(1, rader + 1):
        rad = []
        for c in range(1, kolumnner + 1): 
            if i == 1 and c == 1:
                rad.append("P ")
            else:
                rad.append(f"{i}{c}")  
        chocolate_bar.append(rad)
    return chocolate_bar

def  print_chocolate_bar(chocholate_bar):
    for i in range(len(chocholate_bar)):
        print(" ".join(chocholate_bar[i]))



def chomp1(chocholate_bar,rad,kolumn):
    for i in range(rad, len(chocholate_bar)):
            del chocholate_bar[i][kolumn:] 
        
    return chocholate_bar

def chomp(chocholate_bar, rad, kolumn):
    for i in range(rad, len(chocholate_bar)):
        chocholate_bar[i] = chocholate_bar[i][:kolumn]

    chocholate_bar = [row for row in chocholate_bar if row]  
    return chocholate_bar

 
def check_winner(chocholate_bar):
     return len(chocholate_bar) == 1 and len(chocholate_bar[0]) == 1 and chocholate_bar[0][0] == "P "

def ask_cell_number(chocholate_bar):
    try:
        cell_ask = (input("välj en ruta: ")) 
        for index, element in enumerate(chocholate_bar):
            if cell_ask in element:
              return index, element.index(cell_ask) 
        raise ValueError
    except:
         print("Fel val, ruta", cell_ask, "finns inte i spelplanen, försök igen!")
         return ask_cell_number(chocholate_bar)
          
        
print("Välkommen till spelet Chomp.", end="\n")

print("Instruktioner: I spelet kommer du utmanas om att välja ett blocknummer från spelplanen. Det valda blocket och")
print("alla block under och till högre kommer att raderas. Spelet går ut på att undvika välja P, den spelare som väljer P ")
print("förlorar och den andra spelare vinner.", end="\n")

print("Välkommen till spelet Chomp.", end="\n")

rad = int(input("Hur många rader ska chokladbaren bestå av (mellan 2-9):"))
kolumn = int(input("Hur många kolumner ska chokladbaren bestå av (mellan 2-9): "))

spelplan = create_chocolate_bar(rad,kolumn)

print_chocolate_bar(spelplan)
while True:
    print("första spelarens tur, välj ett blocknummer:")
    a, col = ask_cell_number(spelplan)
    spelplan = chomp(spelplan,a,col)
    print_chocolate_bar(spelplan)  
    if check_winner(spelplan):
        print("Spelet är slut, Vinnare är första spelaren!")
        break
    
    print("andra spelarens tur, välj ett blocknummer:")
    a, col = ask_cell_number(spelplan)
    spelplan = chomp(spelplan,a,col)
    print_chocolate_bar(spelplan)  
    if check_winner(spelplan):
        print("Spelet är slut, Vinnare är andra spelaren!")
        break