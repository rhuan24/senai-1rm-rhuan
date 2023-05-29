def area(largura, comprimento):
    return largura * comprimento

largura = float(input("qual a largura do terreno: "))
comprimento = float(input("qual o comprimento do terreno: "))

resultado = area(largura, comprimento)
print("A área do terreno é:", resultado)