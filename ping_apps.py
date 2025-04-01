import requests
import time
import sys
import os

# 접속할 Streamlit 앱 URL 목록
STREAMLIT_APPS = [
    "https://streamlit-insomnia.streamlit.app",  # 실제 앱 URL로 변경해주세요
]

def ping_apps():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"시작 시간: {current_time}\n"
    
    for app_url in STREAMLIT_APPS:
        try:
            response = requests.get(app_url, timeout=30)
            status = f"앱 URL: {app_url}, 상태 코드: {response.status_code}"
            log_message += status + "\n"
            print(status)
        except Exception as e:
            error = f"앱 URL: {app_url}, 오류 발생: {str(e)}"
            log_message += error + "\n"
            print(error)
    
    completion_time = f"완료 시간: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    log_message += completion_time + "\n\n"
    print(completion_time)
    
    # 로그 파일에 기록
    with open("ping_log.txt", "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    ping_apps() 