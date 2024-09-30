# ==== Question 4: ====

import numpy as np
from itertools import combinations

'''
PSEUDOCODE:
1. create a 10x10 numpy array simulating scores (this array should reflect positions i,j for score difference between player 1 & player 2)
	2. use np.random.randint to generate the 10x10 array
	3. fill the diagonals of this array with 0 (for a player against themselves, score differential is zero) - use numpy.fill_diagonal()
	4. reflect the upper triangle of this matrix across the lower triangle (player 1 vs 2 is the same as player 2 vs 1) - use numpy.triu_indices_from() and transpose '.T'
5. take the upper triangle indices to generate a unique list of paired players OR generate unique pair of matchings from combination of 0-10
6. calculate the squared point differential between each unique pair of players
7. determine the "best" arrangement of pairings with the minimum squared point differentials
'''

# random 10x10 array (-10 to 10)
score_diff = np.random.randint(low=-10,high=10,size=(10,10))

# fill diagonal with 0's
# fill_diagonal documentation: https://numpy.org/devdocs/reference/generated/numpy.fill_diagonal.html
np.fill_diagonal(score_diff,0)

# upper triangle indices with diagonal offset of 1
# triu_indices_from documentation: https://numpy.org/doc/2.1/reference/generated/numpy.triu_indices_from.html
up_diag_indices = np.triu_indices_from(score_diff,k=1)

# reflect upper diagnoal over lower diagonal
score_diff[up_diag_indices] = score_diff.T[up_diag_indices]

print("Score Differences:")
print(score_diff,end="\n\n")

# generate all unique combinations of matches
# combinations documentation: https://docs.python.org/3/library/itertools.html#itertools.combinations
unique_matches = list(combinations(range(10),2))
#print("DEBUG ", unique_matches)

# calculate & store the corresponding score diff^2 for each unique matchup
matchups_and_score = {matchup:score_diff[matchup]**2 for matchup in unique_matches}
#print("DEBUG", matchups_and_score)

# sort the dictionary of matchups by score
score_ascending_matchups = sorted(matchups_and_score.items(), key=lambda item: item[1])
#print("DEBUG ",score_ascending_matchups)

# store players who played already so we do not have a player play more than once per round
played_already = set()

# schedule will be built from score_ascending_matchups (increasing squared score differentials)
schedule = []

# sort through the score_ascending_matchups and add to the schedule the first occurring instance of each unique set of players
for ((p1,p2),score) in score_ascending_matchups:
	if p1 not in played_already and p2 not in played_already:
		played_already.update([p1,p2])
		schedule.append((p1,p2))

# schedule should contain matchups of players with minimized squared point differentials
print("ROUND ONE:")
for p1,p2 in schedule:
	print(f"player {p1} vs player {p2} - (projected point difference of {score_diff[p1,p2]})")