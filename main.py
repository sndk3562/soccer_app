import random
import numpy as np
import numpy.random as rd
import statistics


x = np.array([-99, -50, -10, 0, 10, 20, 30, 40, 50, 60, 70,80,90,100])
y = np.array([0.01, 0.06, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
r = 0
coe = np.polyfit(x,y,2)
Y = coe[0] * r ** 2 + coe[1] * r + coe[2]

name_list = ['a'] * 10
def main(my_team,enemy_team):
    score = predict_game(my_team,enemy_team)
    result = poidssn(score)
    all_live = make_live(result)
    return all_live

def calculate():
    return 2


def predict_game(my_team,enemy_team):
    my_defence = my_team.values_list('defence',flat=True)
    ave_my_defence = statistics.mean(my_defence)

    enemy_defence = enemy_team.values_list('defence',flat=True)
    ave_enemy_defence = statistics.mean(enemy_defence)

    my_dribble = my_team.values_list('dribble',flat=True)
    ave_my_dribble = statistics.mean(my_dribble)
    enemy_dribble = enemy_team.values_list('dribble', flat=True)
    ave_enemy_dribble = statistics.mean(enemy_dribble)

    my_passing = my_team.values_list('passing', flat=True)
    ave_my_passing = statistics.mean(my_passing)
    enemy_passing = enemy_team.values_list('passing', flat=True)
    ave_enemy_passing = statistics.mean(enemy_passing)

    my_shoot = my_team.values_list('shoot', flat=True)
    ave_my_shoot = statistics.mean(my_shoot)
    enemy_shoot = enemy_team.values_list('shoot', flat=True)
    ave_enemy_shoot = statistics.mean(enemy_shoot)

    my_attack = (0.3*ave_my_shoot + 0.4*ave_my_dribble + 0.3*ave_my_passing) - ave_enemy_defence
    enemy_attack = (0.3*ave_enemy_shoot + 0.4*ave_enemy_dribble + 0.3*ave_enemy_passing) - ave_my_defence

    my_score =  (coe[0] * my_attack ** 2 + coe[1] * my_attack + coe[2]) * 1.7
    enemy_score = (coe[0] * enemy_attack ** 2 + coe[1] * enemy_attack + coe[2]) * 1.7




    score = [my_score,enemy_score]

    return score


def poidssn(score):
    myresult = rd.poisson(score[0],1)
    enemyresult = rd.poisson(score[1],1)
    result = [myresult[0],enemyresult[0]]
    return result

chance_words = ['{}がシュート打つもキーパにキャッチされる','{}がサイドを突破','クロスに{}が合わせるもわずかにそれる']
goal_words =['{}がエリア外からミドルシュート!!']
lost_words =['{}がエリア外からミドルシュート!!']

def make_live(result):
    all_live = []
    while sum(result)>15:
        result[0] -=1
        result[1] -=1

    number = 15-result[0] - result[1]
    #ゴール
    minute = [random.randint(0, 90) for _ in range(result[0])]
    [all_live.append([min, 1, random.choice(goal_words).format('s')])for min in minute]
    #失点
    minute = [random.randint(0, 90) for _ in range(result[1])]
    [all_live.append([min, 2, random.choice(lost_words).format(name_list[min % 10])]) for min in minute]
    #チャンス
    minute = [random.randint(0, 90) for _ in range(number//2)]
    print(minute)
    [all_live.append([min, 3, random.choice(chance_words).format('s')]) for min in minute]
    #敵のチャンス
    minute = [random.randint(0, 90) for _ in range(number - number//2)]
    [all_live.append([min, 4, random.choice(chance_words).format('s')]) for min in minute]

    all_live.sort()
    result.insert(1,5)
    all_live.append(result)
    print(all_live)

    return all_live





#
# __pycache__
# myvenv
# db.sqlite3

# chance_words = ['{}がシュート打つもキーパにキャッチされる','{}がサイドを突破、クロスに{}が合わせるもわずかにそれる']
# goal_words =['GOOOOOOOAl!!','{}がエリア外からミドルシュート!!']
# lost_words =['GOAL','{}がエリア外からミドルシュート!!']

#ゴールセリフ[var,pk] チャンスのセリフ[]　コーナキック[]　　オフサイド
#[0 or 1]
#print([random.randint(0,90) for _ in range(2)])




