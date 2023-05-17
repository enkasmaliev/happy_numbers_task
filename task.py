def find_happy_numbers(n, k):
    def is_happy_number(num):
        digits_sum = 0
        prev_digit = -1
        for digit in str(num):
            if int(digit) < prev_digit:
                return False
            digits_sum += int(digit)
            prev_digit = int(digit)
        return digits_sum == n

    happy_numbers = []
    for num in range(10**(k-1), 10**k):
        if is_happy_number(num):
            happy_numbers.append(num)

    return [len(happy_numbers), str(min(happy_numbers)), str(max(happy_numbers))]
