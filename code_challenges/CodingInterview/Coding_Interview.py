def interview(lst, tot):
    # The candidate should have complete all the questions and maximum time given to complete the interview is 120
    if len(lst) != 8 or tot > 120:
        print("disqualified")
        return "disqualified"

    # The maximum time given for very easy questions is 5 minutes each.
    if lst[0] > 5 or lst[1] > 5:
        print("disqualified")
        return "disqualified"
    # The maximum time given for easy questions is 10 minutes each.
    if lst[2] > 10 or lst[3] > 10:
        print("disqualified")
        return "disqualified"
    # The maximum time given for medium questions is 15 minutes each.
    if lst[4] > 15 or lst[5] > 15:
        print("disqualified")
        return "disqualified"
    # The maximum time given for hard questions is 20 minutes each.
    if lst[6] > 20 or lst[7] > 20:
        print("disqualified")
        return "disqualified"
    # If all the above conditions are satisfied, return "qualified", else return "disqualified".
    print("qualified")
    return "qualified"

    # You will be given a list of time taken by a candidate to solve a particular question and the total time taken by
    # the candidate to complete the interview.

    # Given a list , in a true condition will always be in the format
    # [very easy, very easy, easy, easy, medium, medium, hard, hard].


# Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120)  # ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64)  # ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120)  # ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120)  # ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130)  # ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
