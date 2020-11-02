import re


class ArchivoCarga:
    tokens = []
    errores = []

    def revisa_forma(self, forma):
        formas = ["circulo","rectangulo","triangulo","punto","hexagono","diamante"]
        for forma in formas:
            if forma.lower()== forma:
                return True
            else:
                continue

        return False

    def revisa_colores(self,lexema):
        colores = ["Azul","Azul2","Azul3","Rojo","Rojo2","Rojo3","Amarillo","Amarillo2","Amarillo3","Anaranjado","Anaranjado2","Anaranjado3","Cafe","Cafe2","Cafe3","Gris","Gris2","Gris3","Morado","Morado2","Morado3","Verde","Verde2","Verde3","Blanco"]

        for color in colores:
            if color == lexema:
                return True
            else:
                continue
        return False

    def revisa_tokens(self, caracter, lexema, token_esperado):
        elementos = ["(",")","'","verdadero","falso","{","}",";", "lista"]
        elementos.pop(elementos.index(token_esperado))

        for elemento in elementos:
            if elemento == caracter:
                return True
            elif lexema == caracter:
                return True
            else:
                continue

        return False


    def analisislista(self, infodeunalista):
        numero_token = 0
        numero_error = 0
        patron_texto = r"[a-zA-Z]"
        patron_cadena = r"[a-zA-Z0-9]"
        patron_numero = r"[0-9]"

        patron_color = r"[a-zA-Z][0-9]?"

        informacion = infodeunalista.split("\n")

        estado22 = 0
        fila = 0

        d_caracterd = "cararcter desconocido"
        d_sintac = "No se esperaba"
        d_paper = "Parentesis_Apertura"
        d_pcierre = "Parentesis_Cierre"
        d_llaper = "Llave_apertura"
        d_llcierre = " Llave_Cierre"
        d_color = "Color"
        d_numero = "Numero"
        d_comilla = "Comilla"
        d_coma = "Coma"
        d_forma = "Forma"
        d_booleano = "Boolean"
        d_nodo = "Token_ Nodo"


        un_token = []
        un_error = []

        lexema = ""

        for linea in informacion:

            columna = 0
            fila += 1
            for caracter in linea:
                columna += 1

                if caracter == "\n" or caracter == ' ':
                    continue

                if estado == 0:
                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    elif lexema.lower() == "lista":
                        estado = 1
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, "lista"]
                        self.tokens.append(un_token)
                        lexema = ""
                    else:
                        continue


                elif estado == 1:
                    if caracter == "(":
                        estado = 2
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_paper ]
                        self.tokens.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, "("):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                elif estado == 2:
                    if caracter == "'":
                        estado = 3
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""
                    elif re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, "'"):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""


                elif estado == 3:
                    if caracter == "'":
                        estado = 4
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)

                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_caracterd]
                        self.tokens.append(un_token)
                        lexema = ""
                    else:
                        lexema += caracter

                elif estado == 4:
                    if caracter == ",":
                        estado = 5
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_coma]
                        self.tokens.append(un_token)

                    elif re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, ","):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ',' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ',' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                elif estado == 5:
                    if re.search(patron_cadena):
                        lexema += caracter

                    elif self.revisa_forma(lexema):
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna,]
                        self.tokens.append(un_token)
                        lexema = ""
                    elif caracter == ",":
                        estado = 6

                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_coma]
                        self.tokens.append(un_token)

                        if lexema != "":
                            numero_error += 1
                            un_error = [numero_error, lexema, fila, columna, "Se esperaba una forma, no: " + lexema]
                            self.errores.append(un_error)
                            lexema = ""

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""







                elif estado == 6:
                    if re.search(patron_texto, caracter):
                        lexema += caracter
                    elif lexema.lower() == "verdadero" or lexema.lower() == "falso ":
                        estado == 7
                        un_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_booleano]
                        self.errores.append(un_token)
                        lexema = ""
                    else:
                        if lexema != "":
                            if lexema != "":
                                numero_error += 1
                                un_error = [numero_error, lexema, fila, columna, "Se esperaba una caracter booleano, no: " + lexema]
                                self.errores.append(un_error)
                                lexema = ""

                            else:
                                numero_error += 1
                                un_error = [numero_error, caracter, fila, columna, d_caracterd]
                                self.errores.append(un_error)





                elif estado == 7:
                    if caracter == ")":
                        estado == 8
                        un_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_pcierre]
                        self.errores.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, ")"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)





                elif estado == 8:
                    if caracter == "{":
                        estado = 9
                        un_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_llaper]
                        self.errores.append(un_token)

                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, "{"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '{' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '{' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                elif estado == 9:
                    if re.search(patron_texto,caracter):
                        lexema += caracter
                    elif lexema == "nodos" or lexema == "nodos":
                        estado = 10
                        un_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_nodo]
                        self.errores.append(un_token)
                    else:



                elif estado == 10:
                elif estado == 11:
                elif estado == 12:
                elif estado == 13:
                elif estado == 14:
                elif estado == 15:
                elif estado == 16:
                elif estado == 17:
                elif estado == 18:
                elif estado == 19:
                elif estado == 20:
                elif estado == 21:









    def analisis(self, todainformacion):
            patron_texto = r"[a-zA-z]"
            info_aux = todainformacion
            informacion = todainformacion.split("\n")

            estado = 0
            fila = 0
            lexema = ""

            for linea in informacion:

                columna = 0
                fila += 1
                for caracter in linea:
                    columna += 1

                    if caracter == "\n" or caracter == ' ':
                        continue

                    if re.search(patron_texto, caracter):
                        lexema += caracter

                        if lexema.lower() == "lista":
                            self.analisislista(info_aux)
                    else:
                        continue