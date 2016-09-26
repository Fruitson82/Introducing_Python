import datetime
import json

now = datetime.datetime.utcnow()
print(now)

now_str = str(now)
print(json.dumps(now_str))

from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

class DTEncoder(json.JSONEncoder):
	def default(self, obj):
		# isinstance()는 obj의 타입을 확인한다.
		if isinstance(obj, datetime.datetime):
			return int(mktime(obj.timetuple))
		# obj가 datetime 타입이 아니라면 기본 JSON 문자열로 인코딩한다.
		return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))