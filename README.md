Ever wondered if there's a gender bias in the game "Guess Who"?

The naive_analysis.py script shows accumulated metrics and does a
simple estimation, assuming (wrongly) independence between attributes.

The classifier.py script employs a simplified ID3 classifier (as each
character has its own class; we know that the attributes completely
classify the set) to build the decission tree that solves the
game in an efficient way.
