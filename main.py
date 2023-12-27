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
        if self.x < 3:
            self.x += 1
    
    def move_left(self):
        if self.x > 0:
            self.x -= 1
    
    # y축 방향이 반대임
    def move_up(self):
        if self.y > 0:
            self.y -= 1
    
    def move_down(self):
        if self.y < 3:
            self.y += 1

    # 종료 State에 도달했는지 체크
    def is_done(self):
        if self.x == 3 and self.y == 3:
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
    
def main():
    env = GridWorld()
    agent = Agent()
    data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    gamma = 1.0
    alpha = 0.0001 # Monte Carlo Learning Algorithm에서 State Value를 한 Episode마다 업데이트할 때 사용하는 방법
    
    for k in range(50000): #총 50,000번 Episode 진행
        done = False
        history = []

        while not done:
            action = agent.select_action()
            (x, y), reward, done = env.step(action) # Action을 이용해 한 step 진행 후 Environment의 반응
            history.append((x, y, reward))

        env.reset() # 한 Episode가 끝난 후 리셋

        # 매 Episode가 끝날 때마다 해당 데이터로 Table을 업데이트함
        # Return은 Reward의 누적으로 계산할 수 있음
        cum_reward = 0
        for transition in history[::-1]: #방문했던 State들을 뒤에서부터 보며 Return을 계산
            x, y, reward = transition
            data[y][x] = data[y][x] + alpha * (cum_reward - data[y][x]) # 업데이트
            cum_reward = gamma * cum_reward + reward #Episode의 뒤에서부터 리턴을 계산함

    for row in data:
        print(row)

main()