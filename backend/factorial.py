def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.

  Args:
      n: The non-negative integer for which to calculate the factorial.

  Returns:
      The factorial of n.

  Raises:
      ValueError: If n is negative.
  """

  if n < 0:
    raise ValueError("n must be non-negative")

  if n == 0:
    return 1

  result = 1
  for i in range(1, n + 1):
    result *= i

  return result
