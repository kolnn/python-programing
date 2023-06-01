import pickle
import os

filepath = 'score.bin'


def save_data(scores, average):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(average, file)


def load_data():
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
        average = pickle.load(file)

    return scores, average


if os.path.exists(filepath):
    print('[파일 읽기]')
    r_scores, r_average = load_data()
    print(r_scores)
    print(r_average)

else:
    def input_scores():
        print('[점수 입력]')
        scores = []
        while True:
            score = int(input("#{}? ".format(len(scores) + 1)))
            if score < 0:
                break
            scores.append(score)
        return scores


    def get_average(scores):
        if len(scores) == 0:
            return 0
        return sum(scores) / len(scores)


    def show_scores(scores):
        print('')
        print('[점수 출력]')
        print("개인점수:", end=" ")
        for score in scores:
            print(score, end=" ")
        print()


    scores = input_scores()
    average = get_average(scores)
    show_scores(scores)
    save_data(scores, average)
