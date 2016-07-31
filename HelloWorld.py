try:
    mylist=['A','B','C']
    while True:
        print(mylist.pop())
        assert len(mylist)>=1
except AssertionError:
    print('Nothing left!')
finally:
    print("save it")
