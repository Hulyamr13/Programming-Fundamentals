def palindrome(s, palin):
    palindromes_lst = []
    lst = s.split(" ")
    palin_counter = 0
    for i in lst:
        test = i[::-1] == i
        if test:
            palindromes_lst.append(i)
        if i == palin:
            palin_counter += 1

    print(palindromes_lst)
    print(f"Found palindrome {palin_counter} times")


text = input()
p = input()
palindrome(text, p)