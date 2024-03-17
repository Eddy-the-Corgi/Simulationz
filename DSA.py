from pythonds.basic import Stack
from pythonds.basic import Queue
from pythonds.basic import Deque
import random

def check_list(lst,alicescore,bobscore):
        if lst[0] == "H":
            if lst[1] == "H":
                alicescore += 1
            else:
                bobscore += 1
        return alicescore, bobscore

alicewin = 0
bobwin = 0
for i in range(10000):
    lst = []
    bobscore = 0
    alicescore = 0
    coin_sides = ["H","T"]

    for i in range(100):
        lst.append(random.choice(coin_sides))
    twolst = []
    twolst = lst[0:2]

    alicescore, bobscore = check_list(twolst,alicescore,bobscore)
    for i in range(2,len(lst)):
        twolst.append(lst[i])
        twolst.pop(0)
        alicescore, bobscore = check_list(twolst,alicescore,bobscore)
    if alicescore > bobscore:
        alicewin += 1
    else:
        bobwin += 1

print(alicewin)
print(bobwin)


'''
def is_palindrome(astring):
    d = Deque()
    for char in astring:
        d.addFront(char)
    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False
    return True

print(is_palindrome("lsdkjfskf"))
print(is_palindrome("radar"))


def hot_potato(lst,num):
    q = Queue()
    for person in lst:
        q.enqueue(person)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return(q.dequeue())

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))


def dec_to_bin(n):
    s = Stack()
    while n > 0:
        s.push(n % 2)
        n = n//2
    binarystr = ""
    for i in range(s.size()):
        binarystr += str(s.pop())
    return binarystr

print(dec_to_bin(42))
'''