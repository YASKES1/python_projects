from elements import ElementData


class BohrAtom:
    def __init__(self, identifier, element_data):
        if isinstance(identifier, int):
            self.element = element_data.get_element_by_number(
                identifier)
        elif isinstance(identifier, str):
            self.element = element_data.get_element_by_symbol(
                identifier.capitalize())

        if self.element:
            self.element_name = self.element['name']
            self.atomic_number = self.element['atomic_number']
            self.atomic_mass = self.element['atomic_mass']
            self.electron_config = self.element['electron_config']
        else:
            raise ValueError(
                f"Element with identifier {identifier} not found")

    def calculate_orbit_radius(self, n):
        r_n = 0.529 * n ** 2
        return r_n

    def calculate_energy_level(self, n):
        energy = -13.6 / n ** 2
        return energy
