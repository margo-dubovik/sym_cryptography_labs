import math
from textwrap import wrap

# ъ -> ь
ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


# ь -> ъ
# ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й','к', 'л', 'м', 'н', 'о', 'п',
#               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'э', 'ю', 'я']

##### finding modular multiplicative inverse & linear congruences solving
def inv_by_mod(a, m): #finding modular multiplicative inverse
    def gcdExtended(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = gcdExtended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = gcdExtended(a, m)
    d = 0
    if gcd == 1:
        if x < 0:
            d = m + x
        else:
            d = x % m
    else:
        d = 0; print("wrong numbers")
    return d


def congr(a, b, n):  # linear congruences solving. a*x = b (mod n)
    d = math.gcd(a, n)
    if d == 1:
        t = inv_by_mod(a, n)
        x = [(b * t) % n]
    else:
        if b % d != 0:
            x = [0]; print("there are no solutions"); return x
        else:
            a1 = a // d
            b1 = b // d
            n1 = n // d
            x = congr(a1, b1, n1)
            for i in range(1, d):
                z = (x[0] + i * n1) % n
                x.append(z)
    return x


def find_most_fr_bi(num): #finding 5 most frequent bigrams in ciphertext
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


ct_bigrams_dict = find_most_fr_bi("07")  # 5 most frequent bigrams if var 07
ct_bigrams_list = list(ct_bigrams_dict.keys())  # list of those bigrams (without freqs)
ru_bigrams_list = ['ст', 'но', 'то', 'на', 'ен']  # list of 5 most frequent bigrams in russian
print(ct_bigrams_dict)