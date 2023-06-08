#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    name_space = dir(hidden_4)
    for i in name_space:
        if i[:2] != "__":
            print(i)
