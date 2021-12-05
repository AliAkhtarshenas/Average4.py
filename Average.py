name = input("name:")
family = input("family:")

sum = 0
tedade_nomarat = int(input("tedade_nomarat:"))
for i in range(tedade_nomarat):
    score = float(input("score:"))
    sum = sum + score

average = sum / tedade_nomarat

print("average:" ,average )