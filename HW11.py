states = [0, 1, 2]
final = [0,2]
initial = 0
transitions = [[0, "a", 1], [1, "a", 1], [1, "b", 2], [2, "b", 2],[2 ,"a", 1]]

fsa = FSA(states, initial, final, transitions)

strings_to_test = ["", "a", "b", "ab", "aba", "abb", "abab", "ababb", "babab", "abbb", "abbba"]

for s in strings_to_test:
    print(s.rjust(10), fsa.evaluate(s))
