# image-mapper

A Python program that maps an image onto a 3D graph based on brightness levels (calculated using pixel luminance, 0.2126*R + 0.7152*G + 0.0722*B). Uses PIL and Pyplot. A higher z-value represents a lighter area of the image.

## Get started

Via command line, navigate into the directory containing the project. The syntax for running the mapper is:

### python mapper.py \<image> \<size> \[animation]

These are the arguments:
- \<image> is the name of the image you wish to map (including the extension)
- \<size> is the size of each tile that will be mapped. A smaller tile size will cause the program to run much slower
- \<animation> is an integer 0-4, 0 is default. 0 will allow the user to rotate the graph manually, 1 rotates the graph in a horizontal circle, 2 rotates the graph in a vertical circle, 3 shows the formation of the graph, 4 shows the formation of the graph and then rotates it in a horizontal circle  
