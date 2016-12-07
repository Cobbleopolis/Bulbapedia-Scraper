class Pokemon(object):

    def __init__(self, local_number, nat_number, name, types):
        self.local_number = local_number
        self.nat_number = nat_number
        self.name = name
        self.types = types

    def __str__(self):
        return str(self.local_number) + " | " + str(self.nat_number) + " | " + self.name + " | " + str(self.types)
