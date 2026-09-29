def calc():
    a = float(input("عدد اول: "))
    op = input("عملگر (+ - * /): ")
    b = float(input("عدد دوم: "))

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("تقسیم بر صفر نمی‌شود")
        else:
            print(a / b)
    else:
        print("عملگر نامعتبر")

calc()