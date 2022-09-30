import numpy as np
import copy
import random
import math

def different_column_violations(sol):

    conflicts = 0

    for i in range(len(sol)):
        for j in range(len(sol)):
            if (i != j) and (sol[i] == sol[j]):
                conflicts += 1

    return conflicts


def different_diagonal_violations(sol):

    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            deltay = abs(sol[i]-sol[j])
            deltax = abs(i - j)
            if (deltay == deltax):
                conflicts += 1

    return conflicts


def obj(sol):
    return different_diagonal_violations(sol) + different_column_violations(sol)


def rand_in_rand_position(sol):

    neighbor = copy.copy(sol)

    idx = np.random.randint(0, len(sol))
    value = np.random.randint(0, len(sol))

    neighbor[idx] = value

    return neighbor


def swap(sol):

    neighbor = copy.copy(sol)

    idx1 = np.random.randint(0, len(sol))
    idx2 = np.random.randint(0, len(sol))

    neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

    return neighbor


def local_search(sol, objective, get_neighbor, maxit=50):

    best_val = objective(sol)
    it = 0
    while it <= maxit:
        n = get_neighbor(sol)
        n_val = objective(n)
        if n_val < best_val:
            sol = n
            best_val = n_val

        print(f'{it} : {best_val}')

        it += 1

    return sol, best_val

def simulated_annealing(sol, objective, get_neighbor, temp_inicial, temp_final, SAmax, alpha):

    temp = temp_inicial
    iterT = 0
    val = best_val = objective(sol)
    best_sol = sol

    while (temp > temp_final):
        while (iterT < SAmax):
            iterT += 1
            sol_viz = get_neighbor(sol)
            val_viz = objective(sol_viz)
            delta = val_viz - val

            if(delta < 0):
                if(val_viz < best_val):
                    best_sol = sol_viz
                    best_val = val_viz
                    print("aceitei melhora")
            else:
                x = random.uniform(0, 1)
                if(x < math.exp(-delta / temp)):
                    sol = sol_viz
        temp *= alpha
        print("{:.2f}".format(round(temp, 2)), " - " ,f'{best_val}')
        iterT = 0

    sol = best_sol

    return sol, best_val

if __name__ == '__main__':

    sol = [0, 1, 2, 3, 4, 5, 6, 7]
    temp_inicial = 2000
    temp_final = 5
    SAmax = 1000
    alpha = 0.8

    # sol, val = local_search(sol, obj, swap, maxit=100)
    sol, val = simulated_annealing(sol, obj, rand_in_rand_position, temp_inicial, temp_final, SAmax, alpha)

    print(sol)
    print(val)
