def func_maximo():
    maximo = Lista[0]
    for z in range(len(Lista)):
        if Lista[z] > maximo:
            maximo = Lista[z]
    return maximo


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    Lista = []
    for x in arr:
        Lista.append(x)
    x = func_maximo()
    while func_maximo() == x:
        Lista.remove(x)
    print(func_maximo())

