def month_breakdown(principal, rate, payment):
    int_pmt = round(principal * (rate * .01) / 12, 2)
    prin_pmt = round(payment - int_pmt, 2)
    if prin_pmt > principal:
        prin_pmt = principal
    return int_pmt, prin_pmt


sale_price = 154900.0
st_balance = 123920.0
balance = st_balance
int_rate = 2.75
pmt = 505.90
escrow = 294.31
first_payment_prin = 0.0
extra_prin = 100.00
pmi = 0
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