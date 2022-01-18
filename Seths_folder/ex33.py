numbers = []

def loop(top, inc):
	i = 0
	while i < top:
		print(f"At the top i is {i}")
		numbers.append(i)

		i += inc
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

loop(int(input("Choose a top number: ")), int(input("Choose increment: ")))

print("The numbers: ")

for num in numbers:
	print(num)
