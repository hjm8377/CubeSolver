[English](https://github.com/hjm8377/CubeSolver/blob/master/README.en.md) 👈

# CubeSolver
CubeSolver는 큐브를 어떻게 맞추는지 알려주는 프로그램입니다. 
파이썬으로 작성되었고, 색 인식에 pyopencv가, 3D큐브 구현에 OpenGL이 사용되었습니다.
큐브 공식은 초보공식과 CFOP공식을 혼용했습니다.


<!--#### 3D Rubik's Cube of this Project was made by reference to [PyCube](https://github.com/mtking2/PyCube)
-->

[Project Video (youtube) ](https://www.youtube.com/watch?v=KLb918FLVjU)

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
OpenCV-Python을 이용하여 큐브 색 인식

### Create Planar figure
![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opencvplanar.PNG)
색이 잘 인식 되었는지 확인하기 위해 큐브의 전개도 만들기(잘 정리된 전개도는 아님)

### 3D Cube 
![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opengl1.gif)  
오른쪽 방향키를 누르면 3D 큐브가 큐브 맞추는 방법을 알려줍니다. (3D 큐브는 PyOpenGL로 만들어졌고, Pygame으로 렌더링 되었습니다)
프로그램이름이 바뀌면서 진행 정도를 보여줍니다.

![Alt text](https://github.com/hjm8377/CubeSolver/blob/master/resource/opengl2.gif)   
왼쪽 방향키를 누르면 큐브는 이전 단계를 보여줍니다.
