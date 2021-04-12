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

g2 = open('cache/unhandled2.txt', 'w')

def do(input_file, output_file):
	with open(input_file) as f, open(output_file, 'w') as g:
		for line in f:
			if line == '...\n':
				g.write(line)
				break
			line = line.replace('kyonh', 'ayaka_2021')
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
				for c, 拼音 in zip(ch, 拼音們.split(' ')):
					if 拼音 not in kyonh2描述:
						print(拼音, c, file=g2)

do('kyonh.dict.yaml', 'ayaka_2021.dict.yaml')
do('kyonh.words.dict.yaml', 'ayaka_2021.words.dict.yaml')

g2.close()
