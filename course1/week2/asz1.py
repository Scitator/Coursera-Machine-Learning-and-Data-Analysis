import numpy as np
import pandas as pd
from collections import Counter
from scipy.spatial.distance import cosine
import re

f = open('sentences.txt', 'r')
text = f.readlines()
text = map(lambda x: x.lower(), text)

splitedText = []

for line in text:
	splitedText.append(re.split('[^a-z]', line))
	splitedText[-1] = filter(lambda a: a != "", splitedText[-1])

wordDict = {}
counter = 0
for splitedLine in splitedText:
	for word in splitedLine:
		if word not in wordDict:
			wordDict[word] = counter + 1
			counter = counter + 1

dnmatrix = []
for splitedLine in splitedText:
	cnt = Counter(splitedLine)
	line = []
	for key in wordDict:
		line.append(cnt[key])
	dnmatrix.append(line)

for i  in range(1, len(dnmatrix)):
	print str(i) +": " + str(cosine(dnmatrix[0], dnmatrix[i]))