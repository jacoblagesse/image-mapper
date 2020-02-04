from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
from matplotlib.colors import ListedColormap
import PyQt5
matplotlib.use('Qt4Agg')

import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import sys

class ImageMap():

    def __init__(self, name, size, animation):
        self.name = name
        self.size = size
        self.animation = animation

    def map_image(self):
        size = self.size
        animation = self.animation

        fig = plt.figure()

        img = Image.open(self.name)
        width, height = img.size
        pix = img.load()
        imgplot = plt.imshow(img)

        X = []
        Y = []
        Z = []

        print(width, height)
        
        if width>height:
            print("Method 1")
            x = 0;
            while(x < img.width):
                y = 0;
                while(y < img.height):
                    X.append(x)
                    Y.append(img.height-y)
                    Z.append(1*(0.2126*pix[x,y][0]+0.7152*pix[x,y][1]+0.0722*pix[x,y][1]))
                    y += size
                x += size
        else:
            print("Method 2")
            y = 0;
            while(y < img.height):
                x = 0;
                while(x < img.width):
                    X.insert(0,x)
                    Y.append(y)
                    Z.append(1*(0.2126*pix[x,y][0]+0.7152*pix[x,y][1]+0.0722*pix[x,y][1]))
                    x += size
                y += size



        Z = np.array(Z)
        '''for item in Z:
            print(item)'''
        ax = fig.add_subplot(111, projection='3d')

        oranges = cm.get_cmap('Greys', 256)
        newcolors = oranges(np.linspace(0, 1, 256))
        whites = np.array([0, 0, 0, 0])
        newcolors[:2, :] = whites
        newcmp = ListedColormap(newcolors)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.axis('off')
        ax.plot_trisurf(X,Y,Z, linewidth=0.2, cmap=newcmp)
        
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(18.5, 10.5)
        fig.savefig('test2png.png', dpi=100)

        ax.set_zlim(0, 300)

        if animation == 0:
            ax.view_init(elev=75,azim=90)
            plt.show()
        elif animation == 1:
            for angle in range(0,180):
                ax.view_init(elev=75,azim=angle*2)
                plt.draw()
                plt.pause(0.001)
        elif animation == 2:
            for angle in range(0,90):
                ax.view_init(elev=angle*4,azim=270)
                plt.draw()
                plt.pause(0.001)
        elif animation == 3:
            for zvalue in range(0,4):
                ax.view_init(elev=60,azim=270)
                ax.set_zlim(0, 1000-zvalue*250)
                plt.draw()
                plt.pause(0.5)
            plt.show()
        elif animation == 4:
            ax.set_zlim(0, 2000)
            ax.view_init(elev=90,azim=270)
            plt.pause(1)
            for angle in range(0,6):
                ax.view_init(elev=90-angle*10,azim=270)
                plt.draw()
                plt.pause(0.01)
            plt.pause(1)
            for zvalue in range(0,9):
                ax.view_init(elev=30,azim=270)
                ax.set_zlim(0, 1000-zvalue*65)
                plt.draw()
                plt.pause(0.01)
            plt.pause(1)
            for angle in range(0,180):
                ax.view_init(elev=30,azim=270+angle*2)
                plt.draw()
                plt.pause(0.01)
            plt.pause(1)
            for angle in range(0,6):
                ax.view_init(elev=30+angle*10,azim=270)
                plt.draw()
                plt.pause(0.01)
            plt.pause(1)

        
def main():
    if len(sys.argv) < 3:
        print("Syntax: mapper.py <image name> <size of tile (larger will run faster)> <animation mode (0-4, default is 0)>")
    elif len(sys.argv) < 4:
        image = ImageMap(sys.argv[1], int(sys.argv[2]), 0)
        image.map_image()
    else:
        image = ImageMap(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
        image.map_image()

main()
