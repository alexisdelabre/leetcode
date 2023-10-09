import math

def isSymmetric(root) -> bool:
    window = 1
    while root != []:
        print('sub window')
        print()
        string = ''.join([str(el) for el in root[0:window]])
        if string != string[::-1]:
            return False

        root = root[window:]
        print('res')

        print(root)
        window *= 2
        print('window: ', window)

isSymmetric([1,2,2,3,4,4,3])