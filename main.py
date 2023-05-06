# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from split import split as split
def print_hi(message):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {message}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Let''s split some ROs!')
    my_ro = input('Give me RO: ')
    a, b = split(my_ro)
    print(f'RO: {a}')
    print(f'CUI: {b}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
