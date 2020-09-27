# import json
# class MyEncoder(json.JSONEncoder):
#         def default(self, obj):
#                 if isinstance(obj, bytes):
#                         return str(obj, encoding='utf-8')
#                 return json.JSONEncoder.default(self, obj)

from datetime import datetime

date_time_str = '2018-06-29 08:15:27'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
print(type(date_time_obj))