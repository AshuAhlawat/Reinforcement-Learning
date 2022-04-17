
def expn(data):
    data = 2.71828**(data)
    return data

def prob(dist):
    expo = []

    for val in dist:
        expo.append(expn(val))

    probs = []

    tot = sum(expo)
    for val in expo:
        probs.append(round(val/tot,5))

    return probs


av1 = -1.1
av2 = -1.0
av3 = -0.7

dist = [av1, av2, av3]

probablities = prob(dist)

print(probablities)
print(sum(probablities))