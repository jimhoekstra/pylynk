from models import Planet, Moon


if __name__ == '__main__':
    planets = Planet.all()
    for planet in planets:
        print(planet)
        print(planet.relations)

    # moons = Moon.all()
    # for moon in moons:
    #     print(moon)
