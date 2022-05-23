name = input()
adult_ticket_count = int(input())
child_ticket_count = int(input())
net_price_adult_ticket = float(input())
tax = float(input())

net_price_of_child_ticket = net_price_adult_ticket - (net_price_adult_ticket * 0.7)
price_of_adult_ticket_with_tax = net_price_adult_ticket + tax
price_of_child_ticket_with_tax = net_price_of_child_ticket + tax
totall_price_of_tickets = (adult_ticket_count * price_of_adult_ticket_with_tax) + (child_ticket_count *
                                                                                   price_of_child_ticket_with_tax)
income = (f'{totall_price_of_tickets * 0.2:.2f}')

print(f"The profit of your agency from {name} tickets is {income} lv.")