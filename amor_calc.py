def month_breakdown(principal, rate, payment, extra=0.0):
    int_pmt = round(principal * (rate * .01) / 12, 2)
    prin_pmt = round(payment - int_pmt + extra, 2)
    if prin_pmt > principal:
        prin_pmt = principal
    return int_pmt, prin_pmt


sale_price = 154900.0
balance = 147155.0
int_rate = 2.75
pmt = 600.75
first_payment_prin = 23235.0
extra_prin = 100
pmi = 53.96
pmt_num = 1
month = 0
year = 0
total_int = 0.0


while balance > 0:
    if balance < sale_price * .78:
        pmi = 0.0
    if pmt_num == 1:
        int_pmt, prin_pmt = month_breakdown(balance, int_rate, pmt, first_payment_prin)
    else:
        int_pmt, prin_pmt = month_breakdown(balance, int_rate, pmt, extra_prin)
    balance = round(balance - prin_pmt, 2)
    total_int = round(total_int + int_pmt, 2)
    print(f"{pmt_num}: Interest: ${int_pmt:.2f}, "
          f"Principlal: ${prin_pmt:.2f}, "
          f"PMI: ${pmi:.2f}, "
          f"Rmaining Balance: ${balance:.2f}")
    pmt_num += 1
    month += 1
    if month == 12:
        month = 0
        year += 1

print(f"Paid for {year} years, {month} months. Total interest paid: ${total_int:.2f}.")
