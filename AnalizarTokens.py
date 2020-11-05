import re

class CreaArchivo:
    tokens = []
    errores2 = []
    nodos = []

    def crea_grafica_lista(self):
        patron_numero = "[0-9]"
        p1 = '[label = "'
        p2 = ' ,style="filled", fillcolor= "'

        lista_doble = False
        lista_simple = False
        color = ""
        forma = ""
        nombre_mapa = self.tokens[3][1]
        for token in self.tokens:
            if token[1].lower() == "verdadero":
                lista_doble = True
            elif token[1].lower() == "falso":
                lista_simple = True
            elif token[4].lower == "forma":
                if token[1].lower() == "circulo":
                    forma = "circle"
                elif token[1].lower() == "triagunlo":
                    forma = "triangle"
                elif token[1].lower() == "hexagono":
                    forma = "hexagon"
                elif token[1].lower() == "rectangulo":
                    forma = "box"
                elif token[1].lower() == "punto":
                    forma = "point"
                elif token[1].lower() == "diamante":
                    forma = "diamond"

        codigo_forma = 'node[shape =' + forma + ']'
        self.nodos.append(codigo_forma)

        for x in range(0, len(self.tokens)):
            print(self.tokens[x][1])

            if self.tokens[x][1] == "nodo":
                if re.search(patron_numero, self.tokens[(x+2)][1]):
                    if self.tokens[(x + 8)][1].lower() == "azul":
                        color = "lightblue"
                    elif self.tokens[(x + 8)][1].lower() == "azul2":
                        color = "blue"
                    elif self.tokens[(x + 8)][1].lower() == "azul3":
                        color = "blue4"
                    elif self.tokens[(x + 8)][1].lower() == "rojo":
                        color = "firebrick1"
                    elif self.tokens[(x + 8)][1].lower() == "rojo2":
                        color = "firebrick2"
                    elif self.tokens[(x + 8)][1].lower() == "rojo3":
                        color = "firebrick3"
                    elif self.tokens[(x + 8)][1].lower() == "amarillo":
                        color = "yellow"
                    elif self.tokens[(x + 8)][1].lower() == "amarillo2":
                        color = "gold"
                    elif self.tokens[(x + 8)][1].lower() == "amarillo3":
                        color = "yellow3"
                    elif self.tokens[(x + 8)][1].lower() == "anaranjado":
                        color = "orange"
                    elif self.tokens[(x + 8)][1].lower() == "anaranjado2":
                        color = "darkorange"
                    elif self.tokens[(x + 8)][1].lower() == "anaranjado3":
                        color = "orangered2"
                    elif self.tokens[(x + 8)][1].lower() == "cafe":
                        color = "tan2"
                    elif self.tokens[(x + 8)][1].lower() == "cafe2":
                        color = "tan4"
                    elif self.tokens[(x + 8)][1].lower() == "cafe3":
                        color = "saddlebrown"
                    elif self.tokens[(x + 8)][1].lower() == "gris":
                        color = "gray97"
                    elif self.tokens[(x + 8)][1].lower() == "gris2":
                        color = "gray60"
                    elif self.tokens[(x + 8)][1].lower() == "gris3":
                        color = "gray24"
                    elif self.tokens[(x + 8)][1].lower() == "morado":
                        color = "magenta"
                    elif self.tokens[(x + 8)][1].lower() == "morado2":
                        color = "magenta2"
                    elif self.tokens[(x + 8)][1].lower() == "morado3":
                        color = "magenta4"
                    elif self.tokens[(x + 8)][1].lower() == "verde":
                        color = "green"
                    elif self.tokens[(x + 8)][1].lower() == "verde2":
                        color = "green2"
                    elif self.tokens[(x + 8)][1].lower() == "verde3":
                        color = "green4"
                    elif self.tokens[(x + 8)][1].lower() == "blanco":
                        color = "white"
                    n_nodos = 0

                    while n_nodos < self.tokens[x+2][1]:
                        nodo = self.tokens[(x + 5)][1] + p1 + self.tokens[(x + 5)][1] + str((n_nodos+1)) + '"' + p2 + color + '"' + "]"
                        self.nodos.append(nodo)


                else:
                    if self.tokens[(x + 6)][1].lower() == "azul":
                        color = "lightblue"
                    elif self.tokens[(x + 6)][1].lower() == "azul2":
                        color = "blue"
                    elif self.tokens[(x + 6)][1].lower() == "azul3":
                        color = "blue4"
                    elif self.tokens[(x + 6)][1].lower() == "rojo":
                        color = "firebrick1"
                    elif self.tokens[(x + 6)][1].lower() == "rojo2":
                        color = "firebrick2"
                    elif self.tokens[(x + 6)][1].lower() == "rojo3":
                        color = "firebrick3"
                    elif self.tokens[(x + 6)][1].lower() == "amarillo":
                        color = "yellow"
                    elif self.tokens[(x + 6)][1].lower() == "amarillo2":
                        color = "gold"
                    elif self.tokens[(x + 6)][1].lower() == "amarillo3":
                        color = "yellow3"
                    elif self.tokens[(x + 6)][1].lower() == "anaranjado":
                        color = "orange"
                    elif self.tokens[(x + 6)][1].lower() == "anaranjado2":
                        color = "darkorange"
                    elif self.tokens[(x + 6)][1].lower() == "anaranjado3":
                        color = "orangered2"
                    elif self.tokens[(x + 6)][1].lower() == "cafe":
                        color = "tan2"
                    elif self.tokens[(x + 6)][1].lower() == "cafe2":
                        color = "tan4"
                    elif self.tokens[(x + 6)][1].lower() == "cafe3":
                        color = "saddlebrown"
                    elif self.tokens[(x + 6)][1].lower() == "gris":
                        color = "gray97"
                    elif self.tokens[(x + 6)][1].lower() == "gris2":
                        color = "gray60"
                    elif self.tokens[(x + 6)][1].lower() == "gris3":
                        color = "gray24"
                    elif self.tokens[(x + 6)][1].lower() == "morado":
                        color = "magenta"
                    elif self.tokens[(x + 6)][1].lower() == "morado2":
                        color = "magenta2"
                    elif self.tokens[(x + 6)][1].lower() == "morado3":
                        color = "magenta4"
                    elif self.tokens[(x + 6)][1].lower() == "verde":
                        color = "green"
                    elif self.tokens[(x + 6)][1].lower() == "verde2":
                        color = "green2"
                    elif self.tokens[(x + 6)][1].lower() == "verde3":
                        color = "green4"
                    elif self.tokens[(x + 6)][1].lower() == "blanco":
                        color = "white"

                    nodo = self.tokens[(x+3)][1] + p1 + self.tokens[(x+3)][1] + '"' + p2 + color + '"' + "]"
                    self.nodos.append(nodo)


    def escribeinfo(self, info, file, segundaCol, UltimaCol):
        file.write("No. ; Lexema ; Fila ; Columna ;" + UltimaCol)

        for x in range(0, len(info)):
            file.write("\n")
            for y in range(0, len(info[x])):
                if str(info[x][y]) == ";":
                    file.write('";"')
                    file.write(";")
                else:
                    file.write(str(info[x][y]))
                    print(str([x]) + str([y]))
                    file.write(";")




    def crearcsv(self, tokens, errores):
        with open("C:/Users/Erick Mayorga/Desktop/LFP Proyecto2-201901758/LFP-Proyecto2-201901758/Tokens.csv",
                  'w', encoding='utf-8') as file:
            self.escribeinfo(tokens, file, "Lexema", "Token")

        with open("C:/Users/Erick Mayorga/Desktop/LFP Proyecto2-201901758/LFP-Proyecto2-201901758/Errores.csv",
                  'w', encoding='utf-8') as file:
            self.escribeinfo(errores, file, "Caracter", "Descripcion")

    def analiza_datos(self, tokens, errores):
        self.tokens = tokens
        self.errores2 = errores
        #self.crearcsv(self.tokens, self.errores2)
        print(self.tokens[0][1])
        if self.tokens[0][1] == "lista":
            self.crea_grafica_lista()
