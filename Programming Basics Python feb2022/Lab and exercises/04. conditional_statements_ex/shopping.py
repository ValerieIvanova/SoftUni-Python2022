budget = float(input())
n_count = int(input())
m_count = int(input())
p_count = int(input())

n_sum = n_count * 250
m_price = n_sum * 0.35
m_sum = m_count * m_price
p_price = n_sum * 0.10
p_sum = p_count * p_price
total_sum = n_sum + m_sum + p_sum

if n_count > m_count:
    total_sum -= total_sum * 0.15

diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")