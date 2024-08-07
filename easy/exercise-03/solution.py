if __name__ == '__main__':
    N = int(input())  # Lê o número de comandos
    lst = []  # Inicia uma lista vazia

    for _ in range(N):
        command = input().split()  # Lê o comando e separa por espaços
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()


"""
Explicação:
Entrada de Comandos:
O número N indica quantos comandos serão fornecidos.
Para cada comando, a linha é lida e dividida em partes.

Comandos Executados:
insert i e: Insere o elemento e na posição i da lista.
print: Imprime a lista atual.
remove e: Remove a primeira ocorrência do elemento e da lista.
append e: Adiciona o elemento e ao final da lista.
sort: Ordena a lista.
pop: Remove o último elemento da lista.
reverse: Inverte a ordem da lista.

Saída:
A lista é impressa toda vez que o comando print é executado.
"""