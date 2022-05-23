bottles = int(input())
detergent_quantity = bottles * 750
used_detergent = 0
loads = 0
pots = 0
dishes = 0
enough = True
while True:
    all_kind_dishes = input()
    if all_kind_dishes == 'End':
        break
    loads += 1
    if loads % 3 == 0:
        pots += int(all_kind_dishes)
        used_detergent += int(all_kind_dishes) * 15
        if used_detergent > detergent_quantity:
            enough = False
            diff = abs(used_detergent - detergent_quantity)
            print(f'Not enough detergent, {diff} ml. more necessary!')
            break
        continue
    dishes += int(all_kind_dishes)
    used_detergent += int(all_kind_dishes) * 5
    if used_detergent > detergent_quantity:
        enough = False
        diff = abs(used_detergent - detergent_quantity)
        print(f'Not enough detergent, {diff} ml. more necessary!')
        break
if enough:
    diff = abs(used_detergent - detergent_quantity)
    print('Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {diff} ml.')