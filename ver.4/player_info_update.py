import requests
from bs4 import BeautifulSoup
import sys
import time
from selectors import css_selector, position_overalls

# css selector를 통해 받아온 선수의 텍스트 데이터를 포맷에 따라 DB에 넣을 형태로 변환처리
def processed_data(data, data_label):
    # 비어있을 경우 0 리턴 (ex. liveboost)
    if not data:
        return 0
    else :
        output = []
        # data들을 순회하면서 text, strip을 통해 원하는 값만을 추출
        for single_data in data:
            output.append(single_data.text.strip())

        if data_label == 'overall':
            return int(output[0])+3
        # 생년월일은 8자리 int로 변환
        elif data_label == 'birth':
            return int(''.join(output[0][:10].split('.')))
        # 키와 몸무게는 단위인 cm, kg을 제외한 후 int로 변환
        elif data_label == 'height' or data_label == 'weight':
            return int(output[0][:-2])
        # 개인기 수치는 별의 개수(길이)를 반환
        elif data_label == 'skill':
            return len(output[0])
        # 주발은 숫자를 제외한 L, R 알파벳만 추출하여 반환
        elif data_label == 'main_foot':
            return output[0][0]
        # 주발, 약발의 수치를 L, R을 키값으로 하는 dict로 반환
        elif data_label == 'foot':
            return {'L' : int(output[0][1]), 'R' : int(output[0][-1])}
        # 국가는 간혹 뒤에 ", 국가대표" 등으로 붙어있는 경우가 있으므로 제거후 반환
        elif data_label == 'nation':
            return output[0].split(',')[0]
        # 포지션별 ovr 수치
        elif data_label == 'position_overalls':
            return {key: int(val)+3 for key, val in zip(position_overalls, output)}
        # 클럽 경력은 기간, 클럽, 임대를 키, 값 형태의 dict로 만들어 dict들의 list로 반환
        elif data_label == 'club_history':
            term = [term for i, term in enumerate(output) if i % 3 == 0]
            club = [club for i, club in enumerate(output) if i % 3 == 1]
            loan = [loan for i, loan in enumerate(output) if i % 3 == 2]
            return [{'term' : _term, 'club' : _club, 'loan' : _loan} for _term, _club, _loan in zip(term, club, loan)]
        # 세부스탯은 스탯이름(label) : 스탯값(value) 의 dict로 만들어 반환
        # 현재 output에 있는 elements 중에 정수가 아닌 것은 스탯이름, 정수인 것은 스탯값으로 간주
        elif data_label == 'stats':
            stat_label = [label for label in output if not label.isdigit()]
            stat_value = [int(value)+3 for value in output if value.isdigit()]
            return {key : val for key, val in zip(stat_label, stat_value)}
        # 그 외 단일 데이터만 있는 값들은 정수라면 정수로 반환, 아니라면 그대로 반환
        elif len(output) == 1:
            return int(output[0]) if output[0].isdigit() else output[0]
        # 단일 데이터가 아닐 경우 output list를 그대로 반환 (ex. speciality)
        else :
            return output

def get_player_info(spid):
    player = {'spid' : spid}
    url = 'http://fifaonline4.nexon.com/DataCenter/PlayerInfo'
    # url get 메서드의 파라미터 선언, 그러나 player에서 이미 똑같은 형태 dict가 존재해서 player 로 사용
    # params = {'spid' : spid}
    response = requests.get(url, params=player)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        for data_label, selector in css_selector.items():
            data = processed_data(soup.select(selector), data_label)
            player[data_label] = data
    else :
        sys.exit(response.status_code)
    
    return player


if __name__ == '__main__':
    # spid input 을 넣어 player_info 메서드 검증, duration 측정
    start = time.time()
    print(get_player_info(101000001))
    print(time.time() - start)