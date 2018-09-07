#!/bin/env python

import csv
import numpy
import pprint

reader = csv.DictReader(open('data.csv'))
people = list(reader)

interesting = {'Eyes', 'Hair Length', 'Gender', 'Cheeks', 'Frown', 'Hat', 'Hair Color', 'Mouth', 'Nose', 'Smile', 'Hair Shape', 'Glasses', 'Beard'}

def entropy(population):
	if len(population) == 0:
		return 0
	else:
		#each individual belongs to their own class, so the formula simplifies quite a bit
		return numpy.log2(len(population))
	
def split(population, attribute, value):
	a = [i for i in population if i[attribute] == value]
	b = [i for i in population if i[attribute] != value]
	assert(set(map(str, population)) == set(map(str, a + b)))
	return a, b

def information_gain(population, attribute, value):
	a, b = split(population, attribute, value)
	n = len(population)
	return entropy(population) - (len(a) * entropy(a) + len(b) * entropy(b)) / n

def optimal_classifier(population):
	possible = set((attribute, i[attribute]) for attribute in interesting for i in population)
	def k((attribute, value)):
		return information_gain(population, attribute, value)
	
	return max(possible, key=k)

def make_tree(population, depth):
	if len(population) == 1:
		return (population[0]['Name'], depth)
	elif len(population) == 0:
		return []
	
	attribute, value = optimal_classifier(population)
	a, b = split(population, attribute, value)
	return [(attribute, value, make_tree(a, depth+1)), (attribute, '!' + value, make_tree(b, depth+1))]
	
pprint.pprint(make_tree(people, 0))
