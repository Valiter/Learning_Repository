def del_func():
    x = input("First num.: ")
    print(f'F.num.: {x}')
    y = input("Second num.: ")
    print(f'S.num.: {x}')
    try:
        z = int(x) / int(y)
        print(f"Result: {z}")
    except:
        print(f"Error: {err}")

del_func()