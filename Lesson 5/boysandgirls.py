# -*- encoding: utf8 -*-

import itertools
from fractions import Fraction

sex = 'BG'

def product(*variables):
	"The cartesian product (as a str) of the possibilities for each variable."
	return map(''.join, itertools.product(*variables))
	
two_kids = product(sex, sex)
print two_kids	
	
one_boy = [s for s in two_kids if 'B' in s]

def two_boys(s): return s.count('B') == 2

def cond_p(predicate, event):
	"""Conditional probability: P(predicate(s) | s in event).
	The proportion of states in event for which the predicate is true."""
	pred = [s for s in event if predicate(s)]
	return Fraction(len(pred), len(event))
	
print cond_p(two_boys, one_boy)	
	
"""Out of all families with 2 kids with at least one boy born on Tuesday,
what is the probability of two boys?"""
day = 'SMTWtFs'

two_kids_bday = product(sex, day, sex, day)
print two_kids_bday

boy_anyday = [s for s in two_kids_bday if 'B' in s]

boy_on_tuesday = [s for s in two_kids_bday if 'BT' in s]
print boy_on_tuesday

print cond_p(two_boys, boy_on_tuesday)

month = 'DJFMAmjUASON'
two_kids_month = product(sex, month, sex, month)
boy_december = [s for s in two_kids_month if 'BD' in s]

def report(verbose=False, predicate=two_boys, pred_name='two_boys',
		cases= [('2 kids', two_kids), ('2 kids born ony day', two_kids_bday),
			('at least one boy', one_boy),
			('at least one boy born any day', boy_anyday),
			('at least one boy born on Tuesday', boy_on_tuesday),
			('at least one boy born in December', boy_december)]):
	import textwrap
	for (name, event) in cases:
		print ('P(%s | %s) = %s' % (pred_name, name, cond_p(predicate, event)))
		if verbose:
			print ('Reason:\n"%s" has %d elements:\n%s' % (
				name, len(event), textwrap.fill(' '.join(event), 85)))
			good = [s for s in event if predicate(s)]
			print ('of those, %d are "%s":\n%s\n\n' % (
				len(good), pred_name, textwrap.fill(' '.join(good), 85)))
				
report()				
			
