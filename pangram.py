x = input("Enter a phrase: ")
#This phrase
""" alpha = ['a', 'b', 'c']

def is_pangram(x):
    for i in (x):
        if not i in x:
            print("false") """

def pangram(x):
    if len(x) < 26:
        return False
    n = set()
    for i in n:
        n.add(i)
    if len(n) == 26:
        return True
    return False

print(pangram(input("phrase: ")))

pangram(x)
