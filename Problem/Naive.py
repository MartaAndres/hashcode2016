################################################################################
# Authors: Marta is saving us. You can! Come on!
# Date: 11 - February - 2016
################################################################################

import math

import InstanceNaive

instance = InstanceNaive.Instance.readInstance()


instructions = [[] for i in range(instance.drones)]
drone_turn = 0
x0 = instance.warehouses[0][0]
y0 = instance.warehouses[0][1]
drone_locations = [(x0,y0) for i in range(instance.drones)]
instance.orders.sort(key = lambda x: len(x[2]))# Sort taking into account number of orders and distance.
for order in instance.orders:
    order_no = order[3]
    # find closest warehouse with the item
    x2 = order[0]
    y2 = order[1]
    for item in order[2]:
        closest = 0
        dist = math.sqrt((x2-instance.warehouses[0][0])**2+(y2-instance.warehouses[0][1])**2)
        #for i,w in sorted(enumerate(instance.warehouses),key=lambda i,w: math.sqrt((x2-w[0])**2+(y2-w[1])**2)):
        for i,w in enumerate(instance.warehouses):
            if ((instance.warehouses[closest][2][item] <= 0) or 
                (w[2][item] > 0 and math.sqrt((x2-w[0])**2+(y2-w[1])**2) < dist)):
                dist = math.sqrt((x2-w[0])**2+(y2-w[1])**2) < dist
                closest = i
        instance.warehouses[closest][2][item] -= 1
        

        dist = math.sqrt((instance.warehouses[closest][0]-drone_locations[drone_turn][0])**2+(instance.warehouses[closest][1]-drone_locations[drone_turn][1])**2)
        for i,d in enumerate(drone_locations):
            if math.sqrt((instance.warehouses[closest][0]-d[0])**2+(instance.warehouses[closest][1]-d[1])**2) < dist:
                dist = math.sqrt((instance.warehouses[closest][0]-d[0])**2+(instance.warehouses[closest][1]-d[1])**2)
                drone_turn = i
            
        instructions[drone_turn].append((drone_turn,'L',closest,item,1))
        instructions[drone_turn].append((drone_turn,'D',order_no,item,1))
        drone_turn = (drone_turn + 1)%instance.drones
        
# cut off instructions that go past the deadline
for j,inst_list in enumerate(instructions):
    cutoff = len(inst_list)
    time = 0
    x,y = (instance.warehouses[0][0],instance.warehouses[0][1])
    for i,inst in enumerate(inst_list):
        if inst[1] == 'L':
            w = instance.warehouses[inst[2]]
            time += (math.ceil(math.sqrt((x-w[0])**2 + (y-w[1])**2)))+1
            x,y = w[0],w[1]
        elif inst[1] == 'D':
            o = instance.orders[inst[2]]
            time += (math.ceil(math.sqrt((x-o[0])**2 + (y-o[1])**2)))+1
            x,y = o[0],o[1]
        if time > instance.deadline:
            cutoff = i - (1 if inst[1] == 'D' else 0)
            break
    # Add extra instructions to next drone
    extras = instructions[j][cutoff:]
    if j+1 < instance.drones:
        extras = [(j+1,i[1],i[2],i[3],i[4]) for i in extras]
        instructions[j+1] += extras
    instructions[j] = instructions[j][:cutoff]

for j,inst_list in enumerate(instructions):
    time = 0
    x,y = (instance.warehouses[0][0],instance.warehouses[0][1])
    for i,inst in enumerate(inst_list):
        if inst[1] == 'L':
            w = instance.warehouses[inst[2]]
            time += (math.ceil(math.sqrt((x-w[0])**2 + (y-w[1])**2)))+1
            x,y = w[0],w[1]
        elif inst[1] == 'D':
            o = instance.orders[inst[2]]
            time += (math.ceil(math.sqrt((x-o[0])**2 + (y-o[1])**2)))+1
            x,y = o[0],o[1]

# print solutions
print(sum(len(i) for i in instructions))
for d in instructions:
    for i in d:
        print(*i)