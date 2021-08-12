# 작업 완료 후 알람 재생
import time
import pygame

def alarm(num):
    pygame.mixer.init()
    pygame.mixer.music.load("Radar.mp3")
    pygame.mixer.music.play(num)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)
    pygame.mixer.quit()

def task_run(task):
    # task 함수 객체를 받아온 뒤 (task가 완료된 후) 시간을 저장
    now = time.time()
    # task는 (데이터 갯수, 시작시간) 튜플을 반환
    print("Number of Collected Data : ", task[0])
    print("Executing Time Duration : ", round(now - task[1], 4), "sec")
    # 알람은 매개변수로 울리는 횟수 설정
    alarm(1)