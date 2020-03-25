def generate_parens(n):
  if n == 0:
    return []
  return generate_parens_helper('', n, 0)

def generate_parens_helper(curr, num_available, num_unclosed):
  if num_available == 0:
    return [curr + ')' * num_unclosed]
  elif num_unclosed == 0:
    return generate_parens_helper(curr + '(', num_available - 1, num_unclosed + 1)
  return generate_parens_helper(curr + '(', num_available - 1, num_unclosed + 1) + generate_parens_helper(curr + ')', num_available, num_unclosed - 1)

print(generate_parens(3))