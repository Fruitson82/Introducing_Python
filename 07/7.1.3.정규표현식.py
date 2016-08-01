# 시작부터 일치하는 패턴 찾기: match()
import re
source = 'Young Frankenstein'

m = re.match('Fran', source) # match는 소스의 시작부터 패턴이 일치하는지 확인한다.
if m:
	print(m.group())

# 첫 번째 일치하는 패턴 찾기: search()
m = re.search('Frank', source)
if m:
	print(m.group())

m = re.search('.*Frank', source)
if m:
	print(m.group())	

# 일치하는 모든 패턴 찾기: findall()
m = re.findall('n', source)
print(m) #findall은 리스트를 반환
print('Found {0} matches.'.format(len(m)))

m = re.findall('n.?', source)
print(m)

# 패턴으로 나누기: split()
m = re.split('n', source)
print(m) # split은 리스트를 반환

# 일치하는 패턴 대체하기:sub()
m = re.sub('n', '?', source)
print(m)

# 패턴: 지정자
source = 'I wish I may, I wish I might Have a dish of fish tonight.'
print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish tonight.$', source))
print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+', source))
print(re.findall('ght\W', source))
print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))

