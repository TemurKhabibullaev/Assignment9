# Temur Khabibullaev 4/1/2020


def palindrome_check(string):
    if len(string) <= 1:
        return 'yes'
    if string[0] != string[-1]:
        return 'no'
    else:
        return palindrome_check(string[1: -1])


while True:
    string = input('Enter the string, and I\'ll check if it is a palindrome:\n>>>')
    string = string.strip()
    string = string.lower()
    print(palindrome_check(string))