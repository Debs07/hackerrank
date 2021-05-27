if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x = max(arr)
    while max(arr) == x:
        arr.remove(max(arr))
print(max(arr)) 
    

