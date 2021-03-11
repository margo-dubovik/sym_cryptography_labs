from matplotlib import pyplot as plt

f = open(r'C:\Users\Alex\MARGO\crypto_labs\lab2\var7_1.txt', 'r', encoding='utf8', errors='ignore')
text = f.read()
f.close()


def find_r(y):
    a = []
    for r in range(6, 31):
        d_r = 0
        for i in range(1, len(y) - r):
            if y[i] == y[i + r]:
                d_r += 1
        a.append(d_r)
    print("d=", a)
    return a


def plot_d(d):
    r = list(range(6, 31))
    plt.plot(r, d)
    plt.show()


def y_to_blocks(y):
    y_blocks = []
    for i in range(0, len(y), r):
        y_i = y[i: i + r]
        y_blocks.append(y_i)
    return y_blocks


d = find_r(text)
plot_d(d)
r = 15  # found from plot

Y = y_to_blocks(text)  # ciphertext divided into blocks length=r
