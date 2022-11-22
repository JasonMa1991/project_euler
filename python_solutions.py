
def problem_1():
  # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
  # Find the sum of all the multiples of 3 or 5 below 1000.

  running_sum = 0
  for num_to_test in range(1, 1000):
    if (num_to_test % 3 == 0) or (num_to_test % 5 == 0):
      running_sum += num_to_test

  print(f'Sum of all the multiples of 3 or 5 below 1000 is: {running_sum}')


def problem_2():
  # Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
  # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
  # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

  LIMIT_2 = 4_000_000


  fib_0 = 1
  fib_1 = 2
  sum_even = 2
  while fib_1 < LIMIT_2:
    fib_1 = fib_0 + fib_1
    fib_0 = fib_1 - fib_0

    if fib_1 % 2 == 0:
      sum_even += fib_1

  print(f'Sum of even-valued fibonacci values less than 4,000,000: {sum_even}')


def problem_29():
  # Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

  # 22=4, 23=8, 24=16, 25=32
  # 32=9, 33=27, 34=81, 35=243
  # 42=16, 43=64, 44=256, 45=1024
  # 52=25, 53=125, 54=625, 55=3125
  # If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

  # 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

  # How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

  LOWER_LIMIT_29 = 2
  UPPER_LIMIT_29 = 100

  distinct_terms = set()

  for a in range(LOWER_LIMIT_29, UPPER_LIMIT_29 + 1):
    for b in range(LOWER_LIMIT_29, UPPER_LIMIT_29 + 1):
      term = a ** b
      distinct_terms.add(term)

  num_distinct_terms = len(distinct_terms)
  print(f'Distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100: {num_distinct_terms}')


def problem_30():
  # Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

  # 1634 = 14 + 64 + 34 + 44
  # 8208 = 84 + 24 + 04 + 84
  # 9474 = 94 + 44 + 74 + 44
  # As 1 = 14 is not a sum it is not included.

  # The sum of these numbers is 1634 + 8208 + 9474 = 19316.

  # Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

  POWER_30 = 5
  # set max to 290,000 since we observe that 2^5 + 9^5 * 5 = 295277
  MAX_TO_TEST_30 = 290_000

  matching_numbers = []
  for test_num in range(10, MAX_TO_TEST_30):
    digit_powers = [
      int(digit) ** POWER_30 for digit in str(test_num)
      ]
    sum_powers = sum(digit_powers)
    if sum_powers == test_num:
      matching_numbers.append(test_num)
      print(test_num)

  print(f'Sum of all the numbers that can be written as the sum of fifth powers of their digits: {sum(matching_numbers)}')


if __name__ == '__main__':
  problem_30()
