# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, template="Hello, <name>!"):
    template = template.replace("<name>", "{name}")
    return template.format(name=name)


print(greet("Anne", "how's it hanging, <name>?"))


def force(mass, body="earth"):
    gravity = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    return round(mass * gravity[body], 1)


print(force(3.14))


def pull(m1, m2, d):
    G = 0.00000000006674
    print(G)
    F = G * ((m1 * m2) / d ** 2)
    print(round(F, 10))
    return FP


print(pull(800, 1500, 3))
