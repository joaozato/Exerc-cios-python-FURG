scores = []
for x in range(10):
    student_register=input('SR: ')
    score = float(input('Score: '))
    result = [student_register, score]
    scores.append(result)

print ('quantity of scores', len(scores))

for s in scores:
    student_register= s[0]
    score = s[1]
    print("the SR", student_register, 'get the score ', score)
    


