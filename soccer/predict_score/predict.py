import random
import numpy as np
import numpy.random as rd
import statistics


coe = [1.89262233e-04 , 3.11945169e-02 , 1.26079176e+00]


def main(my_team,enemy_team):
    global my_name_list,enemy_name_list
    my_name_list = my_team.values_list('name', flat=True)
    enemy_name_list = enemy_team.values_list('name', flat=True)
    score = predict_game(my_team,enemy_team)
    result = poidssn(score)
    all_live = make_live(result)
    return all_live



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
    if my_attack < -99:
        my_attack = -99

    enemy_attack = (0.3*ave_enemy_shoot + 0.4*ave_enemy_dribble + 0.3*ave_enemy_passing) - ave_my_defence

    if enemy_attack < -99:
        enemy_attack = -99

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
goal_words =['{}がエリア外からミドルシュート!!','{}がPKを冷静に決める!!', '{}が華麗にループシュート!!','{}がヘディングで押し込む!!']
lost_words =['{}がエリア外からミドルシュート!!','{}がPKを冷静に決める!!', '{}がヘディングで押し込む!!', '{}が華麗にループシュート!!']

def make_live(result):
    all_live = []
    super_result = []
    if sum(result) > 15:
        super_result.append(result[0])
        super_result.append(result[1])

        while sum(result)> 15:

            result[0] = max(0,result[0]-1)
            result[1] = max(0,result[1]-1)


    number = 15-result[0] - result[1]
    #ゴール
    minute = [random.randint(0, 90) for _ in range(result[0])]
    [all_live.append([min, 1, random.choice(goal_words).format(random.choice(my_name_list))])for min in minute]
    #失点
    minute = [random.randint(0, 90) for _ in range(result[1])]
    [all_live.append([min, 2, random.choice(lost_words).format(random.choice(enemy_name_list))])for min in minute]
    #チャンス
    minute = [random.randint(0, 90) for _ in range(number//2)]
    [all_live.append([min, 3, random.choice(chance_words).format(random.choice(my_name_list))]) for min in minute]
    #敵のチャンス
    minute = [random.randint(0, 90) for _ in range(number - number//2)]
    [all_live.append([min, 4, random.choice(chance_words).format(random.choice(enemy_name_list))]) for min in minute]

    all_live.sort()
    print(super_result)
    if super_result:
        print(super_result)
        super_result.insert(1,5)
        all_live.append(super_result)
    else:
        result.insert(1, 5)
        all_live.append(result)


    return all_live





