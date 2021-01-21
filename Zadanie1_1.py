import numpy as np



def nominalResolution(file): 
    with open(file) as f:
        size = float(f.readline())
        #print(size)
        image = np.loadtxt(file, skiprows=2)
        px = np.max(np.sum(image,1))
        
        if px:
            return size/px
        else:
            return 0




for i in range(1,7):
    res = nominalResolution(f"figure{i}.txt")
    if (res):
        if (res%1):
            print(f'Номинальное разрешение изображения figure{i}: {str(round(res,2))} mm/px')
        else:
            print(f'Номинальное разрешение изображения figure{i}: {res} mm/px')            
    else:
        print(f"Номинальное разрешение изображения figure{i} не может быть вычисленно")
                  
