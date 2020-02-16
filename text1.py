#δημιουργουμε την λιστα
import itertools
t = [1,2,3,4,5,6,7,8]
c = list(itertools.combinations(t, 4))
unq = set(c)