import time

start = time.time()


def all_variants(text):
    print(f'Количество элементов: {len(text)}')
    count = 0  # интересно, сколько получается комбинаций? считает, но длительность примерно в 2 раза больше
    for i in range(1, len(text) + 1):
        for n in range(0, len(text) - i + 1):
            k = n + i
            if k == len(text):
                k = None
            comb = text[n:k]
            # yield comb
            count += 1
            yield f'{count}. {comb}'


a = all_variants("abcdefghijklmnopqrstuvwxyz")  # 3 элемента можно и вручную перебрать:)
for i in a:
    print(i)

fin = time.time()
print(f'Время выполнения: {round((fin - start) * 1000, 3)} мс')  # Время разное: от 0,997 до 5,053 мс (10 запусков кода)
