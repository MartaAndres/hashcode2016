import math

import Instance

instance = Instance.Instance.readInstance()


instructions = [[]]*instance.drones
drone_turn = 0
# x0 = instance.warehouses[0][0]
# y0 = instance.warehouses[0][1]
# drone_locations = [(x0,y0) for i in range(instance.drones)]
for j,order in enumerate(instance.orders): # ordenar por tamaño de pedido?
    # find closest warehouse with the item
    x2 = order[0]
    y2 = order[1]
    for item in order[2]:
        closest = 0
        dist = math.sqrt((x2-instance.warehouses[0][0])**2+(y2-instance.warehouses[0][1])**2)
        #for i,w in sorted(enumerate(instance.warehouses),key=lambda i,w: math.sqrt((x2-w[0])**2+(y2-w[1])**2)):
        for i,w in enumerate(instance.warehouses):
            if (w[2][item]) > 0 and math.sqrt((x2-w[0])**2+(y2-w[1])**2) < dist:
                closest = i
        instance.warehouses[closest][2][item] -= 1
        instructions[drone_turn].append((drone_turn,'L',closest,item,1))
        instructions[drone_turn].append((drone_turn,'D',j,item,1))
        drone_turn = (drone_turn + 1)%instance.drones

print(sum(len(i) for i in instructions))
for d in instructions:
    for i in d:
        print(*i)