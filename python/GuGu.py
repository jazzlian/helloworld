def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1

    return result

if __name__ == '__main__':
    print(GuGu(2))