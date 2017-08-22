import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""

    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return (x,y)




if __name__ == "__main__":

    number_of_walks = 10000

    for walk_length in range(1,36):
        no_transport = 0
        for i in range(number_of_walks):
            x, y = random_walk(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 5:
                no_transport += 1

        no_transport_percentage = no_transport / number_of_walks

        print("Walk size: ", walk_length, "| no transport: ", 100 * no_transport_percentage, '%')
