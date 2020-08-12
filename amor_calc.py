def month_breakdown(principal, rate, payment, extra=0.0):
    int_pmt = round(principal * (rate * .01) / 12, 2)
    prin_pmt = round(payment - int_pmt + extra, 2)
    return int_pmt, prin_pmt

sale_price = 154900.0
balance = 147155.0
int_rate = 2.75
pmt = 600.75
extra_princ = 0
pmi = 53.96
pmt_num = 1
month = 0
year = 0


while balance > 0:
    if balance < sale_price * .78:
        pmi = 0.0
    int_pmt, prin_pmt = month_breakdown(balance, int_rate, pmt, extra_princ)
    balance = round(balance - prin_pmt, 2)
    print(f"{pmt_num}: Interest: ${int_pmt:.2f}, "
          f"Principlal: ${prin_pmt:.2f}, "
          f"PMI: ${pmi:.2f}, "
          f"Rmaining Balance: ${balance:.2f}")
    pmt_num += 1
    month += 1
    if month > 11:
        month = 0
        year += 1

print(f"Paid for {year} years, {month} months with ${balance:.2f} left.")
