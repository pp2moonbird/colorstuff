from PIL import Image
import numpy as np


def main():
    print('main')
    inputFile = r'..\image\result.bmp'
    # get color matrix from a picture
    image_matrix = np.asarray(Image.open(inputFile))
    print(image_matrix)

    # reshape to a m * 3 matrix
    print(image_matrix.shape)
    image_matrix = image_matrix.reshape(100 * 500 , 3)
    print(image_matrix.shape)
    print(image_matrix)

    # kmeans to calculate k average color
    k = 5
    seeds = np.random.rand(5)

    seeds = [int(x * 50000) for x in seeds]
    seeds.sort()
    print(seeds)

    while(True):
        previous_seeds = seeds




        if(seeds == previous_seeds):
            break


    # draw k color to a result image

if '__main__' == __name__:
    main()