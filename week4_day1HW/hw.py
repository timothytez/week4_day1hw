
#O(N^2)
# this time complexity is nested due to finding a firework that will perform within a time frame of the show.
#There are `n` types of fireworks
#for each type, there’s a specific amount of time it takes to launch that firework.
def create_show(fireworks, show_time):
    fireworks.sort()

    show = []

    remaining_time = show_time


    while remaining_time > 0 and fireworks: #O(N)

           # Select a random firework

           firework = random.choice(fireworks) #O(N)


           if firework <= remaining_time:

               # Add the firework to the show

               show.append(firework) # O(1)

               remaining_time -= firework

    else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework) #O(1)

    return show


