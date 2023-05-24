# def interview(lst: list, tot: int) -> str:
#     if len(lst) < 8:
#         print("disqualified")
#         return "disqualified"
#     if tot > 120:
#         print("disqualified")
#         return "disqualified"
#     # Very easy questions
#     if lst[0] > 5 or lst[1] > 5:
#         print("disqualified")
#         return "disqualified"
#     # Easy questions
#     if lst[2] > 10 or lst[3] > 10:
#         print("disqualified")
#         return "disqualified"
#     # Medium questions
#     if lst[4] > 15 or lst[5] > 15:
#         print("disqualified")
#         return "disqualified"
#     # Hard questions
#     if lst[6] > 20 or lst[7] > 20:
#         print("disqualified")
#         return "disqualified"
#     print("qualified")
#     return "qualified"

# def interview(lst: list, tot: int) -> str:
#     if len(lst) < 8 or tot > 120 or lst[0] > 5 or lst[1] > 5 or lst[2] > 10 or lst[3] > 10 or lst[4] > 15 or lst[5] > \
#             15 or lst[6] > 20 or lst[7] > 20 or lst[6] > 20 or lst[7] > 20:
#         return "disqualified"
#     return "qualified"


def interview(lst: list, tot: int) -> str:
    # Checks if all questions are completed and within time limit
    if len(lst) < 8 or tot > 120:
        return "disqualified"
    # Very easy questions
    if lst[0] > 5 or lst[1] > 5:
        return "disqualified"
    # Easy questions
    if lst[2] > 10 or lst[3] > 10:
        return "disqualified"
    # Medium questions
    if lst[4] > 15 or lst[5] > 15:
        return "disqualified"
    # Hard questions
    if lst[6] > 20 or lst[7] > 20:
        return "disqualified"
    return "qualified"


interview([5, 5, 10, 10, 15, 15, 20, 20], 120)  # ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64)  # ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120)  # ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120)  # ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130)  # ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.


# def interview2(lst: list, tot: int) -> str:
#     qualified = False
#     for l in lst:
#         if



# Working
# def interview(lst: list, tot: int) -> str:
#     if len(lst) < 8:
#         return "disqualified"
#     if tot > 120:
#         return "disqualified"
#     # Very easy questions
#     if lst[0] > 5 or lst[1] > 5:
#         return "disqualified"
#     # Easy questions
#     if lst[2] > 10 or lst[3] > 10:
#         return "disqualified"
#     # Medium questions
#     if lst[4] > 15 or lst[5] > 15:
#         return "disqualified"
#     # Hard questions
#     if lst[6] > 20 or lst[7] > 20:
#         return "disqualified"
#     return "qualified"