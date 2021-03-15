import itertools

file1 = open("./decodeme.txt", "r")
#file2 = open("./bigrams.txt", "r")
#file3 = open("./trigrams.txt", "r")
file4 = open("./maindis.txt", "r")

text = file1.read()
#bigrams = file2.read().splitlines()
#trigrams = file3.read().splitlines()
maindis = file4.read().splitlines()

file1.close()
#file2.close()
#file3.close()

best_permutations = []
best_perm_scores = []
total_perm_scores = []
perm_lengths = []
bw_score = 0

def score_appender(s, p):
	global bw_score
	index = None
	loop_len = len(best_permutations)
	if (len(best_permutations) == 0):
		best_permutations.append(p)
		best_perm_scores.append(s)
	else:
		loop_len2 = loop_len
		for i in range(loop_len):
			if (best_perm_scores[i] < s):
				index = i
				break
				
		if (loop_len < 100):
			best_permutations.append("")
			best_perm_scores.append(0)
			loop_len2 += 1
			
		for i in range(loop_len2-1, index, -1):
			best_permutations[i] = best_permutations[i-1]
			best_perm_scores[i] = best_perm_scores[i-1]
		best_permutations[index] = p
		best_perm_scores[index] = s
		
	bw_score = best_perm_scores[-1]
	return

def get_permutations(permutaton_length):
	new_permutations = []
	blank_perm = []
	for i in range(permutaton_length):
		blank_perm.append(i)
	
	new_permutations = itertools.permutations(blank_perm)
	
	return new_permutations
	
counter = 0
def try_permutation(try_this):
	score = 0
	key_len = len(try_this)
	text_len = len(text)
	cipher = [""] * text_len
	decoded_text = ""
	
	for i in range(text_len):
		mod_index = (i%key_len)
		c_index = try_this[mod_index] + (int((i/key_len)) * key_len)
		if (c_index >= text_len):
			break
		cipher[c_index] = text[i]	
	
	decoded_text = decoded_text.join(cipher)
	"""
	for item in bigrams:
		if item.lower() in decoded_text:
			score += 1
	for item in trigrams:
		if item.lower() in decoded_text:
			score += 1
	"""
	for item in maindis:
		if item.lower() in decoded_text:
			score += 1
			
	return score

for i in range(13, 14):
	total = 0
	counter = 0
	permutations = get_permutations(i)
	for item in permutations:
		counter += 1
		score = try_permutation(item)
		total += score
		if (score > bw_score):
			score_appender(score, item)
		
	perm_lengths.append(counter)
	total_perm_scores.append(total)	

print(best_permutations, "\n")
print(best_perm_scores, "\n\n")
print(total_perm_scores, "\n")
print(perm_lengths)		
		
		
			