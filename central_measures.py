def central_measures(numbers):
    mean = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers)//2]
    d = {n:numbers.count(n) for n in set(numbers)}
    mode = [k for k, v in d.items() if v == max(d.values())][0]
    # mode = max(set(numbers), key=numbers.count)
    return mean, median, mode

# -------------------------------------------------------------------------


if __name__ == '__main__':
    import random
    numbers = [round(random.gauss(50, 20)) for __ in range(100)]

    mean, median, mode = central_measures(numbers)

    print(numbers)
    print('Mean:   %8.2f' % mean)
    print('Median: %8d' % median)
    print('Mode:   %8d' % mode)
