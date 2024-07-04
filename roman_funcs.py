valors = {
    1:"I",
    5:"V", 
    10:"X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
    }
def divide_digitos(n):
   
    orden = 10**(len(str(n))-1)
    d = n//orden

    return d,orden


def to_roman(n):
    d,orden  = divide_digitos(n)
    

    # Números del 1 al 9
    result = ""
    if d <= 3:
        result = d * valors[orden]
    elif d == 4:
        result = valors[orden] + valors[5 * orden] 
    elif d < 9:
        result = valors[5 * orden] + (d-5)* valors[orden]
    elif d == 9:
        result = valors[orden] + valors[orden * 10]

    

    return result

def dividir_en_digitos(n:int):
    cad = f"{n:04d}"

    millares = int(cad[0]) * 1000
    centenas = int(cad[1]) * 100
    decenas = int(cad[2]) * 10
    unidades = int(cad[3]) * 1

    return [millares,centenas,decenas,unidades]

def digits_to_roman(lista):
    result = ""

    for item in lista:
        result += to_roman(item)

    return result
    
def arabigo_a_romano(numero:int):
    
    lista = dividir_en_digitos(numero)
    return digits_to_roman(lista)


to_roman(50)