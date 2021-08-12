# from_API.py
피파온라인 사이트 자체 제공 api에서 제공하는 json 파일을 다운로드 받는 메소드
# id_to_ovr.py
선수 spid로 선수 정보 페이지에 접근하여 ovr 수치를 수집
# data.py
API로 부터 받은 spid.json, seasonid.json 파일과 더불어 가공된 데이터 저장
# prices.py
선수별 시장판매가 정보를 +1~+10강화 까지 수집하는 메소드
# ovr_to_strong.py
강화 대상의 ovr을 선택한 뒤 강화 재료의 ovr 별 강화부스트 퍼센티지 정보 수집
# price_for_ovr.py
선수의 ovr 별로 강화 재료로서의 평균적 가격이 얼마인지 계산

# day_to_day_price.py
멀티 프로세싱으로 prices.py 내부 make_prices() 메소드 실행. 매일 갱신될 때마다 실행 필요
# roster_update.py
로스터 업데이트가 될 때 마다 추가된 선수들을 api로 부터 다시 다운받아 data.py에 갱신


# id_to_ovr.py 실행시간 : 2218초 소요
# dictionary 타입 데이터 json으로 변환하면 key값 전부다 string으로 변환.
# 지금 현재 프로젝트 폴더는 Project2 폴더. Project2/json_files/json_io.py 에서 read/write json을 할 때, 첫 path기준이 프로젝트 폴더 기준인듯.
앞에 ./json_files를 붙여줘야 제대로 읽고 쓰기가 가능함(본 파일이 해당 json_files폴더에 같이 속해있음에도 불구하고)

# 로스터 업데이트 주소 (생성제한 선수 명단)
# 2018 하반기
라이브 클래스 : http://fifa4.vod.nexoncdn.co.kr/list/2018/10/201810_roster_update_02_wsxlIIlmko.html
라이브 클래스 외 : http://fifa4.vod.nexoncdn.co.kr/list/2018/10/201810_roster_update_03_fghbgrnht.html
# 2019 상반기
http://fifa4.vod.nexoncdn.co.kr/list/2019/4/list_FO4_roster_update_20190502_lIlIlIlI.html
# 2019 하반기
http://fifa4.vod.nexoncdn.co.kr/list/2019/10/list_FO4_roster_update_20191024_v4IIllIlIl.html
# 2020 상반기
http://fifa4.vod.nexoncdn.co.kr/list/2020/3/list_FO4_MS14_roster_update_20200326_x4v8Dn.html
# 2020 하반기
http://fifa4.vod.nexoncdn.co.kr/list/2020/12/list_FO4_roster_update_20201217_thelastoftheyear.html