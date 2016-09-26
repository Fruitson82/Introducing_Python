import csv

villains = [
	['Doctor', 'No'],
	['Rosa', 'Klebb'],
	['Mister', 'Big'],
	['Auric', 'Goldfinger'],
	['Ernst', 'Blofeld']
	]

# csv 파일 쓰기
with open('villains', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(villains)

# csv 파일 읽기 (csv to list)
with open('villains', 'rt')	as fin:
	csvin = csv.reader(fin)
	villians2 = [row for row in csvin]

print(villians2)

# csv 파일 읽기 (csv to dictionary)
with open('villains', 'rt') as fin:
	csvin2 = csv.DictReader(fin, fieldnames=['first', 'last'])
	villains3 = [row for row in csvin2]

print (villains3)

villains4 = [
	{'first': 'Doctor', 'last': 'No'},
	{'first': 'Rosa', 'last': 'Klebb'},
	{'first': 'Mister', 'last': 'Big'},
	{'first': 'Auric', 'last': 'Goldfinger'},
	{'first': 'Ernst', 'last': 'Blofeld'}
]
# csv 파일 쓰기 (dictionary with header to csv)
with open('villains4', 'wt') as fout:
	cout = csv.DictWriter(fout, ['first', 'last'])
	cout.writeheader()
	cout.writerows(villains4)

# csv 파일 읽기 (csv to dictionary)
with open('villains4', 'rt') as fin:
	cin = csv.DictReader(fin)
	villains5 = [row for row in cin]

print(villains5)