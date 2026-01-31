def add_many(choice, *args):
    if choice =="add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result

result = add_many('add',1,2,3,4)
print(result)

result = add_many('mul',1,2,3,4)
print(result)