# MarketTimer

2022-09-08 final updated file: MarketTimer_1.0_final.py

- 기본 기능은 아래와 같습니다 


현재 코스닥 지수와 3,5,10 이동평균을 비교해, 실시간으로 09:00, 10:00, 12:00, 14:00, 15:30 알람을 보냅니다


현재 코스닥 지수가 3 or 5 or 10 이동평균보다 높을 경우 -> 매수신호


현재 코스닥 지수가 3 and 5 and 10 이동평균보다 낮을 경우 -> 매도신호 로 활용하실 수 있습니다.


활용방안 ↓

- 전략1: 전날 종가배팅한 종목을 들고 코스닥 마켓타이밍이 매수신호일 경우 홀딩, 매도신호일 경우 10시 청산


- 전략2: 10시에 코스닥 지수가 매도신호일 경우 눌림목 매수, 12시 매수신호일 경우 홀딩, 반대의 경우 청산, 14-15시 매도


텔레그램 채널로 알림을 실시간 전송하니 텔레그램 계정이 없으신 분들은 가입 후 사용 부탁드립니다.


오류 및 기능 문의:

https://open.kakao.com/o/sn4y2B0c

Reference: 

재고 봇 만들기

https://tech.lonpeach.com/2021/02/13/python-telegram-restock-bot/

이동평균선, FinanceDataReader

https://colab.research.google.com/drive/1yFu9PUcj22edVd4Sx0W32DIjvrju50as?usp=sharing#scrollTo=kVTsrHiY1DW8

https://colab.research.google.com/drive/1yVGOELrCsdGlvXEISqwfs-AvYcnfLCS8?usp=sharing

scheduling 

https://github.com/dbader/schedule

퀀트투자를 위한 키움증권 API

https://wikidocs.net/92180

Dataframe 형태 json출력시 문제

https://kibua20.tistory.com/193
