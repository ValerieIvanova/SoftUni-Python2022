def user_present():
    present = False
    for u in sides.values():
        if force_user in u:
            present = True
            break
    return present


def add_user(side_, user_):
    if side_ not in sides:
        sides[side_] = [user_]
    else:
        sides[side_].append(user_)
    return sides


def change_side(side_, user_):
    for side, users in sides.items():
        if user_ in users:
            sides[side].pop(users.index(user_))
            break
    if side_ not in sides:
        sides[side_] = [force_user]
    else:
        sides[side_].append(user_)
    return sides


sides = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')
        if not user_present():
            add_user(force_side, force_user)

    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        change_side(force_side, force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, members in sides.items():
    if len(sides[side]) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        [print(f"! {user}") for user in sides[side]]