# 백준 1935번. 후위 표기식3
# 문제:
# 피연산자: A~Z의 영대문자, 개수 N, 각각 대응하는 숫자가 있음
# 연산자: *, /, +, -
# 구하는 것: 후위 표기식을 계산한 결과를 출력한다.

# ABC*+DE/-은 A+B*C-D/E와 같다.
# 아이디어: 스택을 이용하자.
# 후위 표기식을 앞에서부터 차례대로 읽으면서, 피연산자가 나오면 스택에 넣는다.
# 연산자가 나오면 스택에서 두 개를 pop해서 연산을 한 다음 다시 넣는다.
# 후위 표기식을 끝까지 읽으면 스택에는 최종 계산 결과 값 하나가 남아 있다.

def calculate(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

N = int(input())
expression = input()
values = [int(input()) for _ in range(N)]
stack = []

for x in expression:
    if x.isalpha():
        stack.append(values[ord(x) % 65])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, b, x))

print("{:.2f}".format(stack.pop()))
