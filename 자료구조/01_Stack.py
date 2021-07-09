"""
[자료구조 스택 활용 - 계산기]
    입력: "2+3*5"
    숫자는 피연산자, 나머지는 연산자
    위 입력에서 실제 동작과정은, 
    (2+(3*5)) 순서로 진행된다.
    스택을 활용하여 연산을 수행하기 위해서는
    infix 수식의 입력을 postfix 수식으로 바꿔주면 쉽다.
    "2+3*5" --> "235*+"

    [infix 수식을 postfix 수식으로 바꾸는 방법]
    1. 괄호치기
    2. 연산자의 오른쪽 괄호 다음으로 연산자 이동
    3. 괄호 지우기

    입력: +, -, *, /, (, ), 숫자(영문자)로 구성된 infix 수식
    출력: postfix 수식

    A + B * C -> A B C * +
    1. 피연산자의 순서는 그대로
    2. 연산자의 경우 우선 스택에 추가하고,자신보다 우선 순위의 연산자가 들어오지 않는다면, pop한다.
    3. 모든 탐색이 끝난 뒤, 스택에 남아있는 연산자들을 차례로 pop한다.

    괄호의 경우, 왼쪽 괄호는 우선 순위가 제일 낮고, 오른쪽 괄호는 왼쪽 괄호보다 우선 순위가 낮다.
    오른쪽 괄호가 나타나면, 스택에서 왼쪽 괄호가 나올 때까지 pop한다.

    for token in expr:
        if token == operand:
            outstack.append(token)
        elif token == "(":
            opstack.append(token)
        elif token == ")":
            while True:
                x = stack.pop()
                if x == "(":
                    break

                outstack.append(x)
        else: # elif token in "+*-/"
            opstack에 token보다 우선 순위가 높은 연산자 pop
            자신이 opstack에 들어가기

    while opstack:
        outstack.append(opstack.pop())

    [postfix 수식으로 만든 뒤 계산하기]
    for token in outstack:
        if token == operand:
            S.append(token)
        elif token in "+-*/":
            a = S.pop()
            b = S.pop()
            S.append(b token a)
"""

# 계산기 프로그램
from tkinter import Tk, Label, Button, Entry, StringVar

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def compute_postfix(postfix):
	stack = []
	arr = postfix.split()
	for token in arr:
		if token in "+-*/":
			a = stack.pop()
			b = stack.pop()
			stack.append(str(eval(b + token + a)))
		else:
			stack.append(token)
	
	return f"{float(stack[0]):.4f}"

def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    token_list = infix.split()

    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack:
                x = opstack.pop()
                if x == "(":
                    break

                outstack.append(x)
        elif token in '+-/*^':
            while opstack and prec[opstack.top()] >= prec[token]:
                outstack.append(opstack.pop())
            opstack.push(token)
        else:
            outstack.append(token)
            
    while opstack:
        outstack.append(opstack.pop())
    
    return " ".join(outstack)

def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set(value)
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()