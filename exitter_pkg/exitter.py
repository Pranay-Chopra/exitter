import sys
def bye():
    q=input("Quit? (y/n)")
    if q=='y' or q=='Y':
        sys.exit()
    elif q=='n' or q=='N':
        pass
    else:
        bye()
