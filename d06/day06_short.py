# the position represents the current time, and the value represents the amount of fish with this timer value
fishShift = [0]*9
for fish_timer in [int(p) for p in open('input.txt', 'r').read().split(",")]:
    fishShift[fish_timer] += 1

for day in range(0, 256):
    fishShift = [fishShift[i+1] for i in range(8)] + [fishShift[0]] # shift array
    fishShift[6] += fishShift[8]  # reset zero fish-timer to 6 days, zeros are now in the 8th place after shift
    if day == 79:
        print("Part 1:", sum(fishShift))

print("Part 2: ", sum(fishShift))
