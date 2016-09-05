# -*- encoding: utf8 -*-
# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 

import itertools

def more_pour_problem(capacities, goal, start=None):
	"""The first argument is a tuple of capacities (numbers) of glasses; the
	goal is a number which we must achieve in some glass.  start is a tuple
	of starting levels for each glass; if None, that means 0 for all.
	Start at start state and follow successors until we reach the goal.
	Keep track of frontier and previously explored; fail when no frontier.
	On success return a path: a [state, action, state2, ...] list, where an
	action is one of ('fill', i), ('empty', i), ('pour', i, j), where
	i and j are indices indicating the glass number."""
	# your code here
	def is_goal(state):
		#print 'IG', state
		return goal in state
		
	start_ = tuple([0] * len(capacities)) if start is None else start
	return shortest_path_search(start_, successors, is_goal, capacities)
	
def successors(state, capacities):
	""" state is a tuple of volumes; returns one of ('fill', i), ('empty', i), ('pour', i, j) 
	where i,j - glass indixes """	
	result = dict()
	for i in range(len(capacities)):
#		print 'I: ', i, 'C: ', capacities, 'S: ', state
		capacities_ = list(state)
		capacities_[i] = capacities[i]
		result[tuple(capacities_)] = ('fill', i)
		capacities_ = list(state)
		capacities_[i] = 0
		result[tuple(capacities_)] = ('empty', i)
	for (a, b) in itertools.permutations(range(len(capacities)), 2):
		state_ = list(state)
		if state[a]+state[b] <= capacities[b]: 
			state_[b] = state_[a] + state_[b]
			state_[a] = 0
			result[tuple(state_)] = ('pour', a, b)
		else:
			state_[a] = state_[a] - (capacities[b] - state_[b])
			state_[b] = capacities[b]
			result[tuple(state_)] = ('pour', a, b)
	#print '============== RESULT ', result
	return result
	
def shortest_path_search(start, successors, is_goal, capacities):
	"""Find the shortest path from start state to a state
	such that is_goal(state) is true."""
	if is_goal(start):
		return [start]
	explored = set()
	frontier = [ [start] ] 
	#print 'F:', frontier
	while frontier:
		path = frontier.pop(0)
		s = path[-1]
		#print 'S', s
		for (state, action) in successors(s, capacities).items():
			if state not in explored:
				explored.add(state)
				path2 = path + [action, state]
				if is_goal(state):
					return path2
				else:
					frontier.append(path2)
	return Fail

Fail = []
	
def test_more_pour():
	print more_pour_problem((1, 2, 4, 8), 4)
	assert more_pour_problem((1, 2, 4, 8), 4) == [
		(0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
	assert more_pour_problem((1, 2, 4), 3) == [
		(0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
	starbucks = (8, 12, 16, 20, 24)
	assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
	assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
	assert more_pour_problem((1, 3, 9, 27), 28) == []
	return 'test_more_pour passes'

print test_more_pour()
