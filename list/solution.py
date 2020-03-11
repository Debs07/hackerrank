if __name__ == '__main__':
    result = []
    for i in range(0, int(input())):
        cmd = input().split()
        if cmd[0] == "print":
            print(result)
            continue

        eval(
            "result.{}({})".format(
                cmd[0],
                str(",".join(cmd[1:]))
            )
        )
        

