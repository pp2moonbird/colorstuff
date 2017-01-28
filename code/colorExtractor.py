from PIL import Image, ImageDraw
import numpy as np


def kmeans(m, k):
    """
    :param m: input matrix
    :param k: number of clusters
    :return: cores of k clusters
    """

    # initiate seeds
    initial_seeds = initializeSeeds(m, k)
    print(initial_seeds)
    seeds = initial_seeds
    previous_seeds = seeds

    turn = 1
    while(True):
        distance = np.empty((m.shape[0], k))
        for i, seed in enumerate(seeds):
            distance[:, i] = np.sqrt(np.sum((m - seed) ** 2, axis=1))

        nearest_indexes = np.argmin(distance, axis=1)

        cores = []
        for i in range(k):
            cluster_indexes = nearest_indexes == i

            cluster = m[cluster_indexes, :]
            # print('cluster ', i, ' shape is: ', cluster.shape)
            new_core = np.sum(cluster, axis=0)/cluster.shape[0]
            # print('new core: ', new_core)
            cores.append(new_core)

        seeds = np.array(cores)
        seeds = np.floor(seeds)
        seeds = seeds[seeds[:,0].argsort()]

        print('turn: ', turn)
        turn = turn + 1
        print(seeds)

        if(np.array_equal(previous_seeds, seeds)):
            break

        previous_seeds = seeds


    return seeds


def initializeSeeds(m, k):
    counter = 0
    initial_seeds = np.empty((k, m.shape[1]))
    while(counter < k):
        random_seed_index = int(np.random.rand() * m.shape[0])
        random_seed = m[random_seed_index, :]
        if random_seed not in initial_seeds:
            initial_seeds[counter, :] = random_seed
            counter = counter + 1

    # random_seeds_indexes = np.random.rand(k)
    # random_seeds_indexes = [int(x * m.shape[0]) for x in random_seeds_indexes]
    # random_seeds_indexes.sort()
    # initial_seeds = m[random_seeds_indexes, :]
    return initial_seeds


def drawOutput(fp, color_matrix, block_size):
    k = color_matrix.shape[0]
    # not consider row for now
    size = block_size * k, block_size

    im = Image.new('RGBA', size)
    d = ImageDraw.Draw(im)
    for i, color in enumerate(color_matrix.tolist()):
        print(color)
        color = int(color[0]), int(color[1]), int(color[2])
        d.rectangle([i * block_size, 0, (i + 1) * block_size, (i + 1) * block_size], color)

    im.show()
    im.save(fp)

def main():
    print('main')
    inputFile = r'..\image\test.jpg'
    # get color matrix from a picture
    image_matrix = np.asarray(Image.open(inputFile))

    print(image_matrix.shape)

    # reshape to a m * 3 matrix
    image_matrix = image_matrix.reshape(image_matrix.shape[0] * image_matrix.shape[1] , 3)

    # kmeans to calculate k average color

    result = kmeans(image_matrix, 10)
    print(result)

    # draw k color to a result image
    drawOutput(r'..\result\new.png', result, 100)

if '__main__' == __name__:
    main()