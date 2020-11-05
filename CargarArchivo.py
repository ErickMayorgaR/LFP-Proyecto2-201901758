import re
from AnalizarTokens import *


class ArchivoCarga:
    tokens = []
    errores = []

    def tokens_errores(self):
        analyzer = CreaArchivo()
        analyzer.analiza_datos(self.tokens, self.errores)


    def revisa_forma(self, elemento):
        formas = ["circulo", "rectangulo", "triangulo", "punto", "hexagono", "diamante"]

        for forma in formas:
            if elemento.lower() == forma:
                print(elemento)
                return True
            else:
                continue

        return False

    def revisa_colores(self, lexema):
        colores = ["Azul", "Azul2", "Azul3", "Rojo", "Rojo2", "Rojo3", "Amarillo", "Amarillo2", "Amarillo3",
                   "Anaranjado", "Anaranjado2", "Anaranjado3", "Cafe", "Cafe2", "Cafe3", "Gris", "Gris2", "Gris3",
                   "Morado", "Morado2", "Morado3", "Verde", "Verde2", "Verde3", "Blanco"]

        for color in colores:
            if color.lower() == lexema.lower():
                return True
            else:
                continue
        return False

    def revisa_tokens(self, caracter, lexema, token_esperado):
        elementos = ["(", ")", "'", "verdadero", "falso", "{", "nodo", "}", ";", "lista", "defecto", ","]
        elementos.pop(elementos.index(token_esperado))

        for elemento in elementos:
            if lexema.lower == elemento:
                return True
            elif caracter == elemento:
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

        estado = 0
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
        d_puntocoma = "Punto y Coma"
        d_valordefecto = "Por defecto"
        color_defecto = False
        error_sintactico = False

        un_token = []
        un_error = []

        lexema = ""
        cond_comen = 0
        comentario = False

        for linea in informacion:
            columna = 0
            fila += 1
            if error_sintactico:
                error_sintactico = False
                break
            for caracter in linea:

                columna += 1

                if caracter == "\n" or caracter == ' ':
                    continue

                elif estado == 0:
                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    if lexema.lower() == "lista":
                        estado = 1
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, "lista"]
                        self.tokens.append(un_token)
                        lexema = ""
                        print("Estado 0-1")
                    else:
                        pass

                elif estado == 1:
                    if re.search(patron_texto, caracter):
                        lexema += caracter
                    elif caracter == '(':

                        estado = 2
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_paper]
                        self.tokens.append(un_token)

                        if lexema != "":
                            numero_error += 1
                            un_error = [numero_error, lexema, fila, columna, lexema + " No es parte del lenguaje"]
                            self.errores.append(un_error)
                            lexema = ""

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                    if self.revisa_tokens(caracter, lexema, "("):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + lexema]
                            print(estado, "Este es el estado")
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                elif estado == 2:

                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    elif caracter == "'":
                        estado = 3
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)

                        if lexema != "":
                            numero_error += 1
                            un_error = [numero_error, caracter, fila, columna, lexema + " No es parte del lenguaje"]
                            self.errores.append(un_error)
                            lexema = ""
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""

                    if self.revisa_tokens(caracter, lexema, "'"):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, lexema, fila, columna, "Se esperaba ' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break




                elif estado == 3:
                    if caracter == "'":
                        estado = 4

                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, "Nombre"]
                        self.tokens.append(un_token)

                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
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
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ',' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)

                elif estado == 5:

                    if self.revisa_forma(lexema):
                        numero_token += 1
                        un_token = [numero_token, lexema.lower(), fila, columna, d_forma]
                        self.tokens.append(un_token)

                        lexema = ""

                    if re.search(patron_cadena, caracter):
                        lexema += caracter

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
                            error_sintactico = True
                            break


                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)

                elif estado == 6:

                    if re.search(patron_texto, caracter):
                        lexema += caracter
                    else:
                        if lexema != "":
                            if lexema != "":
                                numero_error += 1
                                un_error = [numero_error, lexema, fila, columna,
                                            "Se esperaba una caracter booleano, no: " + lexema]
                                self.errores.append(un_error)
                                lexema = ""
                                error_sintactico = True
                                break

                            else:
                                numero_error += 1
                                un_error = [numero_error, caracter, fila, columna, d_caracterd]
                                self.errores.append(un_error)

                    if lexema.lower() == "verdadero" or lexema.lower() == "falso ":
                        estado = 7
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_booleano]
                        self.tokens.append(un_token)
                        lexema = ""




                elif estado == 7:
                    if caracter == ")":
                        estado = 8
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_pcierre]
                        self.tokens.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, ")"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)





                elif estado == 8:
                    if caracter == "{":
                        estado = 9
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_llaper]
                        self.tokens.append(un_token)

                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, "{"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '{' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '{' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                elif estado == 9:

                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, "nodo"):
                        numero_error += 1

                        un_error = [numero_error, caracter, fila, columna, "Se esperaba 'nodo' no " + caracter]
                        self.errores.append(un_error)
                        lexema = ""
                        error_sintactico = True
                        break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)

                    if lexema.lower() == "nodo" or lexema.lower() == "nodos":
                        estado = 10
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_nodo]
                        self.tokens.append(un_token)
                        lexema = ""






                elif estado == 10:
                    if caracter == "s":
                        continue
                    elif re.search(patron_texto, caracter):
                        lexema += caracter


                    if caracter == '(':
                        estado = 11
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_paper]
                        self.tokens.append(un_token)

                    elif self.revisa_tokens(caracter, lexema, "("):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        print("este no? ", caracter)
                        self.errores.append(un_error)



                elif estado == 11:
                    if re.search(patron_numero, caracter):
                        estado = 12
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_numero]
                        self.tokens.append(un_token)

                    elif caracter == "#":

                        estado = 15
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, "PorDefecto"]
                        self.tokens.append(un_token)

                    elif caracter == "'":
                        estado = 14
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        print("Aca")
                        lexema = ""



                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, "'"):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break





                elif estado == 12:
                    if caracter == ",":
                        estado = 13
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
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ',' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""



                elif estado == 13:
                    if caracter == "'":
                        estado = 14
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""
                    elif re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, "'"):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, lexema, fila, columna, "Se esperaba ' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""

                elif estado == 14:
                    if caracter == "'":
                        estado = 15

                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, "Nombre"]
                        self.tokens.append(un_token)

                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""
                    else:
                        lexema += caracter

                elif estado == 15:
                    if caracter == ")":
                        estado = 16
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_pcierre]
                        self.tokens.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, ")"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)




                elif estado == 16:
                    if re.search(patron_texto, caracter) or re.search(patron_numero, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, ";"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ';' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ';' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    elif caracter == "#":

                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, "ColorDefecto"]
                        self.tokens.append(un_token)
                        color_defecto = True

                    elif caracter == ";":
                        estado = 17

                        if self.revisa_colores(lexema):

                            numero_token += 1
                            un_token = [numero_token, lexema, fila, columna, d_color]
                            self.tokens.append(un_token)
                            lexema = ""

                            numero_token += 1
                            un_token = [numero_token, caracter, fila, columna, d_puntocoma]
                            self.tokens.append(un_token)

                        elif color_defecto:
                            numero_token += 1
                            un_token = [numero_token, caracter, fila, columna, d_puntocoma]
                            self.tokens.append(un_token)
                            color_defecto = False


                        else:
                            numero_error += 1
                            un_error = [numero_error, lexema, fila, columna, "Se esperaba un color no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)





                elif estado == 17:

                    if re.search(patron_texto, caracter):
                        lexema += caracter

                    elif caracter == "}":
                        estado = 18
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_llcierre]
                        self.tokens.append(un_token)

                    elif len(lexema) > 6:
                        numero_error += 1
                        un_error = [numero_error, lexema, fila, columna, "No pertenece al lenguaje" + lexema]
                        self.errores.append(un_error)
                        lexema = ""
                    elif caracter == "/":
                        cond_comen += 1
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)



                    if lexema == "nodo" or lexema == "nodos":
                        estado = 10
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_nodo]
                        self.tokens.append(un_token)
                        lexema = ""

                    elif self.revisa_tokens(caracter, lexema, "}"):
                        numero_error += 1
                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '}' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '}' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    elif cond_comen == 2:
                        cond_comen = 0
                        break



                elif estado == 18:

                    if re.search(patron_texto, caracter):
                        lexema += caracter
                    elif len(lexema) > 6:
                        numero_error += 1
                        un_error = [numero_error, lexema, fila, columna, "No pertenece al lenguaje" + lexema]
                        self.errores.append(un_error)
                        lexema = ""
                    elif caracter == "/":
                        cond_comen += 1
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)



                    if lexema == "defecto":
                        estado = 19
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_valordefecto]
                        self.tokens.append(un_token)
                        lexema = ""
                    elif self.revisa_tokens(caracter, lexema, "defecto"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba 'defecto' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba 'defecto' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    elif cond_comen == 2:
                        cond_comen = 0
                        break




                elif estado == 19:
                    if caracter == "(":
                        estado = 20
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_paper]
                        self.tokens.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, "("):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba '(' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)


                elif estado == 20:
                    if caracter == "'":
                        estado = 21
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""
                    elif re.search(patron_texto, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, "'"):
                        numero_error += 1

                        if lexema != "":

                            un_error = [numero_error, lexema, fila, columna, "Se esperaba ' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:

                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""


                elif estado == 21:
                    if caracter == "'":
                        estado = 22
                        numero_token += 1
                        un_token = [numero_token, lexema, fila, columna, d_caracterd]
                        self.tokens.append(un_token)

                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""
                    else:
                        lexema += caracter





                elif estado == 22:
                    if caracter == ")":
                        estado = 23
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_pcierre]
                        self.tokens.append(un_token)
                    elif re.search(patron_texto, caracter):
                        lexema += caracter
                    elif self.revisa_tokens(caracter, lexema, ")"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ')' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)



                elif estado == 23:
                    if re.search(patron_texto, caracter) or re.search(patron_numero, caracter):
                        lexema += caracter

                    elif self.revisa_tokens(caracter, lexema, ";"):
                        numero_error += 1

                        if lexema != "":
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ';' no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                        else:
                            un_error = [numero_error, caracter, fila, columna, "Se esperaba ';' no " + caracter]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break

                    elif caracter == ";":
                        estado = 17

                        if self.revisa_colores(lexema):

                            numero_token += 1
                            un_token = [numero_token, lexema, fila, columna, d_color]
                            self.tokens.append(un_token)
                            lexema = ""

                            numero_token += 1
                            un_token = [numero_token, caracter, fila, columna, d_puntocoma]
                            self.tokens.append(un_token)

                        else:
                            numero_error += 1
                            un_error = [numero_error, lexema, fila, columna, "Se esperaba un color no " + lexema]
                            self.errores.append(un_error)
                            lexema = ""
                            error_sintactico = True
                            break
                    else:
                        numero_error += 1
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
        print(self.tokens)
        for token in self.tokens:
            print(token[1])




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
