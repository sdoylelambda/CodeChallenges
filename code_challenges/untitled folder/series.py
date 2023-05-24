def series_resistance(lst):
	output = 0
	for l in lst:
		output += l
	print(output)
	return output


series_resistance([1, 5, 6, 3])  # ➞ "15 ohms"
series_resistance([16, 3.5, 6])  # ➞ "25.5 ohms"
series_resistance([0.5, 0.5])  # ➞ "1.0 ohm"
