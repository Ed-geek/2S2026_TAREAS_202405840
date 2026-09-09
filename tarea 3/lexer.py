# lexer.py
# Analizador léxico simple usando un AFD 

from token import Token

class Lexer:
    def __init__(self, archivo):
        self.archivo = archivo
        self.texto = ""
        self.tokens = []
        self.errores = []
        self.linea = 1
        self.columna = 1
        self.reservadas = {"if", "else", "while", "int", "return"}
        self.simbolos = {'(', ')', '{', '}', ':', '.'}
        self.operadores = {'+', '-', '*', '/', '=', '<', '>', '!'}
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.texto = f.read()
        except FileNotFoundError:
            print(f"Error: archivo '{self.archivo}' no encontrado.")
            exit(1)

    def agregar_token(self, tipo, valor, linea, columna):
        self.tokens.append(Token(tipo, valor, linea, columna))

    def agregar_error(self, linea, columna, caracter):
        self.errores.append((linea, columna, caracter))

    def analizar(self):
        i = 0
        n = len(self.texto)
        self.linea = 1
        self.columna = 1

        while i < n:
            caracter = self.texto[i]

            # Saltar espacios y tabuladores (no se generan tokens)
            if caracter == ' ' or caracter == '\t':
                i += 1
                self.columna += 1
                continue

            # Salto de línea
            if caracter == '\n':
                i += 1
                self.linea += 1
                self.columna = 1
                continue

            # ---------- INICIO DE UN NUEVO TOKEN ----------
            linea_actual = self.linea
            columna_actual = self.columna

            # 1. Identificador o palabra reservada (letra o _)
            if caracter.isalpha() or caracter == '_':
                valor = ""
                while i < n and (self.texto[i].isalnum() or self.texto[i] == '_'):
                    valor += self.texto[i]
                    i += 1
                    self.columna += 1
                # Clasificar
                if valor in self.reservadas:
                    tipo = "PALABRA_RESERVADA"
                else:
                    tipo = "IDENTIFICADOR"
                self.agregar_token(tipo, valor, linea_actual, columna_actual)
                continue

            # 2. Número (dígitos)
            if caracter.isdigit():
                valor = ""
                while i < n and self.texto[i].isdigit():
                    valor += self.texto[i]
                    i += 1
                    self.columna += 1
                self.agregar_token("NUMERO", valor, linea_actual, columna_actual)
                continue

            # 3. Operadores (incluyendo de dos caracteres)
            if caracter in self.operadores:
                valor = caracter
                i += 1
                self.columna += 1
                # Verificar si es un operador doble (==, !=, <=, >=)
                if i < n and self.texto[i] == '=' and caracter in ('=', '!', '<', '>'):
                    valor += self.texto[i]
                    i += 1
                    self.columna += 1
                self.agregar_token("OPERADOR", valor, linea_actual, columna_actual)
                continue

            # 4. Símbolos de agrupación y puntuación (un solo carácter)
            if caracter in self.simbolos:
                self.agregar_token("SIMBOLO", caracter, linea_actual, columna_actual)
                i += 1
                self.columna += 1
                continue

            # 5. Si llegamos aquí, es un carácter no reconocido -> error léxico
            self.agregar_error(linea_actual, columna_actual, caracter)
            i += 1
            self.columna += 1