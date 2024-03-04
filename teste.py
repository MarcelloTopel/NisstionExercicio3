def maior_numero(lista):
    return max(lista)

def total_nomes(lista):
    return len(lista)

def soma_numeros(lista):
    return sum(lista)

def media_numeros(lista):
    return sum(lista) / len(lista)

def quantidade_palavras_com_a(lista):
    return sum(1 for palavra in lista if palavra.startswith('A'))

def mais_longa_palavra(lista):
    return max(lista, key=len)

def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

def numeros_impares(lista):
    return [num for num in lista if num % 2 != 0]

def numeros_presentes_em_ambas(lista1, lista2):
    return list(set(lista1) & set(lista2))

def remover_repetidos(lista):
    return list(set(lista))

if __name__ == "__main__":
    lista_numeros = [2, 5, 10, 8, 3, 15, 7, 9, 10]
    lista_nomes = ["Ana", "João", "Maria", "Pedro", "Alice", "Antônio"]
    lista_palavras = ["amor", "abraço", "casa", "água", "avestruz"]
    lista_strings = ["python", "javascript", "java", "ruby", "c"]

    # 1. Maior número da lista
    print("Maior número:", maior_numero(lista_numeros))

    # 2. Número total de nomes na lista
    print("Total de nomes:", total_nomes(lista_nomes))

    # 3. Soma de todos os números da lista
    print("Soma dos números:", soma_numeros(lista_numeros))

    # 4. Média dos números da lista
    print("Média dos números:", media_numeros(lista_numeros))

    # 5. Quantidade de palavras que começam com 'A'
    print("Quantidade de palavras com 'A':", quantidade_palavras_com_a(lista_palavras))

    # 6. Mais longa palavra da lista
    print("Mais longa palavra:", mais_longa_palavra(lista_strings))

    # 7. Números pares da lista
    print("Números pares:", numeros_pares(lista_numeros))

    # 8. Números ímpares da lista
    print("Números ímpares:", numeros_impares(lista_numeros))

    lista_numeros_1 = [1, 2, 3, 4, 5]
    lista_numeros_2 = [4, 5, 6, 7, 8]

    # 9. Números presentes em ambas as listas
    print("Números presentes em ambas as listas:", numeros_presentes_em_ambas(lista_numeros_1, lista_numeros_2))

    # 10. Remover números repetidos da lista
    print("Lista sem números repetidos:", remover_repetidos(lista_numeros))
