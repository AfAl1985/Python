pack = []
decode = []
bad_packs = 0

packs_amt = int(input('Number of packs: '))

for i_pack_num in range(packs_amt):
    print('\nNumber of a pack', i_pack_num + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'bit:', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Lots fo errors.')
        bad_packs += 1
    pack = []

print('\n',decode)
print('number of errors: ', decode.count(-1))
print('Lost packs: ', bad_packs)