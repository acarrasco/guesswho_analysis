#!/bin/env python

import csv
import numpy
from collections import Counter

reader = csv.DictReader(open('data.csv'))
people = list(reader)

attributes = {name: Counter() for name in reader.fieldnames}
interesting = {'Eyes', 'Hair Length', 'Gender', 'Cheeks', 'Frown', 'Hat', 'Hair Color', 'Mouth', 'Nose', 'Smile', 'Hair Shape', 'Glasses', 'Beard'}

for person in people:
	for attribute, value in person.iteritems():
		attributes[attribute][value] += 1

for attributeName, attributeValues in attributes.iteritems():
	print attributeName
	for value, count in attributeValues.iteritems():
		print "\t%s: %d" % (value, count)

medians = {attributeName: numpy.median(attributes[attributeName].values()) for attributeName in interesting}

byProbabilty = []
for person in people:
	p = 1
	minorities = []
	for attributeName, attributeValue in person.iteritems():
		if attributeName in interesting:
			v = attributes[attributeName][attributeValue]
			p *= v / 24.0
			if v < medians[attributeName]:
				minorities.append(attributeName)
	byProbabilty.append((p, person['Name'], minorities))

for p, name, minorities in sorted(byProbabilty):
	print "%s: %0.6f; %s" % (name, p, minorities)
