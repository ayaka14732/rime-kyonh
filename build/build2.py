kyonh2描述 = {}

with open('cache/kyonh.txt') as f:
	for line in f:
		描述, 拼音 = line.rstrip('\n').split('\t')
		kyonh2描述[拼音] = 描述

描述2ayaka_2021 = {}

with open('cache/ayaka_2021.txt') as f:
	for line in f:
		描述, 拼音 = line.rstrip('\n').split('\t')
		描述2ayaka_2021[描述] = 拼音

def do(input_file, output_file):
	with open(input_file) as f, open(output_file, 'w') as g:
		for line in f:
			if line == '...\n':
				g.write(line)
				break
			line = line.replace('zyenpheng', 'ayaka_2021')
			g.write(line)

		for line in f:
			line = line.rstrip('\n')

			if not line:
				g.write('\n')
				continue

			ch, 拼音們, *extra = line.split('\t')

			try:
				new拼音們 = ' '.join(描述2ayaka_2021[kyonh2描述[拼音]] for 拼音 in 拼音們.split(' '))

				print(ch, new拼音們, *extra, file=g, sep='\t')
			except KeyError:
				pass

do('zyenpheng.dict.yaml', 'ayaka_2021.dict.yaml')
do('zyenpheng.words.dict.yaml', 'ayaka_2021.words.dict.yaml')
