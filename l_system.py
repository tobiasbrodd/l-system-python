import numpy as np
from matplotlib import pyplot as plt
from system import PlantSystem, TreeSystem

def generate_sequence(rules, sequence, N=3):
    for i in range(N):
        new_sequence = ""
        for c in sequence:
            new_sequence += rules[c]
        sequence = new_sequence
    return sequence

def generate_tree_sequence_optimized(rules, N=3):
    if N == 0:
        return "0"
    left_sequence = "1"
    right_sequence = "0"
    sequence = left_sequence + "[0]" + right_sequence
    if N == 1:
        return sequence
    for i in range(N-1):
        new_left_sequence= ""
        new_right_sequence = ""
        for l in left_sequence:
            new_left_sequence += rules[l]
        for r in right_sequence:
            new_right_sequence += rules[r]
        sequence = new_left_sequence + "[" + sequence + "]" + new_right_sequence
        left_sequence = new_left_sequence
        right_sequence = new_right_sequence
    return sequence


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
plant_sequence = generate_sequence(plant_system.rules, plant_system.start, N=5)
plant_fig = plot_system(plant_system, plant_sequence)
plant_fig.savefig("plant.png")

tree_system = TreeSystem()
tree_sequence = generate_sequence(tree_system.rules, tree_system.start, N=10)
tree_fig = plot_system(tree_system, tree_sequence)
plt.show()
tree_fig.savefig("tree.png")