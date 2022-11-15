# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

# numbers =[1,2,3]
# # new_list = [new_item for item in list]
# new_list = [n+1 for n in numbers]
# print(new_list)

student_score ={
    "Alex": 89,
    "Beth": 98

},
passed_studnets = {
    "Beth":72,
    "Caroline":62
},
#
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
spliting_sentence =sentence.split()

result = {sen:len(sen) for sen in spliting_sentence}

print(result)





























