class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent} "


mails = []
while True:
    command = input().split()
    if command[0] == 'Stop':
        break
    the_sender = command[0]
    the_receiver = command[1]
    the_content = command[2]
    email = Email(the_sender, the_receiver, the_content)
    mails.append(email)

send_email = [mails[int(x)].send() for x in input().split(', ')]
for mail in mails:
    print(mail.get_info())