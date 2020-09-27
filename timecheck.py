import time
import traceback
 
 
def is_valid_date(str_date):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(str_date, '%Y-%m-%d %H:%M:%S')
        return True
    except Exception:
        # raise Exception("时间参数错误 near : {}".format(str_date))
        return False
 
 
# if __name__ == "__main__":
#     date = '2018-06-31 23:56:56'
#     if is_valid_date(date):
#         print("true")
#     else:
#         print("false")
