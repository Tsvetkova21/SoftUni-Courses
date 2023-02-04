occurrences = {}
for l in input():
    if l not in occurrences:
        occurrences[l] =0
    occurrences[l]+=1

for letter, times in sorted(occurrences.items()):
    print(f" {letter}: {times} time/s")