# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Part 1
def greet(name, greetTemplate="Hello, <name>!"):
    return greetTemplate.replace("<name>", name)


# part 2
def force(mass, body="earth"):
    gravity = {
        "earth": 9.8,
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6
    }
    return mass * gravity[body]


# part 3
def pull(m1, m2, d):
    G = 6.674*10**-11
    F = G * ((m1 * m2) / d**2)
    return F


greet("Bob")
greet("Bob", "What's up, <name>?")
force(0.1, "sun")
force(0.1, "earth")
pull(0.1, 5.972*10**24, 6.371*10**6)
