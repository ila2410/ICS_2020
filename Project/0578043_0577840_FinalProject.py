"""

1) Plan du magasin

Requis :
    - Coordonnées des Borders (magasin supposé rectangulaire)
    - Coordonnées des Shelves
    - Coordonnées des Entrys
    - Possiblement autres détails (de quel(s) côté(s) donnent les Shelves?)

2) Dictionnaire correspondant au supermarché

Requis :
    - Nom de l'Food
    - Catégorie
    - Prix
    - Localisation
    
3) Création du plan du magasin dans une interface visuelle

Tâches :
    - Tracer contour
    - Tracer Shelves
    
4) Création d'une liste de produits dans une interface visuelle
    
Tâches :
    - Trier par catégorie
    - Afficher les informations utiles du produit
    - Fonction de recherche
    
5) Création d'une liste de courses à partir de wi liste des produits
    
Tâches :
    
    

n) Calcul du chemin le plus court

"""

from tkinter import Tk, Canvas
from random import *

"""

"""

""" The following fonctions are here to help us to make random situations """

def Border_Creation(length, width):
    return [[2.5, 2.5],[length, width]]

def Entry_Creation(length, width):
    a = randint(1, 2)
    b = randint(1, 2)
    if (a == 1):
        le = randint(int(width/6), int(width/4))
        e = randint(le, width - 2*le)
        if (b == 1):
            return [[2.5, e],[2.5, e + le]]
        elif (b == 2):
            return [[length, e],[length, e + le]]
    elif (a == 2):
        le = randint(int(length/10), int(length/7))
        e = randint(le, length - 2*le)
        if (b == 1):
            return [[e, 2.5],[e + le, 2.5]]
        elif (b == 2):
            return [[e, width],[e + le, width]]
    return []

def Shelves_Creation(length, width, number_of_shelves_by_length, number_of_shelves_by_width, shelves_length, shelves_width):
    h_la = (width - 6 - number_of_shelves_by_width*shelves_width)/(number_of_shelves_by_width + 1)
    h_lo = (length - 6 - number_of_shelves_by_length*shelves_length)/(number_of_shelves_by_length + 1)
    Shelves_List = []
    for wi in range(number_of_shelves_by_width):
        for le in range(number_of_shelves_by_length):
            Shelves_List.append([[(le+1)*h_lo + le*shelves_length, (wi+1)*h_la + wi*shelves_width],
                                 [(le+1)*h_lo + (le+1)*shelves_length, (wi+1)*h_la + wi*shelves_width],
                                 [(le+1)*h_lo + (le+1)*shelves_length, (wi+1)*h_la + (wi+1)*shelves_width],
                                 [(le+1)*h_lo + le*shelves_length, (wi+1)*h_la + (wi+1)*shelves_width]])
    return Shelves_List

def Stand_Creation(length, width, Entrance):
    size = [randint(75,125), randint(15,25)]
    r = randint(1,4)
    if (r == 1):
        l = randint(10, width - size[0] - 10)
        while (Entrance[0][1] < l < Entrance[1][1] or Entrance[0][1] < l + size[0] < Entrance[1][1]):
            l = randint(10, width - size[0] - 10)
        return [[5.5,l],[5.5 + size[1],l],[5.5 + size[1],l + size[0]],[5.5,l + size[0]]]
    if (r == 2):
        l = randint(10, width - size[0] - 10)
        while (Entrance[0][1] < l < Entrance[1][1] or Entrance[0][1] < l + size[0] < Entrance[1][1]):
            l = randint(10, width - size[0] - 10)
        return [[length - size[1] - 3,l],[length - 3,l],[length - 3,l + size[0]],[length - size[1] - 3,l + size[0]]]
    if (r == 3):
        l = randint(10, length - size[0] - 10)
        while (Entrance[0][0] < l < Entrance[1][0] or Entrance[0][0] < l + size[0] < Entrance[1][0]):
            l = randint(10, length - size[0] - 10)
        return [[l,5.5],[l + size[0],5.5],[l + size[0],5.5 + size[1]],[l,5.5 + size[1]]]
    if (r == 4):
        l = randint(10, length - size[0] - 10)
        while (Entrance[0][0] < l < Entrance[1][0] or Entrance[0][0] < l + size[0] < Entrance[1][0]):
            l = randint(10, length - size[0] - 10)
        return [[l,width - size[1] - 3],[l + size[0],width - size[1] - 3],[l + size[0],width - 3],[l,width - 3]]
    

def Random_Food_Position_Assignment(Shelves):
    r = randint(0,len(Shelves)-1);
    s = randint(0,1)
    l = randint(1,9)
    position = [Shelves[r][0][0] + (l/10)*(Shelves[r][1][0] - Shelves[r][0][0]),
                Shelves[r][0][1] + (s/2 + 0.25)*(Shelves[r][2][1] - Shelves[r][1][1])]
    return position

def Random_FoodList_Position_Assignment(Shelves, number_of_feeds):
    Positions_List = []
    for k in range(number_of_feeds):
        Positions_List.append(Random_Food_Position_Assignment(Shelves))
    return Positions_List

def Datalist_Creation(Food_List, Shelves):
    Positions_List = Random_FoodList_Position_Assignment(Shelves, len(Food_List))
    Data_List = {}
    Data_List['Food_List'] = Food_List
    Data_List['Positions_List'] = Positions_List
    return Data_List
    
def Random_Situation(Food_List):
    le = randint(600,1200) #Length of the map
    wi = randint(400,600) #Width of the map
    sh_nb_le = randint(2,4) #Number of shelves by length
    sh_nb_wi = randint(5,12) #Number of shelves by width
    sh_wi = randint(12,12) #Witdh of the shelves
    sh_le = randint(int((1/2)*le/sh_nb_le), int((3/4)*le/sh_nb_le)) #Length of the shelves
    Borders = Border_Creation(le, wi)
    Entrance = Entry_Creation(le, wi)
    Stand = Stand_Creation(le, wi, Entrance)
    Shelves = Shelves_Creation(le, wi, sh_nb_le, sh_nb_wi, sh_le, sh_wi)
    Data_List = Datalist_Creation(Food_List, Shelves)
    return [le, wi, Borders, Entrance, Shelves, Stand, Data_List]

""""""

def Borders_Display(Borders, canvas): #To display the borders
    canvas.create_rectangle(Borders[0][0], Borders[0][1], Borders[1][0], Borders[1][1], width=5)
    
def Entry_Display(Entrance, canvas): #To display the Entrance
    canvas.create_line(Entrance[0][0], Entrance[0][1], Entrance[1][0], Entrance[1][1], width=5, fill='red')

def Shelves_Display(Shelves, Stand, canvas): #To display the shelves
    index_bad_shelves = []
    for r in range (len(Shelves)): #We first verify if the shelves to be created won't overlap with the stand
        c = 0
        if (Stand[0][0] < Shelves[r][0][0] < Stand[2][0] and Stand[0][1] < Shelves[r][0][1] < Stand[2][1]):
            c = 1
        elif (Stand[0][0] < Shelves[r][1][0] < Stand[2][0] and Stand[0][1] < Shelves[r][1][1] < Stand[2][1]):
            c = 1
        elif (Stand[0][0] < Shelves[r][2][0] < Stand[2][0] and Stand[0][1] < Shelves[r][2][1] < Stand[2][1]):
            c = 1
        elif (Stand[0][0] < Shelves[r][3][0] < Stand[2][0] and Stand[0][1] < Shelves[r][3][1] < Stand[2][1]):
            c = 1
        elif (Shelves[r][0][0] < Stand[3][0] and Shelves[r][1][0] > Stand[2][0] and Stand[0][1] < Shelves[r][0][1] < Stand[2][1]):
            c = 1
        elif (Shelves[r][3][0] < Stand[0][0] and Shelves[r][2][0] > Stand[1][0] and Stand[0][1] < Shelves[r][2][1] < Stand[2][1]):
            c = 1
        if c == 1: #If one of the conditions is met, that means the shelves will overlap the stand, so we fill a list with the indexes of the bad shelves
            index_bad_shelves.append(r)
    for ind in range(-1, -len(index_bad_shelves) - 1, -1): #And we delete all the associated shelves
        del Shelves[index_bad_shelves[ind]]
    for r in range (len(Shelves)):
        if (Shelves[r][1][0] - Shelves[r][0][0] > Shelves[r][2][1] - Shelves[r][0][1]):
            canvas.create_rectangle(Shelves[r][0][0], Shelves[r][0][1], Shelves[r][1][0], Shelves[r][0][1] + 0.5*(Shelves[r][2][1] - Shelves[r][0][1]), fill='light grey')
            canvas.create_rectangle(Shelves[r][0][0], Shelves[r][0][1] + 0.5*(Shelves[r][2][1] - Shelves[r][0][1]), Shelves[r][1][0], Shelves[r][2][1], fill='light grey')
        else: #This second case is useless here, it was to make the shelves in another direction
            canvas.create_rectangle(Shelves[r][0][0], Shelves[r][0][1], Shelves[r][0][0] + 0.5*(Shelves[r][1][0] - Shelves[r][0][0]), Shelves[r][2][1], fill='light grey')
            canvas.create_rectangle(Shelves[r][0][0] + 0.5*(Shelves[r][1][0] - Shelves[r][0][0]), Shelves[r][0][1], Shelves[r][1][0], Shelves[r][2][1], fill='light grey')
            
def Stand_Display(Stand, canvas): #To display the stand
    canvas.create_rectangle(Stand[0][0], Stand[0][1], Stand[2][0], Stand[2][1], fill='darkslateblue')


def Map_Display(Borders, Entrance, Shelves, Stand, canvas): #To display all the things created
    Borders_Display(Borders, canvas)
    Entry_Display(Entrance, canvas)
    Stand_Display(Stand, canvas)
    Shelves_Display(Shelves, Stand, canvas)
    
def Food_Display(Food, Données, canvas): #To display the selected food on the map
    ind = Données['Food_List'].index(Food)
    x, y = Données['Positions_List'][ind][0], Données['Positions_List'][ind][1]
    location = Données['Positions_List'][ind]
    canvas.create_rectangle(x-2, y-2, x+3, y+3, fill='red', width=0)
    
def FoodList_Display(Liste_Courses, Données, canvas): #To display all the feeds from a list on the map
    for Food in Liste_Courses:
        Food_Display(Food, Données, canvas)
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""HERE ARE THE FONCTIONS FOR THE OTHER WINDOW"""


"""Creating the function which will be called when we click on the main window button"""

def shopping():
    
    #Creating the graphic interface for the shopping list window
    r= Toplevel()
    ff=Frame(r)
    ff.pack()
    
    #Creating the button of the shopping list window
    widget = Button(ff, text = "submit your shopping list", command = creatingshoppinglist, bg = "green2")
    widget.pack(expand=YES, fill=X)
    
    #Deciding on the dimensions of the windows and widgets and positionning them
    W=500
    H=2400
 
    canvas=Canvas(ff, width=W, scrollregion =(0, 0, 10, H), bg='ivory')
    canvas.pack(side=LEFT)
     
    frame = Frame(canvas)
    frame.pack()
           
    #Creating and positionning the scrollbar of the shopping list window
    vbar=Scrollbar(ff,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas['yscrollcommand']=vbar.set      
    canvas.create_window((0,0),window=frame,width=W, height=H, anchor='nw')
 
    #Creating the checkbuttons
    #We travel across the food list to create one checkbutton per food
    for item in Food_List:
        
        #Using the special type which is needed for variable
        var = IntVar()
        
        #Creating each checkbutton
        Checkbutton(frame, text=item,
         variable=var).pack()
        
        #Completing the list which will take every checkbox
        vars.append(var)

"""Creating the function which converts the checkbuttons in values and which
create a list with all the checkbuttons which are checked"""

def creatingshoppinglist():
    
    #Initializing the counter
    j=0
    
    #Making the loop to travel accross every checkbutton
    for i in vars:
        
        #updating the counter
        j=j+1
        
        #Looking to the value of the checkbox variable which show if it is checked or not
        #Here, the condition is okay if the checkbox is checked
        if i.get()==1:
            
            #If the checkbox is checked, we add the food of this checkbox in the shopping list
            Shopping_list.append(Food_List[int(j-1)])
            
    #We print the list we made with all the wanted food = the shopping list
    print(Shopping_list)
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
"""Creating the list of available products"""
Food_List = ['Milk','Cereals','Chocolate powder','Jam','Orange juice', 
        'Bread','Cooking oil','Butter', 'Eggs','Emmental',
        'Cheddar','Yogurt','Sugar','Onions','Garlic','Apple',
        'Mandarin','Cherry','Blueberry','Orange','Cucumber',
        'Courgette','Salad','Rice','Pasta',
        'Carots']

"""Creating the list which will be used for the checkbuttons"""
vars = list()

"""Creating the list which will receive what products you have chosen"""
Shopping_list=[]


"""Creating the main window with the title and positioning it""" 
fenetre_main = Tk()
l = LabelFrame(fenetre_main, text="Click on the button if you are ready to create your shopping list", padx=20, pady=20)
l.pack(fill="both", expand="yes")

"""Creating the widget of the main window"""  
widget = Button(l, text = "Edit my shopping list", command = shopping, bg = "grey60")
widget.pack(expand=YES, fill=X)
  
"""Being able to launch the program and to receive the clicks of the user"""  
fenetre_main.mainloop()

"""Opening the second window with the positions of the feeds on the map"""
fenetre = Tk()

[length, width, Borders, Entrance, Shelves, Stand, Data_List] = Random_Situation(Food_List)

canvas = Canvas(fenetre, width=length, height=width, background='white')

Map_Display(Borders, Entrance, Shelves, Stand, canvas)
for Food in Shopping_list:
    Food_Display(Food, Data_List, canvas)

canvas.pack()

fenetre.mainloop()

'''
Ideas :
    - add the price of the shopping (we just need to add the price of each product in the dictionnary, and to display the total price in the final window)
    - display the food associated to the red point when the user click on
    - instead of creating the map after the selection of food, try to modify it directly when click on a food from the first window
    - use databases
'''

