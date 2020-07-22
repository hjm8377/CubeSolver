# CubeSolver
CubeSolver is a program that that can learn you how to solve a cube written in python.
PyOpenCV was used for color recognition and OpenGL was used for 3D cube.   
Used Beginner's method and CFOP method to formulate a solving algorithm.


#### 3D Rubik's Cube of this Project was made by reference to [PyCube](https://github.com/mtking2/PyCube)

--------------------------------
## Environment

[Pycharm 2020.1](https://www.jetbrains.com/pycharm/)

[Python 3.7.7](https://www.python.org/)

[anaconda 4.8.2](https://www.anaconda.com)

--------------------------------

## Dependencies
This program utilizes the following Python modules:

[OpenCV-Python](https://github.com/opencv/opencv)

[PyOpenGL](https://github.com/mcfletch/pyopengl)

[Pygame](https://www.pygame.org/)

[NumPy](https://numpy.org/)

[itertools](https://pypi.org/project/more-itertools/)

Python 3.x:

```pip3 install opencv-python PyOpenGL PyOpenGL_accelerate pygame numpy ```

--------------------------------


## Solving Progress
### Color Detection
![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opencvcapture.png)
Cube color analyzing using OpenCV-Python

### Create Planar figure
![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opencvplanar.PNG)
Create Cube's planar figure to take a look the color is well recognized. (It's not the complete planar figure)

### 3D Cube 
![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opengl1.gif)   
3D cube that let you know how to solve Rubik's cube by press right arrow on your keyboard is show up.(3D cube is made with PyOpenGL and rendered by Pygame)   
The Program's name changes as you progress to show percentage of progress.

![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opengl2.gif)   
If you press left arrow on your keyboard, cube will show previous step.

