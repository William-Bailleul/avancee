import random
import tkinter as tk
from PIL import Image, ImageTk

class Slot:

    def __init__(self,x , y, frame, player_click):
        self.x = x
        self.y = y
        self.char = '-'
        self.frame = frame 
        self.init_button()
        self.player_click = player_click
        

    def init_button(self):
        self.image = ImageTk.PhotoImage(Image.open('blank.png'))
        self.button = tk.Button(self.frame, image = self.image, command= self.click)
        self.button.grid(row = self.x, column= self.y)

    def click(self):
        if self.char == '-':
            self.set_char('X')
            self.player_click(self.x,self.y)

    def set_char(self,char):
        self.char = char
        if char == '-':
            self.image = ImageTk.PhotoImage(Image.open('blank.png'))
        else:
            self.image = ImageTk.PhotoImage(Image.open(f'{char}.png'))
        self.button.config(image = self.image)




class Morpion(tk.Tk):

    def __init__(self):
        super().__init__()
        self.tableau = []
        self.tour = 0
        

    def creer_tableau(self):
        self.frame = tk.Frame(self, width= 700, height= 700, bg='White')
        for row in range(3):
            ligne = []
            for col in range(3):
                button = Slot(row,col,self.frame,self.player_click) 
                ligne.append(button)
            self.tableau.append(ligne)
        self.frame.pack()
        

    def random_premier_joueur(self):
        return random.randint(0, 1)

    def mettre_signe(self, ligne, colonne, player):
        if ligne>3 or colonne>3:
             ligne, colonne = list(
                map(int, input("Entrer la ligne et la colonne ").split()))
        else:

            self.tableau[ligne][colonne].set_char(player)

    def victoire_joueur(self, player):
        win = None
        n = len(self.tableau)

        # on regarde les lignes
        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # on regarde les colonnes
        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # on regarde les diagonales
        win = True
        for i in range(n):
            if self.tableau[i][i] != player:
                win = False
                break
        if win:
            return win
        win = True

        for i in range(n):
            if self.tableau[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for ligne in self.tableau:
            for item in ligne:
                if item.char == '-':
                    return False
        return True

    def tableau_remplit(self):
        for ligne in self.tableau:
            for item in ligne:
                if item.char == '-':
                    return False
        return True

    def tour_joueur_suivant(self, player):
        return 'X' if player == 'O' else 'O'

    def player_click(self, ligne, colonne):
        self.prochain_tour('X')
        self.tour_bot(ligne, colonne)
        self.prochain_tour('O')
    

    def prochain_tour(self, player):          
        # on regarde si un joueur a gagné
        if self.victoire_joueur(player):
            print(f"Joueur {player} à gagné le match!")
            return
        # on regarde si il y a match nul
        if self.tableau_remplit():
            print("Match nul!")
            return
        self.tour += 1



    def afficher_tableau(self):
        for ligne in self.tableau:
            for item in ligne:
                print(item, end=" ")
            print()

    def tour_bot(self, ligne, colonne):
        player = 'O'

        if self.tour == 1:
            if ligne == 2 and colonne == 2:
                self.tableau[0][2].set_char(player)

            else:
                self.tableau[1][1].set_char(player)




        if self.tour == 2:


            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[1][2].set_char(player)



            if ligne == 1 and colonne == 2:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[0][0].set_char(player)



            if ligne == 1 and colonne == 3:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[1][2].set_char(player)




            if ligne == 2 and colonne == 1:

                if self.tableau[0][0] == 'X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[0][0].set_char(player)




            if ligne == 2 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[0][2].set_char(player)





            if ligne == 3 and colonne == 1:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[2][1].set_char(player)



            if ligne == 3 and colonne == 2:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[2][2]=='X':
                    self.tableau[2][0].set_char(player)



            if ligne == 3 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[1][0]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][2]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][0]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)




        if self.tour == 3:

            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X': 
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)




            if ligne == 1 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)




            if ligne == 1 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1].set_char(player)


                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2].set_char(player)





            if ligne == 2 and colonne == 1:




                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2].set_char(player)



                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0].set_char(player)



                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0].set_char(player)



                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)



            if ligne == 2 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)



            if ligne == 3 and colonne == 1:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[1][0].set_char(player)


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)


                if self.tableau[1][2].char=='X' and self.tableau[2][1].char=='X' :
                    self.tableau[0][0].char=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)


                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)




            if ligne == 3 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1].set_char(player)


            if ligne == 3 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X':
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1].set_char(player)


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[1][2].set_char(player)


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][1].set_char(player)


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1].set_char(player)


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0].set_char(player)






        if self.tour == 4:
            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1].set_char(player)
            if ligne == 1 and colonne == 2:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

            if ligne == 1 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2].set_char(player)





                pass
            if ligne == 2 and colonne == 1:
                pass
            if ligne == 2 and colonne == 2:
                pass
            if ligne == 2 and colonne == 3:
                pass
            if ligne == 3 and colonne == 1:
                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0].set_char(player)

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1].set_char(player)

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0].set_char(player)
            if ligne == 3 and colonne == 2:
                pass
            if ligne == 3 and colonne == 3:
                pass
















    def start(self):
        self.creer_tableau()
        # on tire au sort quel joueur va commencer à jouer
        player = 'X'
        while True:
            print(f"Tour du joueur {player} ")

            self.afficher_tableau()

            # demander au joueur la postion de son signe
            ligne, colonne = list(map(int, input("Entrer la ligne et la colonne ").split()))
            print()

            # mettre le signe aux bonnes coordonnées
            self.mettre_signe(ligne - 1, colonne - 1, player)

            # on regarde si un joueur a gagné
            if self.victoire_joueur(player):
                print(f"Joueur {player} à gagné le match!")
                break

            # on regarde si il y a match nul
            if self.tableau_remplit():
                print("Match nul!")
                break

            # passer au tour suivant
            player = self.tour_joueur_suivant(player)

            self.tour_bot(ligne,colonne)
            if self.victoire_joueur(player):
                print(f"Joueur {player} à gagné le match!")
                break

            # on regarde si il y a match nul
            if self.tableau_remplit():
                print("Match nul!")
                break

            player = self.tour_joueur_suivant(player)


        # on affiche le tableau à la fin du match
        print()
        self.afficher_tableau()


# on commence le match
morpion = Morpion()
morpion.start()

morpion.mainloop()