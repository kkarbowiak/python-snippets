def for_(start, stop):
    print('-> for loop from {} to {}'.format(start, stop))
    for i in range(start, stop):
        print(i)
    print('<-\n')

def for_c(start, stop, con):
    print('-> for loop from {} to {} with continue {}'.format(start, stop, con))
    for i in range(start, stop):
        print(i)
        if i == con:
            continue
    print('<-\n')

def for_b(start, stop, bre):
    print('-> for loop from {} to {} with break {}'.format(start, stop, bre))
    for i in range(start, stop):
        print(i)
        if i == bre:
            break
    print('<-\n')

def for_e(start, stop):
    print('-> for loop from {} to {} with else'.format(start, stop))
    for i in range(start, stop):
        print(i)
    else:
        print('else')
    print('<-\n')

def for_ce(start, stop, con):
    print('-> for loop from {} to {} with continue {} and else'.format(start, stop, con))
    for i in range(start, stop):
        print(i)
        if i == con:
            continue
    else:
        print('else')
    print('<-\n')

def for_be(start, stop, bre):
    print('-> for loop from {} to {} with break {} and else'.format(start, stop, bre))
    for i in range(start, stop):
        print(i)
        if i == bre:
            break
    else:
        print('else')
    print('<-\n')

def for_cbe(start, stop, con, bre):
    print('-> for loop from {} to {} with continue {}, break {}, and else'.format(start, stop, con, bre))
    for i in range(start, stop):
        print(i)
        if i == con:
            continue
        if i == bre:
            break
    else:
        print('else')
    print('<-\n')

for_(0, 0)
for_(0, 1)
for_(0, 5)
for_c(0, 0, 2)
for_c(0, 1, 2)
for_c(0, 5, 2)
for_b(0, 0, 3)
for_b(0, 1, 3)
for_b(0, 5, 3)
for_e(0, 0)
for_e(0, 1)
for_e(0, 5)
for_ce(0, 0, 2)
for_ce(0, 1, 2)
for_ce(0, 5, 2)
for_be(0, 0, 3)
for_be(0, 1, 3)
for_be(0, 5, 3)
for_cbe(0, 0, 2, 3)
for_cbe(0, 1, 2, 3)
for_cbe(0, 5, 2, 3)
