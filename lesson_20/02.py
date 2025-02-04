A = [18, 42, 600, 214, 86, 320, 99, 52, 901]
iki_belgili = []
uc_belgili = []
mukdar = 0
m = 0
for i in A:
    if i <= 99:
        iki_belgili.append(i)
        mukdar += 1
    else:
        uc_belgili.append(i)
        m += 1

print(iki_belgili)
print(f"Mukdar {mukdar}")
print(uc_belgili)
print(f"Mukdar {m}")