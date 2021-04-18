import math
from textwrap import wrap
from itertools import combinations

m = 31

# ъ -> ь
ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


# ь -> ъ
# ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й','к', 'л', 'м', 'н', 'о', 'п',
#               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'э', 'ю', 'я']

##### finding modular multiplicative inverse & linear congruences solving
def inv_by_mod(a, m):
    def gcdExtended(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = gcdExtended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = gcdExtended(a, m)
    if gcd == 1:
        if x < 0:
            d = m + x
        else:
            d = x % m
    else:
        d = -1; print("wrong numbers")
    return d


def congr(a, b, n):
    d = math.gcd(a, n)
    if d < 0:
        x = None;
        print("there are no solutions");
        return x
    if d == 1:
        t = inv_by_mod(a, n)
        x = [(b * t) % n]
    else:
        if b % d != 0:
            x = None; print("there are no solutions"); return x
        else:
            a1 = a // d
            b1 = b // d
            n1 = n // d
            x = congr(a1, b1, n1)
            for i in range(1, d):
                z = (x[0] + i * n1) % n
                x.append(z)
    return x


###### finding 5 most frequent bigrams in ciphertext
def find_most_fr_bi(num):  # finding 5 most frequent bigrams in ciphertext
    num = num + ".txt"
    f = open(f"for_test\{num}", 'r', encoding='utf8', errors='ignore')
    text = f.read()
    f.close()

    d = [s for s in list(text) if s != '\n']
    text_without_space = ''.join(d)
    data_bi_1 = wrap(text_without_space, 2)
    if len(data_bi_1[-1]) == 1: del data_bi_1[-1]

    k = 0
    dict_bi_1_w_s = {}

    for i in range(0, len(data_bi_1)):  # было(0,len(data_bi)-1)
        if data_bi_1[i] in dict_bi_1_w_s:
            pass
        else:
            dict_bi_1_w_s.update({data_bi_1[i]: k})
            k = k + 1

    data_bi_1_w_s = data_bi_1  # список всех непересекающихся биграмм без пробелов

    freq_bi_1_w_s = []  # список частот

    for i in range(0, len(dict_bi_1_w_s)):
        num = 0
        for item in data_bi_1_w_s:
            if dict_bi_1_w_s.get(item) == i: num = num + 1
        freq_bi_1_w_s.append(num / len(data_bi_1))

    # создаём словарь биграмма-частота
    d = {}
    for key, value in dict_bi_1_w_s.items():
        d[key] = freq_bi_1_w_s[value]

    # сортируем по частотам
    bi_1_w_s_freq = {}  # словарь непересек. биграмм без пробелов
    sorted_keys = reversed(sorted(d, key=d.get))
    for w in sorted_keys:
        bi_1_w_s_freq[w] = d[w]

    res = dict(list(bi_1_w_s_freq.items())[0: 5])
    return res


###### converting bigrams to numbers
def bigr_to_num(bigr):
    i = ru_alph.index(bigr[0])
    j = ru_alph.index(bigr[1])
    num = i * m + j
    return num


def list_bigr_to_num(lst):
    res = {}
    res_num = []
    for item in lst:
        res[item] = bigr_to_num(item)
        res_num.append(bigr_to_num(item))
    return res, res_num

####### iterating over all possible pairs (X,X**)&(Y,Y**) and finding all possible solutions for them
def find_key_candidates(x_pairs, y_pairs):
    ans_dict = {}
    for i in range(len(x_pairs)):
        for j in range(len(y_pairs)):
            bi = f"{x_pairs[i]}={y_pairs[j]}"
            y1 = (Y[y_pairs[j][0]] - Y[y_pairs[j][1]]) % m**2
            x1 = (X[x_pairs[i][0]] - X[x_pairs[i][1]]) % m**2
            a = congr(x1,y1,m**2) #we have to find 'a' from x1*a=y1(mod m^2)
            if a == None:
                continue
            a_b = []
            for item in a:
                b = (Y[y_pairs[j][0]]- item * X[x_pairs[i][0]]) % m**2
                a_b.append([item, b])
            ans_dict[bi] = a_b
    return ans_dict

ct_bigrams_dict = find_most_fr_bi("07")  # 5 most frequent bigrams if var 07
Y_bigrams = list(ct_bigrams_dict.keys())  # list of those bigrams (without freqs)
X_bigrams = ['ст', 'но', 'то', 'на', 'ен']  # list of 5 vjst frequent bigrams in russian
print("5 most frequent bigrams if ciphertext:", ct_bigrams_dict)

Y, Y_nums = list_bigr_to_num(Y_bigrams)
X, X_nums = list_bigr_to_num(X_bigrams)
print(Y)  # dictionary of ciphertext most freq bigrams
print(Y_nums)  # only numbers from the dictionary
print(X)  # dictionary of plaintext most freq bigrams
print(X_nums)  # only numbers from the dictionary

x_pairs = list(combinations(X_bigrams, 2))
y_pairs = list(combinations(Y_bigrams, 2))

pairs_solutions = find_key_candidates(x_pairs, y_pairs)  #all possible pairs & their solutions
for i in pairs_solutions:
    print (i,':', pairs_solutions[i])