'''
ou're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
'''
def calPoints(ops):
	
	pointsList = []
	for i in range(len(ops)):
		if ops[i] not in ["+", "D", "C"]:
			pointsList.append(int(ops[i]))
		elif ops[i] == "+":
			twoRoundPoints = pointsList[-1] + pointsList[-2]
			pointsList.append(twoRoundPoints)
		elif ops[i]  == "D":
			doubleRoundPoints = pointsList[-1] * 2
			pointsList.append(doubleRoundPoints)
		elif ops[i] == "C":
			pointsList.pop()
	
	return sum(pointsList)

if __name__ == '__main__':
	print(calPoints(["5","2","C","D","+"]))
	print(calPoints(["5","-2","4","C","D","9","+","+"]))
			