# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
x = [1, 3, 4]
print(x.pop(0))
print(x)
board = [['___'], ['___'], ['___']]
lst = []
for row in board:
    for ch in row:
        lst.append(' '.join(ch))
print('\n'.join(lst))


def cell_list(b):
    lst = []
    for i in range(len(b)):
        for j in range(len(b)):
            lst.append((i, j))
    lst.append((3, 7))
    return lst


print(cell_list(board))

b = {1:2, 2:3}
print(b)
print(b.items())


a = [(1, 2), (2,4)]
print(a)
print(*a)
user_input = "Y,r"
print(user_input)
user_input = user_input.split(",")
print(user_input)
name, movekey = user_input
print(name)
print(movekey)
