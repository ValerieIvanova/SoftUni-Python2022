class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    command = input()
    if command == 'End':
        print(f"Going: {', '.join(party.people)}")
        print(f"Total: {len(party.people)}")
        break
    name = command
    party.people.append(name)