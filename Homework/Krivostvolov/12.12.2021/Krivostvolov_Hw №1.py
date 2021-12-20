from random import randint
ticket = []
uncountable = 0
countable = 0
for i in range (6):
    ticket.append(randint(1, 9))
print(ticket)
s_num_1 = ticket [0] + ticket [1] + ticket [2]
s_num_2 = ticket [3] + ticket [4] + ticket [5]
if s_num_1 == s_num_2:
    print ('It`s a lucky ticket')
else:
    print ('It`s unlucky ticket')

for num_1 in ticket:
    if num_1 % 2 == 0:
        for countable in num_1:
            countable += num_1
for num_2 in ticket:
    if num_2 % 2 == 1:
        for uncountable in num_2:
            uncountable += num_2
print(countable)
print(uncountable)