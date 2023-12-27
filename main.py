# 바닥부터 배우는 강화 학습 P.113 Monte Carlo Learning Algorithm 구현

import random

class GridWorld():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    # Agent의 움직임을 나타냄
    def step(self, a):
        if a == 0:
            self.move_right()
        elif a == 1:
            self.move_left()
        elif a == 2:
            self.move_up()
        elif a == 3:
            self.move_down()
        
        state = self.get_state()
        reward = -1
        done = self.is_done()

        return state, reward, done
    
    # 4칸을 벗어날 수 없음
    def move_right(self):
        if x < 3:
            x += 1
    
    def move_left(self):
        if x > 0:
            x -= 1
    
    # y축 방향이 반대임
    def move_up(self):
        if y > 0:
            y -= 1
    
    def move_down(self):
        if y < 3:
            y += 1

    # 종료 State에 도달했는지 체크
    def is_done(self):
        if self.x == 3 or self.y == 3:
            return True
        else:
            return False
    
    # 현재 Agent가 위치한 State를 반환
    def get_state(self):
        return (self.x, self.y)
    
    # 종료 State에 도달했을 때 리셋
    def reset(self):
        self.x = 0
        self.y = 0

class Agent():
    def __init__(self):
        pass

    def select_action(self):
        # Action을 확률적으로 선택
        coin = random.random()

        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3
            
        return action