#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for x in range(len(name)):
        if name[x][0] != "_" and name[x][1] != "_":
            print(name[x])
