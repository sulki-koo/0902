import urllib # url 요청을 위한 라이브러리
import json # JSON 데이터 파싱용
import pandas as pd # 데이터 프레임 생성 및 데이터 처리용
import cv2 # 영상 처리용
import urllib.request # URL 요청

def its_cctv():
    # 1. 인증 키 설정 (import os로 환경변수 처리 해보기)
    apiKey = ""

    # 2. 도로 유형 저장
    # 'its'는 일반도로 || 'ex'는 고속도로
    type = "its"

    # 3. 경도, 위도 설정
    minX = float(120.95)
    maxX = float(127.02)

    minY = float(30.55)
    maxY = float(37.69)

    # 4. 응답 데이터 형식 설정
    getType = "json"

    # 5. API 요청 URL 생성
    url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={apiKey}&type={type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"

    # 6. 요청 및 응답 받기
    response = urllib.request.urlopen(url_cctv)

    # 7. 데이터 디코딩
    json_str = response.read().decode("utf-8")

    # 8. 파이썬 딕셔너리 변환
    json_object = json.loads(json_str)

    # 9. 판다스 데이터 프레임 변환
    cctv_play = pd.json_normalize(json_object["response"]["data"], sep='')

    # 10. 특정 CCTV 선택
    test_url = cctv_play["cctvurl"][93]
    return test_url