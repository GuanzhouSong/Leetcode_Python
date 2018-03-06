t = "aaa"
s = "aaaa"
mem = [1 for _ in range(len(s) + 1)] + [[0 for _ in range(len(s) + 1)] for _
                                        in range(len(t))]
print(mem)
