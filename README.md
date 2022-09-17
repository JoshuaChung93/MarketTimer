# MarketTimer

2022-09-08 final updated file: MarketTimer_1.0_final.py

- 기본 기능은 아래와 같습니다 


현재 코스닥 지수와 3,5,10 이동평균을 비교해, 실시간으로 09:00, 10:00, 12:00, 14:00, 15:30 알람을 보냅니다


현재 코스닥 지수가 3 or 5 or 10 이동평균보다 높을 경우 -> 매수신호


현재 코스닥 지수가 3 and 5 and 10 이동평균보다 낮을 경우 -> 매도신호 로 활용하실 수 있습니다.


활용방안 ↓

- 전략1: 전날 종가배팅한 종목을 들고 코스닥 마켓타이밍이 매수신호일 경우 홀딩, 매도신호일 경우 10시 청산


- 전략2: 9시 코스닥 갭하락 시작시에 매수, 12시까지 매도신호만 뜰 경우 청산, 매수신호일 경우 홀딩


텔레그램 채널로 알림을 실시간 전송하니 텔레그램 계정이 없으신 분들은 가입 후 사용 부탁드립니다.


활용 가능한 클라우드 서버:


Oracle Cloud: https://cloud.oracle.com


맥에서 오라클 클라우드 ssh 서버 설정:


https://chailmon.com/dev/cloud/cloud-connecting-to-oracle-cloud-server-via-ssh-in-terminal-on-mac/


리눅스 명령어 관련:


https://joonyon.tistory.com/entry/%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85%ED%95%9C-nohup-%EA%B3%BC-%EB%B0%B1%EA%B7%B8%EB%9D%BC%EC%9A%B4%EB%93%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%82%AC%EC%9A%A9%EB%B2%95


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
