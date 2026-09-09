from lexer import Lexer

def main():
    print("=== ANALIZADOR LÉXICO ===")
    archivo = input("Ingrese el nombre del archivo de código: ")

    lexer = Lexer(archivo)
    lexer.analizar()

    # Mostrar tokens
    lexer.mostrar_tokens()

    # Mostrar errores
    lexer.mostrar_errores()

if __name__ == "__main__":
    main()