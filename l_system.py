import numpy as np
import time
from matplotlib import pyplot as plt
from system import PlantSystem, TreeSystem

def generate_system(rules, system, N=3):
    for i in range(N):
        new_system = ""
        for c in system:
            new_system += rules[c]
        system = new_system
    return system

def plot_system(system, sequence, x_org=1.0, y_org=0.0, l=1.0, a=90.0):
    stack = []
    fig, ax = plt.subplots()
    for c in sequence:
        if c in system.d_vars:
            x = x_org + l * np.cos(a*np.pi / 180)
            y = y_org + l * np.sin(a*np.pi / 180)
            ax.plot([x_org,x], [y_org,y], system.d_opt[c])
            x_org = x
            y_org = y
        if c in system.s_app_vars:
            stack.append((x_org, y_org, l, a))
        if c in system.s_pop_vars:
            x_org, y_org, l, a = stack.pop()
        if c in system.a_inc_vars:
            a += system.a_inc
        if c in system.a_dec_vars:
            a -= system.a_dec
    ax.set_aspect('equal')
    ax.set_axis_off()
    return fig

plant_system = PlantSystem()
plant_sequence = generate_system(plant_system.rules, plant_system.start, N=5)
plant_fig = plot_system(plant_system, plant_sequence)
plant_fig.savefig("plant.png")

tree_system = TreeSystem()
tree_sequence = generate_system(tree_system.rules, tree_system.start, N=10)
tree_fig = plot_system(tree_system, tree_sequence)
plt.show()
tree_fig.savefig("tree.png")