import re
def sums(nums,op='*'):
    num=nums[0]
    for i in nums[1:]:
        if op=='+':
            num+=i
        if op=='-':
            num-=i
        if op=='*':
            num*=i
        if op=='/':
            num/=i
    return num
# print(sums([2,6,7,8,9,22,4]))


def int_in_leter(st):
    w = ''
    for i in st:
        try:
            int(i)
            w+=i
        except:pass
    return int(w)
# print(int_in_leter('1af2af3af4af5af6a7fa8f9faf'))


def number(st):
    try:
        int(st)
        return False
    except:return True
# print(number('4523kjhkjl52jkhkjl'))

def solution(s):
    return re.findall(".{2}",s+"_")   

print(solution('abc'),solution('abcdef'))
