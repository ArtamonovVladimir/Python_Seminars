import math as mt

const_pi = mt.pi
# print(const_pi)
path = "6_Seminar\orbits_in.txt"
orbits = []
with open(path, 'r') as text:
    in_data = list(map(float, text.read().split(',')))
    print(in_data)

    for i in range(0, len(in_data)-1, 2):
        a = in_data[i]
        b = in_data[i+1]

        planet = (a, b)

        orbits.append(planet)

print(orbits)


def find_farthest_orbit(lst):
    planets_or = []
    for i in lst:
        x = i[0]*i[1]*const_pi
        planets_or.append(x)
    # print(planets_or)
    return planets_or.index(max(planets_or))


# print(*orbits[planets_or.index(max(planets_or))])
print(*orbits[find_farthest_orbit(orbits)])
