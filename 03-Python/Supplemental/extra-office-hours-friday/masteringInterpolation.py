msg = 'Python rocks!'
num = 8
print('*************************')
print('Old string formatting with % ')
print('*************************')

print(f'Hey Dana.... here is my message: %s' % msg)
print('                            ')

print(msg)

print('*************************')
print('Using string.format')
print('*************************')
print('here is my message Dana: {1} and your number is {0}'.format(num,msg))
print(' ' * 50)

#To simplify formatting even further, in 2015, Eric Smith proposed the PEP 498 -- Literal String Interpolation .
print('*************************')
print('Using Interpolation')
print('*************************')
print(f'HERE is my message..... : {msg}')
print(' ' * 53)


# Let's practice some more.... this time we want our OUTPUT to have double quotes in it.
# therefore, we will use '' single quotes for our f'string formatting.
book = "The dog guide"
num_pages = 124
print(f'The book "{book}" has {num_pages} pages\n')
print(' ' * 53)

#HARDCODED below ... explaning the use of "" double quotes and '' single quotes
print("CARLOS .... is in California and reading 'TypeScript' and it has 234 pages.")


print('*'*70)
print('Using Interpolation, and working with expressions')
print('*'*70)
print(' ' * 53)

print(f"4 * 4 is {4 * 4}")  # NOTE: We have an expression inside curly brackets


print('*'*70)
print('FORMATTING: Set Float Number Precision in a F-String')
print('*'*70)
print(' ' * 53)

num = 4.125956

print(f'num rounded to 2 decimal places = {num: .2f}')
print(f'Original num variable {num}')
print('\n')

bigbudget = 1234567890

print('*'*70)
print(f"{bigbudget:,}".replace(',', ' '))
print('*'*70)
