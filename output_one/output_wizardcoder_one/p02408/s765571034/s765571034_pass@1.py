m_cards = set()
for i in range(int(input())):
    m, n = input().split()
    if (m not in m_cards) and int(n) >= 1 and int(n) <= 13:
        print(f"{m} {n}")
        m_cards.add(m)