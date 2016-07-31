#test lambda
def rept(n):
    return lambda s:s*n
twice=rept(2)
print(twice('word'))
print(twice(5))
