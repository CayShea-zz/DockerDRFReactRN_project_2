class ChoicesMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.choices = tuple(
            (v[0], v[1]) if isinstance(v, tuple) else (v, v.title().replace("_", " "))
            for k, v in cls.__dict__.items()
            if not k.startswith("_")
        )
        cls.allowed_values = set(i[0] for i in cls.choices)
