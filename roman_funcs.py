valors = {
    1:"I",
    5:"V", 
    10:"X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
    }

def romano_simples(n):
    # Números del 1 al 9
    result = ""
    if n <= 3:
        result = n * valors[1]
    elif n == 4:
        result = valors[1] + valors[5]
    elif n < 9:
        result = valors[5] + (n-5)* valors[1]
    elif n == 9:
        result = valors[1] + valors[10]
    

    return result



def to_roman(n):
    result = ""
    acum = 0
    if n >= 50:
          result = valors[n]

    elif n >= 40 :
        n = n-40
        result = valors[10] + valors[50] + romano_simples(n)
    
    elif  n < 40 :
        while n >= 10:
            n = n-10
            acum += 1 
        
        result = (valors[10] * acum ) + romano_simples(n)
    
    elif n <= 10:
        result = romano_simples(n)

    return result

