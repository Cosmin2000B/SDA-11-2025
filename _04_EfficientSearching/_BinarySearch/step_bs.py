##
# hidden = (-24, 15)
# hidden = (24, -15)
# hidden = (-24, -15)
hidden = (24, 15)

def ask(x1, x2):
    if (x1[0] - hidden[0]) ** 2 + (x1[1] - hidden[1]) ** 2 < (x2[0] - hidden[0]) ** 2 + (x2[1] - hidden[1]) ** 2:
        return x1
    return x2

# pas 1: det cadran
step = [ask((-1, 0), (1, 0))[0], ask((0, -1), (0, 1))[1]]
print ("step=", step)

# pas 2: det celelalte doua margini ale dreptunghiului care il cuprinde pe hidden
for i in range(2):
    x1 = (step[i], 0) if  i == 0 else (0, step[i])
     
    while ask(x1, (0, 0)) == x1:
        step[i] *= 2
        x1 = (step[i], 0) if i == 0 else (0, step[i])

print(f"step 2 {step = }")

# step 3
p1, p2 = [step[0] / 2, step[1] / 2], [0, 0]
for _ in range(10):
    for i in range(2):
        # mid = ((x1[0] + x2[0]) / 2, 0) if i == 0 else (0, x1[1] + x2[1] / 2)
        x1, x2 = ((p1[i], 0), (p2[i], 0)) if i == 0 else ((0, p1[i]), (0, p2[i]))
        if ask(x1, x2) == x1:
            p2[i] = (p1[i] + p2[i]) / 2
        else:
            p1[i] = (p1[i] + p2[i]) / 2
    print(f"iter {_+1} finished, {p1 = }, {p2 = }")    