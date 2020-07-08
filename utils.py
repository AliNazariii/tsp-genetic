import matplotlib.pyplot as plt
from gene import Gene

def parse_input(input_path):
    file = open(input_path, 'r')
    cities = []
    for line in file:
        info = list(map(float, line.split()))
        cities.append(Gene(int(info[0]), info[1], info[2]))
    file.close()
    return cities

def plot(costs, route, save_to=None):
    plt.figure(1)
    plot_convergence(costs)
    plt.show()

    plt.figure(2)
    plot_route(route)
    plt.show()

def plot_convergence(costs):
    x = range(len(costs))
    plt.title("GA Convergence")
    plt.xlabel('generation')
    plt.ylabel('cost')
    plt.text(x[len(x) // 2], costs[0],
             'min cost: {}'.format(costs[-1]), ha='center', va='center')
    plt.plot(x, costs, '-')

def plot_route(route):
    for i in range(len(route) - 1):
        x = [route[i].x, route[i + 1].x]
        y = [route[i].y, route[i + 1].y]
        plt.plot(x, y)
    
    x = [route[0].x, route[-1].x]
    y = [route[0].y, route[-1].y]
    plt.plot(x,y)
    plt.show()