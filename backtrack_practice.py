# write over here


#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 

# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def generateParenthesis(n):
  ans = []
  self.helper(n, ans)
  return res

def helper(self, n, ans, ""):
  if n == 0:
    return
  if string == "":
    string += "("

# incremental solution
# solving small problems



#   dfasdfasdfsda
- when can you place an open parenthesis?
- when can you place a closed parenthesis?
- when are you finished?
- what is the mathematical proof that this works?
- how does this fit the structure of a back tracking problem


# mathematical proof by induction
# identify base case
# identify the inductive/hypothesis step

generateParen(ans, opening, close, curr): # ans;
  # base case
  if (opening == 0 and close == 0):
     ans.append(curr)
     return

  if (okay to open)
    curr += "("
    recur()

  if (okay to close)
    curr += ")"
    recur()
    curr = curr[0..-1]

  return;
  # assuming i can solve subproblems, how can i solve current problem?

  # when curr == ((()))()()()(() ????

n = 3

(
((
(((
((()
((())
((()))
  meets base case
  pushes into answer
((())
.
(


# some arbitrary curr
# find all solutions to curr + (
# return the state to curr
# find all solutiosn to curr + )
# curr )
# ( (
# ( )


# mathematical proof by induction
# identify base case
# identify the inductive/hypothesis step


(()())

  # curr + "("


  # curr + ")"

open - (int) for open
close - (int)

#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"

# 1. recognize it can be solved with solutions to subproblems
# 2. find base case
# 3. solve n step with solutions to 0...n-1th step
#   a. if backtracking show state, and how you return state to original form such that the inductive proof still holds