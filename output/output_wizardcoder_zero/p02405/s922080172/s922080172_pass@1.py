new_code = (lambda h, w, b: [print(b[i%2][0:w] for i in range(h)) for _ in range(h)])
XS = list(map(int, open(0).read().split()))
new_code(*XS[:2], ["#."*150, ".#"*150])