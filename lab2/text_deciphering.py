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

def find_key_letter(mas):
    k = []
    for i in range(len(mas)):
        k_i = (mas[i] - 14) % m
        k.append(k_i)
    return k

def num_to_letter(y):
    word = []
    for item in y:
        word.append(ru_alph[item])
    return word

def M_i(n, g):  #function M_i(g)
    m_i = 0
    for i in range (r):
        for t in range(len(ru_alph)):
            let = ru_alph[t]
            z = freqs[n][(t+g) % m]
            m_i = m_i + ru_freqs.get(let) * z
    return m_i

def find_k_n(n): #meaning of n_th letter of the key
    m_values = []
    for g in range (m):
        m_i = M_i(n, g)
        m_values.append(m_i)
    k_n = m_values.index(max(m_values))
    return k_n

def find_key():
    k = []
    for j in range(r):
        k.append(find_k_n(j))
    return k

def decipher(y, k): #decipher the text using key
    x = []
    for i in range(len(y)):
        y_i = ru_dict.get(y[i])
        x_i = (y_i - k[i%r]) % m
        x.append(x_i)
    return x

ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й','к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']

ru_freqs = {'а': 0.08413309204466018, 'б': 0.018444537359456968, 'в': 0.040462673208464264, 'г': 0.01711178764854606,
            'д': 0.02942828957254013, 'е': 0.07911241482488061,  'ж': 0.009113656111376064, 'з': 0.017559304095592126,
            'и': 0.06170010518269777, 'й': 0.011478633539561108, 'к': 0.03969340223562231, 'л': 0.05009897626529559,
            'м': 0.034354237033455935, 'н': 0.06501238019952048, 'о': 0.1144482481527697, 'п': 0.028178836718561154,
            'р': 0.04283091718005841, 'с': 0.05246558696518518, 'т': 0.062276650094403106, 'у': 0.030447451116177884,
            'ф': 0.0015924399119339897, 'х': 0.009015659809103203, 'ц': 0.0038561544944370764, 'ч': 0.015486682302521117,
            'ш': 0.008515878667511613, 'щ': 0.002889257645344849, 'ъ': 0.00022865803863667545, 'ы': 0.019801786145936095,
            'ь': 0.018248544754911247, 'э': 0.0031946794540952655, 'ю': 0.00484755041909752, 'я': 0.023942129916964466}

ru_dict = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,'к':10, 'л':11, 'м':12, 'н':13,
           'о':14, 'п':15, 'р':16, 'с':17, 'т':18, 'у':19, 'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24, 'щ':25, 'ъ':26,
           'ы':27, 'ь':28, 'э':29, 'ю':30, 'я':31}

d = find_r(text)
plot_d(d)
r = 15  # found from plot

Y = y_to_blocks(text) #ciphertext divided into blocks of symbols with step r
freqs = letter_freqs(Y) #freqs of letters of block

most_freq = find_most_freq(freqs) #indexes of most frequent letters of the block
print("max_let_ind=",most_freq)

### визначення символів ключа прирівнюючи найчастіші літери в мові
# "o" is most frequent in russian. position:14
m = 32

key_numbers_1 = find_key_letter(most_freq) #key letters`numbers
print("key 1:\n", key_numbers_1)

key_word_1 = num_to_letter(key_numbers_1)
print(key_word_1)

### визначення символів ключа за допомогою функції М_і(g)

key_numbers_2 = find_key() #key letters`numbers
print("key 2:\n", key_numbers_2)

key_word_2 = num_to_letter(key_numbers_2)
print(key_word_2)

key = key_numbers_2

X_numbers = decipher(text, key)
X = ''.join(num_to_letter(X_numbers)) #original text

print("KEY:", ''.join(key_word_2))
print("ORIGINAL TEXT:\n", X)
