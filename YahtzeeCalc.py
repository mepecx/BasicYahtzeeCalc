from tokenize import Number


class Yahtzee:
    def __init__(self, rolls):
        self.rolls = rolls

    def checkOnes(self):
        ones_score = 0
        number_of_ones = 0
        for i in self.rolls:
            if i == 1:
                ones_score += 1
                number_of_ones += 1
        return ones_score

    def checkTwos(self):
        twos_score = 0
        number_of_twos = 0
        for i in self.rolls:
            if i == 2:
                twos_score += 2
                number_of_twos += 1
        return twos_score

    def checkThrees(self):
        threes_score = 0
        number_of_threes = 0
        for i in self.rolls:
            if i == 3:
                threes_score += 3
                number_of_threes += 1
        return threes_score

    def checkFours(self):
        fours_score = 0
        number_of_fours = 0
        for i in self.rolls:
            if i == 4:
                fours_score += 4
                number_of_fours += 1
        return fours_score

    def checkFives(self):
        fives_score = 0
        number_of_fives = 0
        for i in self.rolls:
            if i == 5:
                fives_score += 5
                number_of_fives += 1
        return fives_score

    def checkSixes(self):
        sixes_score = 0
        number_of_sixes = 0
        for i in self.rolls:
            if i == 6:
                sixes_score += 6
                number_of_sixes += 1
        return sixes_score

    def checkThreeOfAKind(self):
        three_of_a_kind_score = 0
        for i in self.rolls:
            if self.rolls.count(i) >= 3:
                three_of_a_kind_score = sum(self.rolls)
        return three_of_a_kind_score

    def checkFourOfAKind(self):
        four_of_a_kind_score = 0
        for i in self.rolls:
            if self.rolls.count(i) >= 4:
                four_of_a_kind_score = sum(self.rolls)
        return four_of_a_kind_score

    def checkFullHouse(self):
        full_house_score = 0
        used_nums = []
        for i in self.rolls:
            if self.rolls.count(i) >= 3:
                used_nums.append(i)
                for j in self.rolls:
                    if self.rolls.count(j) >= 2 and j not in used_nums:
                        full_house_score = 25
        return full_house_score

    def checkSmallStraight(self):
        small_straight_score = 0
        sortedRoll = sorted(self.rolls)
        if sortedRoll == [1, 2, 3, 4, 5] or sortedRoll == [1, 2, 3, 4, 6] or sortedRoll == [2, 3, 4, 5, 6] or sortedRoll == [1, 3, 4, 5, 6]:
            small_straight_score = 30
        return small_straight_score

    def checkLargeStraight(self):
        large_straight_score = 0
        if sorted(self.rolls) == [1, 2, 3, 4, 5] or sorted(self.rolls) == [2, 3, 4, 5, 6]:
            large_straight_score = 40
        return large_straight_score

    def checkYahtzee(self):
        yahtzee_score = 0
        for i in self.rolls:
            if self.rolls.count(i) == 5:
                yahtzee_score = 50
        return yahtzee_score

    def checkChance(self):
        return sum(self.rolls)

    def showPossibleMoves(self):
        possibleMoves = []
        if self.checkOnes() != 0:
            possibleMoves.append("Ones with a score of " + str(self.checkOnes()))
        if self.checkTwos() != 0:
            possibleMoves.append("Twos with a score of " + str(self.checkTwos()))
        if self.checkThrees() != 0:
            possibleMoves.append("Threes with a score of " + str(self.checkThrees()))
        if self.checkFours() != 0:
            possibleMoves.append("Fours with a score of " + str(self.checkFours()))
        if self.checkFives() != 0:
            possibleMoves.append("Fives with a score of " + str(self.checkFives()))
        if self.checkSixes() != 0:
            possibleMoves.append("Sixes with a score of " + str(self.checkSixes()))
        if self.checkThreeOfAKind() != 0:
            possibleMoves.append("Three of a kind with a score of " + str(self.checkThreeOfAKind()))
        if self.checkFourOfAKind() != 0:
            possibleMoves.append("Four of a kind with a score of " + str(self.checkFourOfAKind()))
        if self.checkFullHouse() != 0:
            possibleMoves.append("Full house with a score of " + str(self.checkFullHouse()))
        if self.checkSmallStraight() != 0:
            possibleMoves.append("Small straight with a score of " + str(self.checkSmallStraight()))
        if self.checkLargeStraight() != 0:
            possibleMoves.append("Large straight with a score of " + str(self.checkLargeStraight()))
        if self.checkYahtzee() != 0:
            possibleMoves.append("Yahtzee with a score of " + str(self.checkYahtzee()))
        if self.checkChance() != 0:
            possibleMoves.append("Chance with a score of " + str(self.checkChance()))
        if len(possibleMoves) == 0:
            possibleMoves.append("No possible moves. Must put a 0 in some category. :'( ")
        return possibleMoves
    
usedMoves = []
gameGoing = True
score = 0
while gameGoing:
    rolls = []
    for i in range(5):
        rolls.append(int(input("Enter a number: ")))
    
    print("\n")
    print("===================================================")
    print("       Your rolls were: " + str(rolls))
    print("===================================================")
    print("\n")

    yahtzee = Yahtzee(rolls)
    possibleMoves = yahtzee.showPossibleMoves()
    for move in possibleMoves:
        if move not in usedMoves:
            print(move)
            print("----------------------------")

    print("----------------------------")
    print("Your current score: " + str(score))
    print("\n")
    print("Ones | Twos | Threes | Fours | Fives | Sixes | Three of a kind | Four of a kind | Full house | Small straight | Large straight | Yahtzee")
    using_move = input("Which move would you like to use? ")
    print("\n")
    
    if using_move == "Ones":
        usedMoves.append("Ones with a score of " + str(yahtzee.checkOnes()))
        score += yahtzee.checkOnes()
    elif using_move == "Twos":
        usedMoves.append("Twos with a score of " + str(yahtzee.checkTwos()))
        score += yahtzee.checkTwos()
    elif using_move == "Threes":
        usedMoves.append("Threes with a score of " + str(yahtzee.checkThrees()))
        score += yahtzee.checkThrees()
    elif using_move == "Fours":
        usedMoves.append("Fours with a score of " + str(yahtzee.checkFours()))
        score += yahtzee.checkFours()
    elif using_move == "Fives":
        usedMoves.append("Fives with a score of " + str(yahtzee.checkFives()))
        score += yahtzee.checkFives()
    elif using_move == "Sixes":
        usedMoves.append("Sixes with a score of " + str(yahtzee.checkSixes()))
        score += yahtzee.checkSixes()
    elif using_move == "Three of a kind":
        usedMoves.append("Three of a kind with a score of " + str(yahtzee.checkThreeOfAKind()))
        score += yahtzee.checkThreeOfAKind()
    elif using_move == "Four of a kind":
        usedMoves.append("Four of a kind with a score of " + str(yahtzee.checkFourOfAKind()))
        score += yahtzee.checkFourOfAKind()
    elif using_move == "Full house":
        usedMoves.append("Full house with a score of " + str(yahtzee.checkFullHouse()))
        score += yahtzee.checkFullHouse()
    elif using_move == "Small straight":
        usedMoves.append("Small straight with a score of " + str(yahtzee.checkSmallStraight()))
        score += yahtzee.checkSmallStraight()
    elif using_move == "Large straight":
        usedMoves.append("Large straight with a score of " + str(yahtzee.checkLargeStraight()))
        score += yahtzee.checkLargeStraight()
    elif using_move == "Yahtzee":
        usedMoves.append("Yahtzee with a score of " + str(yahtzee.checkYahtzee()))
        score += yahtzee.checkYahtzee()
    elif using_move == "Chance":
        usedMoves.append("Chance with a score of " + str(yahtzee.checkChance()))
        score += yahtzee.checkChance()
    else:
        print("Invalid move")
        print("\n")
        continue

    print("\n")
    playAgain = input("Would you like to roll again? (y/n): ")
    if playAgain == "n":
        gameGoing = False

