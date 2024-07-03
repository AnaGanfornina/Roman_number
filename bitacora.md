# Test
- crear una funcón que pase de número arabigo a romano (menor 4000)

```
to_romain(n: int) -> str

- Test simples
    - 1 -> "I"
    - 5 -> "V"
    - 10 -> "X"
-Test que suman números de mayor a menor
    -

-Despues de la investigación hemos decidido que un buen algoritmo es:

    1. Dividir el numero (siempre menor de 4000) en
millares, centenas, decenas y unidades. Poner en una
lista
    2. Procesar cada item de la lista transformandolo en
romano. Tendre que retocar el algoritmo que ya tengo
    3. Concatenar de mayor a menor los simbolos romanos obtenidos