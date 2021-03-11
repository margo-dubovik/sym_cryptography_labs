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
    for i in range(0, r):
        y_i = y[i:: r]
        y_blocks.append(y_i)
    return y_blocks

def letter_freqs(y):
    fr = []
    for j in range(len(Y)):
        fr_j = []
        for i in range(0,32):
            fr_j.append(Y[j].count(ru_alph[i]))
        fr.append(fr_j)
    return fr


def find_most_freq(fr):
    max_let = []  #indexes of most frequent letters of the block
    for i in range(len(fr)):
        max_let.append(freqs[i].index(max(fr[i])))
    return max_let

ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й','к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']


d = find_r(text)
plot_d(d)
r = 15  # found from plot

Y = y_to_blocks(text) #ciphertext divided into blocks of symbols with step r
freqs = letter_freqs(Y) #freqs of letters of block

most_freq = find_most_freq(freqs) #indexes of most frequent letters of the block
print("max_let_ind=",most_freq)

