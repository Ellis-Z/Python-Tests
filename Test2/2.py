import random
aliens = []
colors = ['red','yellow','green','blue','pink','brown','purple']
speeds = ['slow','medium','fast']

for number in range (0,50):
    color = random.choice(colors)
    speed = random.choice(speeds)
    point = random.randrange(10,30)
    new_alien = {
                 'number': number,
                 'color': color,
                 'points': point,
                 'speed': speed
                }
    aliens.append(new_alien)


for i in range(0,7):
    for alien in aliens[0:50]:
        if alien['color'] == colors[i]:
            print(f'alien',alien)
print()
print()
print()
for i in range(0,3):
    for alien in aliens[0:50]:
        if alien['speed'] == speeds[i]:
            print(f'alien',alien)


