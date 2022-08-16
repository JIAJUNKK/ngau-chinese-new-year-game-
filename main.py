import itertools
import copy
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
point_card_array = []
real_card_array = []
point_array = []
check_ngaw_zai = []
check_position = []
ngaw_zai = []
pictures_count = 0
spade = 0
# 3 7 j 3 4 - test case 1 
# 6 6 4 10 3 - test case 2 
while len(real_card_array) < 5:
    choice_card = input("pls enter your card: ")
    if choice_card.upper() == "A":
        ace = int(input("Spades or no? Enter 1 for yes. Enter 2 for no\n>>"))
        if ace == 1:
            spade += 1
        real_card_array.append(choice_card.upper())
    else:
        real_card_array.append(choice_card.upper())

for i in range(len(real_card_array)):
    if real_card_array[i] == 'J' or real_card_array[i] == 'Q' or real_card_array[i] == 'K':
        pictures_count += 1
    if real_card_array[i].isdigit():
        real_card_array[i] = int(real_card_array[i])
print("The cards you have entered: ", real_card_array)


for five_cards in range(len(real_card_array) + 1):
    for card in itertools.combinations(real_card_array, five_cards):
        if len(card) == 3:
            check_ngaw_zai.append(card)
            check_position.append(card)
            
# find ngaw_zai, or also known as passport 
for three_cards in range(len(check_ngaw_zai)):
    check_ngaw_zai[three_cards] = list(check_ngaw_zai[three_cards])
    check_position[three_cards] = list(check_position[three_cards])

    for real_card in range(len(check_position[three_cards])):
        if check_position[three_cards][real_card] == 'J'\
                or check_position[three_cards][real_card] == 'Q'\
                or check_position[three_cards][real_card] == 'K':
            check_position[three_cards][real_card] = 10

        if check_position[three_cards][real_card] == 'A':
            check_position[three_cards][real_card] = 1

    for card in range(len(check_position[three_cards])):
        if sum(check_position[three_cards]) % 10 != 0:
            while check_position[three_cards][card] == 6:
                check_position[three_cards][card] = 3
        if sum(check_position[three_cards]) % 10 != 0:
            while check_position[three_cards][card] == 3:
                check_position[three_cards][card] = 6
    if sum(check_position[three_cards]) % 10 == 0:
        ngaw_zai.append(check_ngaw_zai[three_cards])

print("Three cards arrangement in points:   ", check_position)
print("Three cards arrangement in real word:", check_ngaw_zai)
print("Ngaw zai:                            ", ngaw_zai)


double = 0
double_point1 = 0
ngaw_tongku = 0
double_array = []

if len(ngaw_zai) >= 1:
    largest_point1 = []
    largest_point2 = []
    for card in range(len(ngaw_zai)):
        check_largest_point = copy.deepcopy(real_card_array)
        while len(ngaw_zai[card]) != 0:
            if ngaw_zai[card][0] in check_largest_point:
                check_largest_point.remove(ngaw_zai[card][0])
                ngaw_zai[card].remove(ngaw_zai[card][0])
        largest_point1.append(check_largest_point)
        largest_point2.append(check_largest_point)

        for i in range(len(largest_point2[0])):
            if 3 in largest_point2[card]:
                while largest_point2[card][i] == 3:
                    largest_point2[card][i] = 6

            elif 6 in largest_point2[card]:
                while largest_point2[card][i] == 6:
                    largest_point2[card][i] = 3
    print("This is the checking part 1: ", largest_point1)
    print("This is the checking part 2: ", largest_point2)
    for two_cards in range(len(largest_point1)):
        if largest_point1[two_cards][0] == largest_point1[two_cards][1]:
            double_point1 = largest_point1[two_cards][1]
            double_array.append(double_point1)
            double += 1
        if ('J' in largest_point1[two_cards] or 'Q' in largest_point1[two_cards] or'K' in largest_point1[two_cards])\
            and 'A' in largest_point1[two_cards] and (spade == 1):
            ngaw_tongku += 1
    if pictures_count == 5:
        print("You have got five pictures!!!")
    else:
        if ngaw_tongku >= 1:
            print("You have got ngaw tong ku !!!")
        else:
            if double == 0:
                for two_cards in range(len(largest_point1)):
                    for i in range(len(largest_point1)):
                        if 'J' in largest_point1[two_cards] or \
                                'Q' in largest_point1[two_cards] or \
                                'K' in largest_point1[two_cards]:
                            while largest_point1[two_cards][i] == 'J' or \
                                    largest_point1[two_cards][i] == 'Q' or \
                                    largest_point1[two_cards][i] == 'K':
                                largest_point1[two_cards][i] = 10

                        if 'J' in largest_point2[two_cards] or \
                                'Q' in largest_point2[two_cards] or \
                                'K' in largest_point2[two_cards]:
                            while largest_point2[two_cards][i] == 'J' or \
                                    largest_point2[two_cards][i] == 'Q' or \
                                    largest_point2[two_cards][i] == 'K':
                                largest_point2[two_cards][i] = 10
                        if 'A' in largest_point1[two_cards]:
                            while largest_point1[two_cards][i] == 'A':
                                largest_point1[two_cards][i] = 1
                        if 'A' in largest_point2[two_cards]:
                            while largest_point2[two_cards][i] == 'A':
                                largest_point2[two_cards][i] = 1

                    point1 = sum(largest_point1[two_cards]) % 10
                    if point1 == 0:
                        point_array.append(10)
                    else:
                        point_array.append(point1)
                    point2 = sum(largest_point2[two_cards]) % 10
                    point_array.append(point2)
                print("Your final score is: ", max(point_array))

            elif double >= 1:
                if len(double_array) == 1:
                    print("Your final score is: Double", double_array[0])
                else:
                    if double_array[0] == double_array[1]:
                        print("Your final score is: Double", double_array[0])
                    else:
                        print("\nYou have", len(double_array), "doubles")
                        for i in range(len(double_array)):
                            print("Final score", i+1, "is: Double", double_array[i])

elif len(ngaw_zai) == 0:
    print("没有点 / no points")
