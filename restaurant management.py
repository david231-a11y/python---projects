print('1: Noodles')
print('2: Fried rice')
print('3: Garri and egusi soup')
def AllMenu():
 menu=int(input('Menu:'))
 if menu==1:
    total=int(input('Total of portion:'))
    print("$", total * 1.5)
    return AllMenu()
 elif menu==2:
    total=int(input('Total of portion:'))
    print("$", total * 1)
    return AllMenu()
 elif menu==3:
    total=int(input('Total of portion:'))
    print("$", total * 2)
    return AllMenu()

AllMenu()