calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(a):
    count_calls()
    a = '(' + str(len(a)) + ', "' + a.upper() + '", "' + a.lower() + '")'
    print(a)


def is_contains(b=str(), c=[]):
    c = [item.lower() for item in c]
    count_calls()
    if any(item in b.lower() for item in c):
        return True
    else:
        return False


string_info('Capybara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
string_info('Distruction')
string_info('Emansipation')
print(is_contains('SaMoKaT', ['Samara', 'SAMARKAND', 'SAMOkat']))
print(is_contains('one', ['two', 'three', 'four']))
print(calls)
