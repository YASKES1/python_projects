import matplotlib.pyplot as plt
import numpy as np
from elements import ElementData
from Bohr_model import BohrAtom


def visualize_atom_with_labels(identifier):
    element_data = ElementData()
    atom = BohrAtom(identifier, element_data)

    electron_config = atom.electron_config
    total_protons = atom.atomic_number
    total_neutrons = round(atom.atomic_mass) - total_protons

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    core_radius = 0.5  

    for i in range(total_protons):
        angle = 2 * np.pi * i / total_protons
        x = core_radius * np.cos(angle)
        y = core_radius * np.sin(angle)
        ax.plot(x, y, 'ro', markersize=10)
        ax.text(x, y, 'p', color='white', fontsize=8, ha='center',va='center')  

    for i in range(total_neutrons):
        angle = 2 * np.pi * i / total_neutrons + np.pi / total_neutrons  
        x = core_radius * 0.8 * np.cos(angle)  
        y = core_radius * 0.8 * np.sin(angle)
        ax.plot(x, y, 'yo', markersize=10)
        ax.text(x, y, 'n', color='black', fontsize=8, ha='center',va='center') 

    orbit_spacing = 2  
    for level, num_electrons in enumerate(electron_config):
        orbit_radius = (level + 1) * orbit_spacing
        orbit = plt.Circle((0, 0), orbit_radius, color='b', fill=False,
                           linestyle='--')
        ax.add_artist(orbit)


        for i in range(num_electrons):
            angle = 2 * np.pi * i / num_electrons
            x = orbit_radius * np.cos(angle)
            y = orbit_radius * np.sin(angle)
            ax.plot(x, y, 'bo', markersize=8)
            ax.text(x, y, 'e', color='white', fontsize=8, ha='center',
                    va='center') 


    ax.set_xlim(-orbit_spacing * (len(electron_config) + 1),
                orbit_spacing * (len(electron_config) + 1))
    ax.set_ylim(-orbit_spacing * (len(electron_config) + 1),
                orbit_spacing * (len(electron_config) + 1))
    ax.set_title(
        f'{atom.element_name} (Z = {atom.atomic_number}), Mass: {atom.atomic_mass} u')


    # ax.legend(loc='upper right')

    plt.show()


# визуализация атома по символу или номеру элемента
# visualize_atom_with_labels('He')  # По символу элемента
visualize_atom_with_labels(32)  # По номеру элемента

