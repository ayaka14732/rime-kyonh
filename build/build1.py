from datetime import datetime
import os

baxter2描述 = {}

with open('cache/baxter.txt') as f:
	for line in f:
		描述, 拼音 = line.rstrip('\n').split('\t')
		baxter2描述[拼音] = 描述

描述2kyonh = {}

with open('cache/kyonh.txt') as f:
	for line in f:
		描述, 拼音 = line.rstrip('\n').split('\t')
		描述2kyonh[描述] = 拼音

header = f'''\
# Rime dictionary
# encoding: utf-8

---
name: zyenpheng.words
version: "{datetime.today().strftime('%Y.%m.%d')}"
sort: by_weight
use_preset_vocabulary: true
...
'''

with open('cache/words_certain.tsv') as f, open('zyenpheng.words.dict.yaml', 'w') as g1, open('cache/unhandled.txt', 'w') as g2:
	print(header, file=g1)
	for line in f:
		ci, gu, _, _ = line.rstrip('\n').split('\t')
		gu = gu.replace('’', "'") # preprocess
		try:
			gu = ' '.join(描述2kyonh[baxter2描述[py]] for py in gu.split(' '))
			print(ci, gu, sep='\t', file=g1)
		except KeyError:
			print(ci, gu, sep='\t', file=g2)
