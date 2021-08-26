from matplotlib import pyplot as plt
from shipmarker.shipmarker import shipmarker

ship1 = {
    'x' : 1,
    'y' : 2,
    'psi' : 90,
    'c' : 'r'
}

ship2 = {
    'x' : -1,
    'y' : 1,
    'psi' : 322,
    'c' : 'b'
}

ship3 = {
    'x' : 0,
    'y' : -2,
    'psi' : 180,
    'c' : 'g'
}

ships = [ship1, ship2, ship3]

for ship in ships:
    xm,ym,mm = shipmarker(ship['x'], ship['y'], ship['psi'])
    plt.scatter(xm, ym, marker=mm, s=100, color=ship['c'])
plt.show()