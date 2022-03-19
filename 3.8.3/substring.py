def commonPermuatation(m,n):
        m,n = list(m), list(n)
        # print(m)
        sub = []
        # print(m)
        # print(n)
        for char in list(set(m)):
            # print(char)
            for i in range(min(n.count(char), m.count(char))):
                sub.append(char)
                # m.pop(m.index(char))
                # n.pop(n.index(char))
                # print(m)
        return ("".join(sorted(sub)))
if __name__ == "__main__":
    commonPermuatation("acro", "orca")