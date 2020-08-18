def get_info(settings_file=True):
    if settings_file:
        load_file = ""
        while load_file != "y" and load_file != "n":
            load_file = input("Would you like to load a settings file? (y/n):\n")
        if load_file == "y":
            filename = "amor_calc_settings.txt"
            try:
                with open(filename) as settings:
                    settings_str = settings.read()
                settings_list = settings_str.split(",")
                if len(settings_list) != 7:
                    raise IndexError
            except FileNotFoundError:
                cont = input("Settings file not found. Enter 'q' to quit program or any "
                             "other key to continue with new settings:\n")
                if cont == "q":
                    exit()
                else:
                    return get_info(False)
            except IndexError:
                cont = input("Settings file is in incorrect format. Enter 'q' to quit program or any "
                             "other key to continue with new settings:\n")
                if cont == "q":
                    exit()
                else:
                    return get_info(False)

            for i in range(len(settings_list)):
                settings_list[i] = float(settings_list[i])

            return settings_list

    accepted = False
    while not accepted:
        try:
            price = float(input("What is the total sale price?\n").lstrip("$"))
            if price != round(price, 2) or price < 0:
                raise ValueError
        except ValueError:
            print("Input may contain a leading dollar sign, but otherwise must be a positive"
                  "number with up to two decimal places only, please try again.\n")
            continue
        accepted = True

    accepted = False
    while not accepted:
        try:
            percent_or_amount = input("Would you like to enter the down payment as a percentage or as a dollar amount?"
                                      "\nEnter 'p' for percent, 'd' for dollar amount:\n").lower()
            if percent_or_amount != 'p' and percent_or_amount != 'd':
                raise ValueError
        except ValueError:
            print("Must enter 'p' or 'd', please try again.\n")
            continue
        accepted = True

    if percent_or_amount == 'p':
        accepted = False
        while not accepted:
            try:
                down = float(input("What is the down payment? (as a percentage, "
                                   "e.g. '20%' or '20'): \n").rstrip("%"))
                if down != round(down, 2) or down < 0:
                    raise ValueError
            except ValueError:
                print("Input may contain a trailing percentage sign, but otherwise "
                      "must be a positive number with up to two decimal places only, please try again.\n")
                continue
            if down > 100:
                print("You have chosen to enter as a percentage, down payment cannot be over 100%, please try again.\n")
                continue
            if down > 20:
                confirm = input("You have entered over a 20% down payment, "
                                "is this correct? (enter 'y' for yes):\n").lower()
                if confirm != 'y':
                    continue
            if down < 5:
                confirm = input("You have entered under a 5% down payment, "
                                "is this correct? (enter 'y' for yes):\n").lower()
                if confirm != 'y':
                    continue
            accepted = True
        down = price * (down / 100)
    else:
        accepted = False
        while not accepted:
            try:
                down = float(input("What is the down payment? (as a dollar amount, "
                                   "e.g. '$5000' or '5000'): \n").lstrip("$"))
                if down != round(down, 2) or down < 0:
                    raise ValueError
            except ValueError:
                print("Input may contain a leading dollar sign, but otherwise must be a positive "
                      "number with up to two decimal places only, please try again.\n")
                continue
            if down > price:
                print("Down payment cannot be higher than the sale price, please try again.\n")
                continue
            if down > price * .2:
                confirm = input("You have entered over a 20% down payment, "
                                "is this correct? (enter 'y' for yes):\n").lower()
                if confirm != 'y':
                    continue
            if down < price * .05:
                confirm = input("You have entered under a 5% down payment, "
                                "is this correct? (enter 'y' for yes):\n").lower()
                if confirm != 'y':
                    continue
            accepted = True

    accepted = False
    while not accepted:
        try:
            year_rate = float(input("What is the yearly interest rate? (as a percentage, "
                                    "e.g. '4.5%' or '4.5'):\n").rstrip("%"))
            if year_rate != round(year_rate, 3) or year_rate < 0:
                raise ValueError
        except ValueError:
            print("Input may contain a trailing percentage sign, but otherwise must be a positive"
                  "number with up to three decimal places only, please try again.\n")
            continue
        accepted = True

    accepted = False
    while not accepted:
        try:
            years_term = input("What is the term of the loan (in years)?\n")
            if int(years_term) < 0 or int(years_term) != float(years_term):
                raise ValueError
        except ValueError:
            print("Input must be a positive whole number only, please try again.\n")
            continue
        years_term = int(years_term)
        if years_term != 15 and years_term != 30:
            confirm = input("You have entered a term other than 15 or 30 years, "
                            "is this correct? (enter 'y' for yes)\n").lower()
            if confirm != 'y':
                continue
        accepted = True

    if down < price * .2:
        accepted = False
        while not accepted:
            try:
                pmi_cost = float(input("With a down payment of less than 20%, you may need to pay mortgage insurance,"
                                       "what is the monthly cost of the mortgage insurance? "
                                       "(enter 0 if none or unknown):\n").lstrip("$"))
                if pmi_cost != round(pmi_cost, 2) or pmi_cost < 0:
                    raise ValueError
            except ValueError:
                print("Input may contain a leading dollar sign, but otherwise must be a positive"
                      "number with up to two decimal places only, please try again.\n")
                continue
            accepted = True

    accepted = False
    while not accepted:
        try:
            escrow_pmt = float(input("What is the estimated monthly escrow payment? "
                                     "(enter 0 if none or unknown): \n").lstrip("$"))
            if escrow_pmt != round(escrow_pmt, 2) or escrow_pmt < 0:
                raise ValueError
        except ValueError:
            print("Input may contain a leading dollar sign, but otherwise must be a positive"
                  "number with up to two decimal places only, please try again.\n")
            continue
        accepted = True

    accepted = False
    while not accepted:
        try:
            addl_prin = float(input("How much extra would you like to pay toward the principal each month? "
                                    "(enter 0 if none): \n").lstrip("$"))
            if addl_prin != round(addl_prin, 2) or addl_prin < 0:
                raise ValueError
        except ValueError:
            print("Input may contain a leading dollar sign, but otherwise must be a positive"
                  "number with up to two decimal places only, please try again.\n")
            continue
        accepted = True

    save_file = ""
    while save_file != "y" and save_file != "n":
        save_file = input("Would you like to save these settings to a file? "
                          "(This will overwrite previous settings. y/n):\n")
    if save_file == "y":
        filename = "amor_calc_settings.txt"
        settings_str = ",".join([str(price), str(price - down), str(year_rate), str(years_term),
                                 str(pmi_cost), str(escrow_pmt), str(addl_prin)])
        with open(filename, "w") as settings:
            settings.write(settings_str)

# TODO: add input for FHA loan and for modular extra payments

    return price, price - down, year_rate, years_term, pmi_cost, escrow_pmt, addl_prin


def calc_payment(loan_amount, year_rate, years_term):
    month_rate = year_rate / 12 / 100
    months_term = years_term * 12
    payment = loan_amount * (month_rate * (1 + month_rate) ** months_term) / ((1 + month_rate) ** months_term - 1)
    return round(payment, 2)


def month_breakdown(principal, rate, payment):
    int_pmt = round(principal * (rate * .01) / 12, 2)
    prin_pmt = round(payment - int_pmt, 2)
    if prin_pmt > principal:
        prin_pmt = principal
    return int_pmt, prin_pmt


sale_price, st_balance, int_rate, term, pmi, escrow, extra_prin = get_info()
balance = st_balance
pmt = calc_payment(st_balance, int_rate, term)
# 505.90
# sale_price = 154900.0
# st_balance = 147155.0
# balance = st_balance
# int_rate = 2.75
# pmt = 600.75
# escrow = 294.31
first_payment_prin = 0.0
# extra_prin = 0.0
# pmi = 53.96
pmt_num = 1
month = 0
year = 0
total_int = 0.0
amor_str = ""
if first_payment_prin != 0:
    first_pay_str = f"Initial principal payment: ${first_payment_prin:.2f}; "
else:
    first_pay_str = ""
start_str = f"\nStarting balance: ${st_balance:.2f}; Monthly Payment: ${pmt + extra_prin + escrow + pmi:.2f}" \
            f"; {first_pay_str}Extra Monthly Principal Payment: ${extra_prin:.2f}."

while balance > 0:
    if balance <= sale_price * .78 or pmi == 0:
        pmi = 0.0
        pmi_str = ""
    else:
        pmi_str = f"PMI: ${pmi:.2f}, "
    int_pmt, prin_pmt = month_breakdown(balance, int_rate, pmt)
    if first_payment_prin:
        balance = round(balance - prin_pmt - first_payment_prin, 2)
        extra_str = f"Additional principal: ${first_payment_prin:.2f}, "
        first_payment_prin = None
    elif int_pmt + prin_pmt < pmt:
        balance = round(balance - prin_pmt, 2)
        extra_str = ""
        extra_prin = 0
    else:
        balance = round(balance - prin_pmt - extra_prin, 2)
        if extra_prin == 0:
            extra_str = ""
        else:
            extra_str = f"Additional principal: ${extra_prin:.2f}, "
    total_int = round(total_int + int_pmt, 2)
    pmt_str = f"{pmt_num}-- " \
              f"Total Payment: ${int_pmt + prin_pmt + extra_prin + escrow + pmi:.2f} " \
              f"Interest: ${int_pmt:.2f}, " \
              f"Principal: ${prin_pmt:.2f}, " \
              f"{extra_str}" \
              f"{pmi_str}" \
              f"Escrow: ${escrow:.2f}, " \
              f"Remaining Balance: ${balance:.2f}"
    amor_str = "\n".join([amor_str, pmt_str])
    pmt_num += 1
    month += 1
    if month == 12:
        month = 0
        year += 1

if month == 1:
    s = ""
else:
    s = "s"
finish_str = f"\nTotal Term: {year} years, {month} month{s}. Total interest paid: ${total_int:.2f}\n"
print(start_str)
print(amor_str)
print(finish_str)

save_file = ""
while save_file != "y" and save_file != "n":
    save_file = input("Write results to file? (y/n):\n")
if save_file == "y":
    filename = input("Enter a file name:\n")
    with open(filename, "w") as write_file:
        write_file.write(start_str)
        write_file.write("\n___________________________________________________________________________________________"
                         "____________________________________________________________________________________________")
        write_file.write("\n")
        write_file.write(amor_str)
        write_file.write("\n")
        write_file.write(finish_str)
