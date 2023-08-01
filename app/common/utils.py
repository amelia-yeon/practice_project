''' 공통 함수 '''

import pendulum

# 날짜 및 시간 반영 함수 
def now_time_millisecond():
    now = pendulum.now('Asia/Seoul')
    now_time = now.strftime("%Y%m%d %H:%M:%S.%f")
    return now_time



# 리스트 변수 콤마로 이은 문자열 형식으로 변환 
def list_to_str(list_data: list):
    result = ', '.join('{0}'.format(w) for w in list_data)
    return result



