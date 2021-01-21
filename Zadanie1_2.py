import numpy as np

def offset(file1, file2):
    image1 = np.loadtxt(file1, skiprows=2)
    image2 = np.loadtxt(file2, skiprows=2)
    index1 = [i[0] for i in np.nonzero(image1)]
    index2 = [i[0] for i in np.nonzero(image2)]
    return index2[0]-index1[0], index2[1]-index1[1]


result = offset("img1.txt", "img2.txt")
print(f"Смещение по Y: {result[0]} px. По X: {result[1]} px.")
