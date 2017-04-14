#python3
'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''
def readBinaryWatch(num):
	"""
        :type num: int
        :rtype: List[str]
        """
	from itertools import combinations
	timeList = []
	hourList = [8, 4, 2, 1]
	minuteList = [32, 16, 8, 4, 2, 1]
	
	for i in range(num + 1):
		hoursList = []
		minutesList = []
		hourLights = i
		minuteLights = num - i
		if i >= 4 or (num - i) >= 6:
			continue
		for hourCom in combinations(hourList, hourLights):
			if sum(hourCom) <= 11:
				hoursList.append(str(sum(hourCom)))
		for minuteCom in combinations(minuteList, minuteLights):
			if sum(minuteCom) <= 59:
				minutesList.append(str(sum(minuteCom)))
		
		if minutesList == []:
			for hour in hoursList:
				timeList.append(hour + ":" + "00")
		if hoursList == []:
			for minute in minutesList:
				timeList.append("0" + ":" + minute) if len(minute) == 2 else timeList.append("0" + ":" + "0" + minute)
		
		for hour in hoursList:
			for minute in minutesList:
				timeList.append(hour + ":" + minute) if len(minute) == 2 else timeList.append(hour + ":" + "0" + minute)
	
	return timeList
		
if __name__ == '__main__':
	print(readBinaryWatch(6))