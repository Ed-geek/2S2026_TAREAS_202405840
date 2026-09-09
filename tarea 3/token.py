# token.py

class Token:
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo        
        self.valor = valor      
        self.linea = linea      
        self.columna = columna  

    def __str__(self):
        return f"<{self.tipo}, '{self.valor}', línea {self.linea}, columna {self.columna}>"