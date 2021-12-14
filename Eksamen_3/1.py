def numb_card(card):
    return '*' * (len(card)-4) + card[-4:]
print(numb_card("1234567890"))
