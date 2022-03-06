import statistics
# This is our input
a = int(input("How many numbers are you using? "))
n = list(map(int, input("What are you're numbers ").strip().split()))
print(n)
#These are the results
print("Mean: ", statistics.mean(n))
print("Mode: ", statistics.mode(n))
print("Median: ", statistics.median(n))
