#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      llafin
#
# Created:     17/11/2022
# Copyright:   (c) llafin 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random


class morpion:

    def __init__(self):
        self.tableau = []

    def creer_tableau(self):
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append('-')
            self.tableau.append(ligne)

    def random_premier_joueur(self):
        return random.randint(0, 1)

    def mettre_signe(self, ligne, colonne, player):
        if ligne>3 or colonne>3:
             ligne, colonne = list(
                map(int, input("Entrer la ligne et la colonne ").split()))
        else:

            self.tableau[ligne][colonne] = player

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
                if item == '-':
                    return False
        return True

    def tableau_remplit(self):
        for ligne in self.tableau:
            for item in ligne:
                if item == '-':
                    return False
        return True

    def tour_joueur_suivant(self, player):
        return 'X' if player == 'O' else 'O'

    def afficher_tableau(self):
        for ligne in self.tableau:
            for item in ligne:
                print(item, end=" ")
            print()

    def tour_bot(self, ligne, colonne, player,tour):



        if tour == 1:
            if ligne == 2 and colonne == 2:
                self.tableau[0][2]= player

            else:
                self.tableau[1][1]= player




        if tour == 2:


            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[1][2]=player



            if ligne == 1 and colonne == 2:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][2] = player

                if self.tableau[0][2]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][0]=player



            if ligne == 1 and colonne == 3:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][1] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][2]=='X':
                    self.tableau[1][2]=player




            if ligne == 2 and colonne == 1:

                if self.tableau[0][0] == 'X':
                    self.tableau[2][0] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][0]=player




            if ligne == 2 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][2]=player





            if ligne == 3 and colonne == 1:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][0] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[2][1]=player



            if ligne == 3 and colonne == 2:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[2][0]=player



            if ligne == 3 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X':
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[2][1]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player




        if tour == 3:

            if ligne == 1 and colonne == 1:



                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player




            if ligne == 1 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player




            if ligne == 1 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1]=player


                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][2]=player


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player





            if ligne == 2 and colonne == 1:




                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2]=player



                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player



                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player



                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player



            if ligne == 2 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player


                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player



            if ligne == 3 and colonne == 1:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[1][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player




            if ligne == 3 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


            if ligne == 3 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player






        if tour == 4:
            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player
            if ligne == 1 and colonne == 2:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

            if ligne == 1 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player





                pass
            if ligne == 2 and colonne == 1:
                pass
            if ligne == 2 and colonne == 2:
                pass
            if ligne == 2 and colonne == 3:
                pass
            if ligne == 3 and colonne == 1:
                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player
            if ligne == 3 and colonne == 2:
                pass
            if ligne == 3 and colonne == 3:
                pass
















    def start(self):
        self.creer_tableau()
        tour=1

        # on tire au sort quel joueur va commencer à jouer
        player = 'X'
        while True:
            print(f"Tour du joueur {player} ")

            self.afficher_tableau()

            # demander au joueur la postion de son signe
            ligne, colonne = list(
                map(int, input("Entrer la ligne et la colonne ").split()))
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

            self.tour_bot(ligne,colonne,player,tour)
            tour=tour+1
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
morpion = morpion()
morpion.start()