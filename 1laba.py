kod = True
while kod:
    numberlab = int(input("Введите номер задания(1-6). Нажмите ноль, если хотите выйти.\n"))
    if numberlab == 1:
        sum = 0
        i=0
        while sum <3:
            i+=1
            sum += 1/i
        print("Сумма слагаемых 1+1/2+1/3+1/4+...+1/n больше 3")
        print(i)
        kod = True

    elif numberlab == 2:
        for i in input('Введите строку: \n'):
            if i in '1234567890':
                print("числа, которые встречаются в строке:")
                print(i)
        kod = True

    elif numberlab == 3:
        s = input("введите список:").split()
        s = list(map(int, s))
        num = int(input("введите число:"))
        k = 0
        for i in s:
            if i > num:
                k+=1
        if abs(min(s)) > abs(max(s)):
            ma = min(s)
        else:
            ma = max(s)
        flag = False
        ymnoz = 1
        for i in s:
            if flag:
                ymnoz*=i
            if ma == i:
                flag = True
        s=[i for i in s if i<0]
        print("количество элементов массива, больших С:")
        print(k)
        print("произведение элементов массива, расположенных после максимального по модулю элемента:")
        print(ymnoz)
        print("удалить все положительные элементы списка:")
        print(s)
        kod = True

    elif numberlab == 4:
        s = "I love Python"
        dic = {k: s.count(k) for k in s}
        print(dic)
        kod = True

    elif numberlab == 5:

        shop = {
            "Кольцо": ["Золото", 500, 10],
            "Браслет": ["Серебро", 200, 15],
            "Серьги": ["Золото", 300, 5],
            "Ожерелье": ["Платина", 1000, 2]
        }

        while True:
            print("\nМеню:")
            print("1. Просмотр описания")
            print("2. Просмотр цены")
            print("3. Просмотр количества")
            print("4. Вся информация")
            print("5. Покупка")
            print("6. До свидания")

            choice = input("Введите номер пункта меню: ")

            if choice == "1":
                name = input("Введите название товара: ")
                if name in shop:
                    characteristic = shop[name][0]
                    print(f"{name} - {characteristic}")
                else:
                    print("Товар не найден")

            elif choice == "2":
                name = input("Введите название товара: ")
                if name in shop:
                    price = shop[name][1]
                    print(f"{name} - {price} рублей")
                else:
                    print("Товар не найден")

            elif choice == "3":
                name = input("Введите название товара: ")
                if name in shop:
                    count = shop[name][2]
                    print(f"{name} - {count} штук")
                else:
                    print("Товар не найден")

            elif choice == "4":
                for product, parameters in shop.items():
                    characteristic, price, count = parameters
                    print(f"{product}: {characteristic}, Цена: {price} рублей, Количество: {count} штук")


            elif choice == "5":
                name = input("Введите название товара (или 'n' для выхода): ")
                if name == "n":
                    break
                if name in shop:
                    while True:
                        count_input = input("Введите количество: ")
                        if count_input.isdigit():
                            count = int(count_input)
                            if count > 0:
                                if count <= shop[name][2]:
                                    price = shop[name][1]
                                    itog = count * price
                                    print(
                                        f"Вы приобрели {count} {name} по {price} рублей каждый. Общая стоимость: {itog} рублей.")
                                    shop[name][2] -= count
                                    break
                                else:
                                    print("Недостаточно товара на складе.")
                            
                        else:
                            print("Введите корректное число.")
                else:
                    print("Товар не найден")
            kod=True

    elif numberlab == 6:
        strok1 = input("Введите элементы первого множества через пробел: ")
        elements1 = strok1.split()
        mnozhestvo1 = set(map(int, elements1))

        strok2 = input("Введите элементы второго множества через пробел: ")
        elements2 = strok2.split()
        mnozhestvo2 = set(map(int, elements2))

        difference = mnozhestvo1 - mnozhestvo2

        print("Элементы первого множества, которых нет во втором множестве:", difference)

        kod = True
    elif numberlab == 0:
        kod = False
