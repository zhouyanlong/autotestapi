# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import testtool.test
import sys,os
curPath = os.path.abspath(__file__)
rootPath = os.path.split(curPath)[0]
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(curPath)
    print(rootPath)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
