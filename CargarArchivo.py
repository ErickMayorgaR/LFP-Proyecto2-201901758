import re


class ArchivoCarga:
    tokens = []
    errores = []

    def revisa_tokens(self, caracter, lexema, token_esperado):
        elementos = ["(",")","'","verdadero","falso","{","}",";", "lista"]
        elementos.pop(elementos.index(token_esperado))

        for elemento in elementos:
            if elemento == caracter:
                return True
            elif elemento == caracter:
                return True
            else:
                continue

        return False


    def analisislista(self, infodeunalista):
        numero_token = 0
        numero_error = 0
        patron_texto = r"[a-zA-z]"
        patron_cadena = r"[a-zA-z0-9]"
        patron_numero = r"[0-9]"

        informacion = infodeunalista.split("\n")

        estado = 0
        fila = 0

        d_caracterd = "cararcter desconocido"
        d_sintac = "No se esperaba"
        d_paper = "Parentesis_Apertura"
        d_pcierre = "Parentesis_Cierre"
        d_llaper = "llave_apertura"
        d_color = "Color"
        d_numero = "Numero"
        d_comilla = "Comilla"

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
                        numero_token +=1
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
                        lexema = ""
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
                        un_error = [numero_error, caracter, fila, columna, d_caracterd]
                        self.errores.append(un_error)
                        lexema = ""


                elif estado == 3:


                    if caracter == "'":
                        estado = 4
                        numero_token += 1
                        un_token = [numero_token, caracter, fila, columna, d_comilla]
                        self.tokens.append(un_token)
                        lexema = ""


                    else:
                        if re.search(patron_cadena, caracter):
                            numero_token += 1
                            un_token = [numero_token, caracter, fila, columna, d_comilla]
                            self.tokens.append(un_token)


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