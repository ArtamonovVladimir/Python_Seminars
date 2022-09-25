# minus = lambda a, b: a - b

# plus = lambda a, b: a + b

# div = lambda a, b: a / b

# multi = lambda a, b: a * b

# exponent = lambda a, b: a * b

def minus(a, b): return a - b


def plus(a, b): return a + b


def div(a, b): return a / b


def multi(a, b): return a * b


def exponent(a, b): return a ** b


def print_operation_table(action, num_row=9, num_columns=9):
    # for i in range(1, num_columns+1):
    #     print(i, end='\t')
    # print('\n')
    for i in range(1, num_row+1):
        for j in range(1, num_columns+1):
            if action == '+':
                print(plus(i, j), end='\t')
            elif action == '-':
                print(minus(i, j), end='\t')
            elif action == '*':
                print(multi(i, j), end='\t')
            elif action == '/':
                print(div(i, j), end='\t')
            elif action == '^':
                print(exponent(i, j), end='\t')
        print('\n')


action = input("Какое действие будем делать для таблицы? (+,-,*,/, ^): ")
num = int(input("до какого числа?: "))
print_operation_table(action, num, num)
