import string
import re


def sums(nums, op="*"):
    num = nums[0]
    for i in nums[1:]:
        if op == "+":
            num += i
        if op == "-":
            num -= i
        if op == "*":
            num *= i
        if op == "/":
            num /= i
    return num


# # print(sums([2,6,7,8,9,22,4]))


def int_in_leter(st):
    w = ""
    for i in st:
        try:
            int(i)
            w += i
        except:
            pass
    return int(w)


# # print(int_in_leter('1af2af3af4af5af6a7fa8f9faf'))


def number(st):
    try:
        int(st)
        return False
    except:
        return True


# # print(number('4523kjhkjl52jkhkjl'))


def solution(s):
    return re.findall(".{2}", s + "_")


# print(solution('abc'),solution('abcdef'))


def count(string, a) -> int:
    string = str(string)
    if type(string) == list:

        def to_list(list):
            word = ""
            for item in list:
                word += str(item)
            word = string
            return word

        string = to_list(string)
    a = str(a)
    w = 0
    for i in string:
        if i == a:
            w += 1
    return w


# # print(count('elzero','e'))


def repeat(string: str, re: int, space=" ", end_space: bool = False):
    integar = string
    string = str(string)
    word = ""
    for i in range(re):
        if end_space == False:
            word += string
            if re - 1 > i:
                word += space
        else:
            word += string + space
    return word


# print (repeat(8888,6,'#',True))


def zfill(st, width: int, fill: str = "0") -> str:
    st = str(st)
    len(st)
    while True:
        if len(st) == width:
            return st
        else:
            st = fill + st


# # print(zfill('999',4,'#'))


def reverse(st: str):
    word = ""
    for i in st:
        word = i + word
    return word


# # print(reverse('orezle'))


def minmal(lst, minOrMax="minmal"):
    num = lst[0]
    for i in lst:
        if minOrMax == "minmal":
            if i < num:
                num = i
        elif minOrMax == "max" or "maxmal":
            if i > num:
                num = i
    return num


# # print(minmal([-220,392,933,444]))


def idn(st: str, align="all", og=" "):
    if align == "right" or align == "all":
        for a in st:
            if a != og:
                break
            st = st[0 : len(st) - 1]
    if align == "left" or align == "all":
        st = reverse(st)
        for i in st:
            if st[-1] != og:
                st = reverse(st)
                break
            st = st[0 : len(st) - 1]
    return st


# print(idn('elzero','all',' ')) # elzero### or elzero or ###elzero


def clean_string(st, keepnum=True):
    w = ""
    if keepnum == True:
        for i in st:
            if i in string.hexdigits or i in string.ascii_uppercase or i == "_":
                w += i
    if keepnum == False:
        for i in st:
            if i in string.ascii_letters or i == "_":
                w += i
    return w


# # print(clean_string("sjdflaj_fja5_82ut8/_/]'`1",False))


def pares_string(st):
    w = ""
    for i in st:
        if i == "&":
            w += "\n"
            continue
        if w == "=":
            i += ":"
            continue
        w += i
    return w


# print(pares_string("name=nawaf&age=14&"))


def count_word(st, sep=" "):
    return len(st.split(sep))


# # print(count_word("elze#ro web #sch#ool","#"))


def first_capital(st: str) -> bool:
    st = st.split(" ")
    for i in st:
        if i[0].isupper() == False:
            return False
    return True


def imp_round(num: float) -> int:
    return int(num + 0.5)


def imp_floor(num: float) -> int:
    return int(num)


def imp_ceil(num: float) -> int:
    return int(num) + 1


def join(li, sep=" | "):
    word = ""
    num = 0
    for i in li:
        num += 1
        if len(li) == num:
            word += i
            continue
        word += i + sep
    return word


# print(join(["elzero","web","school"]))
# create function in python programming
def ceate_range(start: int, end: int, op=True):
    li = []
    i = start
    while True:
        if i >= start and i <= end:
            li.append(i)
        if i == end - 1 and op == False:
            break
        if i > end and op == True:
            break
        i += 1
    return li


print(ceate_range(3, 10, False))
