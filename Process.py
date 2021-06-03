import cv2
import numpy as np
from sklearn.cluster import *


def make_pixel(img, maxSize=80, BlackAndWhite=False):
    w = img.shape[1]
    h = img.shape[0]

    newW = maxSize if w >= h else (w * maxSize) // h
    newH = maxSize if h >= w else (h * maxSize) // w
    newImg = img
    if BlackAndWhite:
        print("Converting to black and white...")
        newImg = cv2.cvtColor(cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    if newImg.shape[2] == 4:
        newImg = np.delete(newImg, 3, axis=0)
    print("Resizing to ({},{})...".format(newW, newH))
    newImg = cv2.resize(newImg, dsize=(newW, newH), interpolation=cv2.INTER_AREA)
    return newImg


def getColors(img, n=1):
    w = img.shape[1]
    h = img.shape[0]
    clrs = [img[i // w, i % w] for i in range(w * h)]
    clrs = np.array(clrs)
    if not (type(n) == int) or n == 0:
        print("Using best value of n from 1 to 10...")
        res = []
        for k in range(11):
            kmeans = KMeans(n_clusters=k + 1).fit(clrs)
            similarity = 0

            for c1 in kmeans.cluster_centers_:
                for c2 in kmeans.cluster_centers_:
                    c1 = tuple(c1)
                    c2 = tuple(c2)
                    if not (c1 == c2):
                        similarity += 10000 * int(max([abs(c1[i] - c2[i]) for i in range(3)]) <= 50)
            res.append((kmeans.score(clrs) - similarity) * (k + 1))

        n = res.index(max(res))
        print("Best value is " + str(n))
    kmeans = KMeans(n_clusters=n + 1).fit(clrs)
    clusterNumbers = list(kmeans.labels_)
    colors = list(map(tuple, list(kmeans.cluster_centers_)))
    colors = list(map(lambda t: tuple(map(int, t)), colors))

    if n == 1:
        colors = [(0, 0, 0), (255, 255, 255)] if colors[0][0] < colors[1][0] else [(255, 255, 255), (0, 0, 0)]
    return (clusterNumbers, colors)


def newColors(img, n=1):
    clusterNumbers, colors = getColors(img, n)
    w = img.shape[1]
    h = img.shape[0]

    assert not (type(n) == int) or n == 0 or len(colors) == n + 1, "There are " + str(
        len(colors)) + " but I wanted " + str(n + 1) + "..."

    newImg = [colors[k] for k in clusterNumbers]
    newImg = np.array(newImg)
    newImg = newImg.reshape(h, w, len(colors[0])).astype("float32")

    return newImg
