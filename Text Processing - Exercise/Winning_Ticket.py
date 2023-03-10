tickets = input().replace(" ", "")
tickets = tickets.split(",")
special_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    jackpot_win = False
    normal_win = False
    symbols = 0
    if len(ticket) == 20:
        first_half = ticket[:len(ticket) // 2]
        second_half = ticket[len(ticket) // 2:]
        for symbol in special_symbols:
            if 20 * symbol in ticket:
                jackpot_win = True
                break

            elif 6 * symbol in first_half and 6 * symbol in second_half:
                symbols = 6
                for index in range(7, 11):
                    if index * symbol in first_half and index * symbol in second_half:
                        symbols += 1
                normal_win = True
                break

        if normal_win:
            print(f'ticket "{ticket}" - {symbols}{symbol}')
        elif jackpot_win:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        elif not normal_win and not jackpot_win:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")