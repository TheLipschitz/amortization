def month_breakdown(principal, rate, payment):
    int_pmt = round(principal * (rate * .01) / 12, 2)
    prin_pmt = round(payment - int_pmt, 2)
    if prin_pmt > principal:
        prin_pmt = principal
    return int_pmt, prin_pmt


sale_price = 154900.0
balance = 147155.0
int_rate = 2.75
pmt = 600.75
escrow = 294.31
first_payment_prin = 23235.0
extra_prin = 0.0
pmi = 0.0
pmt_num = 1
month = 0
year = 0
total_int = 0.0
# save_file = ""
# while save_file != "y" or save_file != "n":


while balance > 0:
    if balance <= sale_price * .80:
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
        extra_str = f"Additional principal: ${extra_prin:.2f}, "
    total_int = round(total_int + int_pmt, 2)
    print(f"{pmt_num}-- "
          f"Total Payment: ${int_pmt + prin_pmt + extra_prin + escrow + pmi:.2f} "
          f"Interest: ${int_pmt:.2f}, "
          f"Principal: ${prin_pmt:.2f}, "
          f"{extra_str}"
          f"{pmi_str}"
          f"Remaining Balance: ${balance:.2f}")
    pmt_num += 1
    month += 1
    if month == 12:
        month = 0
        year += 1

if month == 1:
    s = ""
else:
    s = "s"
finish_str = f"Paid for {year} years, {month} month{s}. Total interest paid: ${total_int:.2f}"
print(finish_str)
