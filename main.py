    import tkinter as tk
    import tkinter.simpledialog

    STOCK_FILE = open('STOCK_FILE.txt', 'r')


    def login():
        w = tk.Tk()
        w.withdraw()
        username = tk.simpledialog.askstring('Username:', 'Username')
        print(username)
        password = tk.simpledialog.askstring('Password:', 'Password', show='*')
        print(password)

        user_list = open('users.txt', 'r')

        for l in user_list:
            group = l.split(':')
            if username == group[0] and password == group[1]:
                return True
            else:
                return False


    def calc_check(gtin):
        gtin_check_sum = 0
        calc_check_iterate = 0
        iteration_control = 1
        if len(str(abs(gtin))) == 7:
            for n in str(gtin):
                if iteration_control % 2 != 0:
                    gtin_check_sum += int(n) * 3
                else:
                    gtin_check_sum += int(n)
                iteration_control += 1
        else:
            print('Error. GTIN not correct length')

        if gtin_check_sum % 10 == 0:
            gtin_check = 0
            return gtin_check
        else:
            while gtin_check_sum % 10 != 0:
                gtin_check_sum += 1
                calc_check_iterate += 1
                if gtin_check_sum % 10 == 0:
                    gtin_check = calc_check_iterate
                    return gtin_check


    def validate(gtin):
        if len(str(abs(gtin))) == 8:
            valid = False
            gtin_str = str(gtin)
            gtin_no_check = gtin_str[8]
            if gtin_no_check == str(calc_check(gtin)):
                valid = True
                return valid
            else:
                return valid

    def add_product():
        product_string = ''
        if login():

        else:
