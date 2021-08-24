# file dice.py
import math

def func():
    combinations = [(dice1, dice2) for dice1 in range(1, 7) for dice2 in range(1, 7)]
    print(len(combinations))

    result_list8 = [{x: [j for j in combinations if j[0] + j[1] == x]} for x in range(2, 13)]
    print(result_list8)

    result_list9 = [{x: '{0:.2f}'.format((len([j for j in combinations if j[0] + j[1] == x]) / len(combinations) * 100)) + "%"} for x in
                    range(2, 13)]
    print(result_list9)
    return result_list9

print("top-level in dice")

if __name__ == "__main__":
    print("dice is being run directly")
else:
    print("dice is being imported into another module")