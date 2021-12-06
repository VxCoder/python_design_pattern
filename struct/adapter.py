class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} computer".format(self.name)

    def execute(self):
        return "executes a program"


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"the {self.name} synthesizer"

    def play(self):
        return "is playing an electronic song"


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} the human"

    def speak(self):
        return "says hello"


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

    def __getattr__(self, item):
        return getattr(self.obj, item)


def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for object in objects:
        print(f"{object} {object.execute()} {object.name}")


if __name__ == "__main__":
    main()
