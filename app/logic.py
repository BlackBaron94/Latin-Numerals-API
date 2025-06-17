from random import randint


class number:

    def __init__(self, latin, decimal):
        self.latin = latin
        self.decimal = decimal

    def return_value(self):
        return self.decimal


def create_numerals_list():
    """
    Creates numerals classes and array containing each instance of
    the class.


    Args:
        None.

    Returns:
        list (number): A list of number class objects representing all numerals.
    """
    i = number("I", 1)
    v = number("V", 5)
    x = number("X", 10)
    l = number("L", 50)
    c = number("C", 100)
    d = number("D", 500)
    m = number("M", 1000)
    numerals = [i, v, x, l, c, d, m]
    return numerals


def randomize():
    """
    Decides Latin to Decimal or vice versa.


    Returns:
        str: Random number in Latin or Decimal.
    """
    random_type = randint(0, 1)

    random_number = randint(0, 3999)
    # 0 == Requests Decimal to Latin
    if random_type:
        return str(random_number)
    # 1 == find out Latin version, request Latin to Decimal
    else:
        random_latin = dec2lat(random_number)
        return random_latin


def purify_input(input_string):
    """
    Retains only latin numerals present in string.


    Args:
        input_string(str): The string entered by the user.

    Returns:
        str: Stripped string of all non latin numeral characters.
    """
    purified_string = ""
    for letter in input_string:
        letter = str(letter).capitalize()
        if letter not in "IVXLCDM":
            continue
        else:
            purified_string = purified_string + letter

    return purified_string


def letter_conversion(
    letter: str,
) -> int:
    """
    Evaluates each Latin numeral to its decimal value.


    Args:
        letter (str): The letter to be evaluated.

    Returns:
        int: The value of letter passed.
    """
    numerals = create_numerals_list()
    # Handles "None" case
    if letter:
        for y in numerals:
            if letter == y.latin:
                return y.return_value()
    else:
        return 0


def lat2dec(my_num):
    """
    Translates a sequence of Latin numerals to their decimal value.


    Args:
        my_num (str): User input string.

    Returns:
        list: The result list has one of the following formats:

            If input is valid:
                [True, int]:
                    [0] (boolean): Flag for correct input.
                    [1] (int): Value of Latin numerals.

            If input is invalid:
                [False, str]:
                    [0] (boolean): Flag indicating error.
                    [1] (str): The letter that was misused (V/L/D in this case).

                or

                [False, str, str]:
                    [0] (boolean): Flag indicating error.
                    [1] (str): The misused character that is less than 1/10
                    of next character.
                    [2] (str): The misused character that is more than [1] * 10.

    """
    my_num = purify_input(my_num)
    # If string doesn't contain any numerals
    if len(my_num) == 0:
        return [False, False]

    # # Maximum length for consecutive M's ~ 15.000
    current_milleniums = 15
    for index in range(0, len(my_num)):
        if my_num[index] != "M":
            break
        else:
            current_milleniums -= 1
    if current_milleniums < 1:
        return [False, "M"]

    # Checks if same numeral appears more than 3 times
    same_letter = 0
    for index in range(0, len(my_num) - 1):
        # Exception for 4000+ taking lack of V̅ into consideration
        if my_num[index] == my_num[index + 1] and my_num[index] != "M":
            same_letter += 1
        # Counter needs to reset to allow numbers like XXXIX = 39
        else:
            same_letter = 0
        if same_letter > 2:
            return [False, my_num[index]]

    my_sum = 0
    index = 0
    while index < len(my_num):
        current_value = letter_conversion(my_num[index])
        # Checks if VLD are repeated
        if int(current_value) in (500, 50, 5):
            i = index + 1
            while i <= len(my_num) - 1:
                tested_value = letter_conversion(my_num[i])
                # Checks for VIX scenarios, V L D aren't allowed to be
                # followed by a greater value than themselves
                if my_num[index] == my_num[i] or int(current_value) < int(
                    tested_value
                ):
                    return [False, my_num[index]]
                i += 1

        # Check if current letter is the last letter
        # If it's not, calculates next letter
        if index != (len(my_num) - 1):
            next_letter = my_num[index + 1]

        # If it is, next_letter = none

        else:
            next_letter = None

        # Returns value from letter_conversion (0 if None)
        next_value = letter_conversion(next_letter)

        # Checks for IV, IX etc reductions of V/X/... values by I/X/... values
        if current_value < next_value:

            # Checks if VLD are placed before an XCM respectively
            if (int(current_value / 5) in (100, 10, 1)) and (
                current_value < next_value
            ):
                return [False, my_num[index]]

            # Checks wrongful use, e.g. IC or VM
            if (next_value != 0) and (current_value / next_value < 0.1):
                return [False, my_num[index], my_num[index + 1]]

            # Checks if previous letter was also same letter, which is
            # a mistake for a reduction case, like XIIX
            # Makes sure current letter is not first one, or else it would
            # compare to last letter ( array [-1] )
            if (my_num[index - 1] == my_num[index]) and (index != 0):
                return [False, my_num[index]]

            try:
                # Checks for IXI/XCX etc
                if my_num[index + 2] == my_num[index]:
                    return [False, my_num[index]]
                # Checks for IXV/XCL/XIVM/IVD etc
                elif letter_conversion(my_num[index + 2]) > current_value:
                    return [False, my_num[index + 2]]
            # No harm done by *pass* in this case, mistake is impossible
            except IndexError:
                pass

            # Increases sum by V-I = 4, X-I = 9 etc
            my_sum = my_sum + (next_value - current_value)

            # If next letter isn't the last one
            if index + 1 < len(my_num) - 1:
                # Skip next letter
                # Example
                # (for IV, (V-I) is already calculated,
                # V shouldn't be counted again)
                index += 2
                continue

            # If next letter is last one, calculation is done already
            else:
                break

        # If next value is less than current, current needs to be added
        # and next to be checked in its own iteration
        else:
            my_sum = my_sum + current_value
            index += 1

    return [True, my_sum]


def dec2lat(my_num_str):
    """
    Translates decimals to latin.


    Args:
        my_num_str (str): A string of an integer.

    Returns:
        str: The latin representation of the decimal number.
        Returns False if input was not only decimal integers.
    """

    # Tries to get an integer out of input string
    try:
        my_num_int = int(my_num_str)
        if my_num_int < 1 or my_num_int > 9999:
            raise ValueError
    # If input string contains non-decimals or negative numbers
    except ValueError:
        return False

    # *THIS WORKS UP TO 3999*
    digits = []
    divider = 1000
    latin = ""
    # Grabs each digit by dividing seperately, if none, grabs 0
    # 1st iteration [0]/1000, 2nd [1]/100 etc
    for index in range(0, 4):
        # Division and adding digit
        digits.append(int(my_num_int // divider))
        # Reduces main number by digit * place, e.g. if [0] was 4, then -4*1000
        my_num_int = my_num_int - digits[index] * divider
        # Reduces divider for next iteration from 10^x to 10^x-1
        divider = divider / 10

    numerals = create_numerals_list()
    # Thousands are calculated differently due to limitations
    # E.g. 4000 = MMMM instead of MV̅ due to character limitations
    if digits[0]:
        latin += numerals[-1].latin * digits[0]

    # Rest of the digits are calculated through digit_conversion()
    for index in range(1, 4):
        # Zeros are handled here
        if digits[index]:
            latin += digit_conversion(digits, index)
    return latin


def digit_conversion(digits_array, digit_num):
    """
    Converts a certain digit to the corresponding latin numeral(s).


    Args:
        digits_array (list): A list containing all digits, including zeros.
        digit_num (int): Index of number to be converted.

    Returns:
        str: Latin numeral(s) corresponding to value of indexed number.
    """

    return_string = ""

    # digit 1 base value 100,
    # digit 2 base value 10,
    # digit 3 base value 1

    # Calculates which base value applies for current digit_num
    # e.g. if the digit_num(index) is 3,
    # then the number has base value 10^0 = 1
    base_value = pow(10, (3 - digit_num))

    # Subset to be used for this particular digit
    subset = []
    numerals = create_numerals_list()

    # Subset[0] is base_value
    # Checks which numeral has the base value we're looking for, I/X/C
    for numeral in numerals:
        if numeral.decimal == base_value:
            subset.append(numeral)
            break

    # Subset[1] is used in case of digit being a 9,
    # e.g. X base value requiring C to depict 90, XC
    for numeral in numerals:
        if numeral.decimal == base_value * 10:
            subset.append(numeral)
            break

    # Subset[2] is used in case of digit being "near" a 5,
    # e.g. X base value requiring L to depict 60, LX
    for numeral in numerals:
        if numeral.decimal == base_value * 5:
            subset.append(numeral)
            break

    # Checks examined digit
    if digits_array[digit_num] == 9:
        # Appends to string the numeral that's given by x, x*10 like IX, XC, CM
        return_string = return_string + subset[0].latin
        return_string = return_string + subset[1].latin

    elif digits_array[digit_num] >= 5:
        # Since it's >= 5 we definetely need subset[2] first (V,L,D)
        return_string = return_string + subset[2].latin
        # If it's > 5, we need to append base value X times, where X = number-5
        # e.g. if number is 7, we need to append base value 7-5=2 times e.g. DCC
        if digits_array[digit_num] > 5:
            return_string = return_string + (
                subset[0].latin * (digits_array[digit_num] - 5)
            )

    elif digits_array[digit_num] == 4:
        # 4 requires special handling as it's the only case where base_value is
        # placed right before subset[2] (IV, XL, CD)
        return_string = return_string + subset[0].latin
        return_string = return_string + subset[2].latin

    # Basically when <= 3, append base value * number.
    else:
        return_string = return_string + (
            subset[0].latin * digits_array[digit_num]
        )
    return return_string


def handle_translation_input(user_input: str, direction: str) -> str:
    """
    Function that receives input to be translated entered in the translator
    window, checks translation direction and translates or returns
    relative error message. Translation handled either by lat2dec() or dec2lat.
    Input is purified using purify_input() to redisplay in a decent manner in
    result.


    Args:
        user_input (str): User input as gotten from UI
        direction (str): Indicated direction of translation.

    Returns:
        str: String for message to be displayed, if input was valid it's the
        translation of input, or in any other case a relative error message.
    """
    # Checks direction of translation
    if direction == "Latin to Decimal":

        result = lat2dec(user_input)

        # Checks if string is free of mistakes
        if result[0]:
            # Purifies input to display correctly
            purified_input = purify_input(str(user_input))
            return "Result: " + str(purified_input + " is " + str(result[1]))

        # String has mistakes
        else:
            # Checks secondary mistake flag (non numeral strings)
            if not result[1]:
                return "Invalid input"
            # Main case of mistake, e.g. VV
            elif len(result) == 2:
                return "Invalid input,\n'" + result[1] + "' wrongfully used."

            # Special case of rule #3 mistake
            else:
                return str(
                    "Invalid input,\n'"
                    + result[1]
                    + "' wrongfully used before '"
                    + result[2]
                    + "'. \nCheck rule #3."
                )

    else:
        result = dec2lat(user_input)
        if result:
            return "Result: " + str(user_input + " is " + str(result))
        elif result == False:
            return "Invalid input"


def handle_quiz_input(
    question_number: str, user_input: str, quiz_streak: int
) -> tuple[str, int]:
    """
    Function that receives a quiz question number, the user's input and the
    current quiz streak, checks if the correctness of user's input,
    updates and returns quyz streak and prepares a message for the result to
    display.


    Args:
        question_number (str): The number displayed as a quiz to be translated.
        user_input (str): The answer the user has entered.
        quiz_streak (int): Current correct quiz answers streak.

    Returns:
        tuple(str, int): Message to be displayed and updated quiz streak.
    """

    initial_input = user_input
    # Checks if first string character is latin in question text
    if question_number[0] in "IVXLCDM":
        try:
            # Double typecasting to get rid of starting 0s
            user_input = str(int(user_input))
        except ValueError:
            # Sends relative message and resets quiz streak
            return ("Invalid input. Please use decimals only.", 0)
        correct_answer = lat2dec(question_number)
        # lat2dec returns array, since question text is controlled
        # it's always len = 2, [0] = True, [1] = *translation*
        correct_answer = str(correct_answer[1])
    else:
        correct_answer = dec2lat(question_number)
        # Purifies user's latin input
        user_input = purify_input(user_input)
    # If user input is latin, it's been purified so it matches perfectly
    if user_input == correct_answer:

        result_message = "Your answer is correct!\n{0} is {1}".format(
            question_number, user_input
        )
        # Adds +1 to correct streak
        quiz_streak += 1

        # Displays streak # and a message for high correct streaks
        if quiz_streak > 19:
            result_message = (
                result_message
                + "\n"
                + str(quiz_streak)
                + " correct answers streak!!! \nYou're on FIRE!!!"
            )

        elif quiz_streak > 9:
            result_message = (
                result_message
                + "\n"
                + str(quiz_streak)
                + " correct answers streak!! \nYou're on a roll!!"
            )
        elif quiz_streak > 4:
            result_message = (
                result_message
                + "\n"
                + str(quiz_streak)
                + " correct answers streak!"
            )
        return (result_message, quiz_streak)
    # Answer was incorrect
    else:
        # Shows input's correct answer as opposed to user's wrong answer
        result_message = "Your answer is wrong.\n{0} is {1}, not '{2}'".format(
            question_number, correct_answer, initial_input
        )
        # Resets correct streak
        quiz_streak = 0
        return (result_message, quiz_streak)
