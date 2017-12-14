ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'A':'a@a.com',
    'B':'b'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Larry']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['Tang'] = 'tang@qq.com'

if 'Tang' in ab:
    print("\nTang's address is", ab['Tang'])
