import heapq

def combine_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        new_cable = cable1 + cable2
        connection_cost = cable1 + cable2
        total_cost += connection_cost

        heapq.heappush(cables, new_cable)

    return total_cost

try:
    num_cables = int(input("Введіть кількість кабелів: "))
    if num_cables < 2:
        raise ValueError("Кількість кабелів повинна бути не менше 2")
    
    cables_input = input(f"Введіть довжини кожного з кабелів через пробіл для розрахунку: ")
    cables = list(map(int, cables_input.split()))

    if len(cables) != num_cables:
        raise ValueError(f"Очікується {num_cables} довжина кабелів")

    result = combine_cables(cables)
    print("Загальні витрати:", result)

except ValueError as ve:
    print(f"Помилка: {ve}")
