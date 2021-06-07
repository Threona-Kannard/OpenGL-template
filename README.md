# OpenGL Visual Studio Code template

#### This is a template project for OpenGL with debug config on Visual Studio Code

> This template supports:
>
> * OpenGL 4.6 or below
> * OpenGL ES 3.2 or below
> * OpenGL SC 2.0 or below

#### The advantages of this template

**1. A cross-platform template**

​	With this template, you can continue your OpenGL project on any computer without the attention to the Operating System being used. It can run smoothly on Windows, Linux, and macOS with only one time to configure it.

**2. Easy to configure your project**

​	In Visual Studio, you need to do a lot of steps to configure an OpenGL project (You can see the tutorial <a href="http://www.mcihanozer.com/tips/setting-up-libraries/setting-up-glfw-for-visual-studio/">here</a>). To configure your build, you need to do a lot of steps on the Visual Studio GUI. But with this template, you just configure only one file (tasks.json).

**3. Faster than Visual Studio**

​	Due to downloading a lot of redundant extensions and libraries for C/C++, the Visual Studio takes up a lot of hard drive space. 

​	This template just requires you have a C/C++ compiler to build and run. 

**4. Add external libs easier by one step**

​	You just add the link to download the external library (git or url) to `external.json` then run the Python script `getExternal.py`

<h2><b>Tutorial</b></h2>



<h3 style="text-align:left"><b>A. Prerequisite</b></h3>

<h4>I. C/C++ extension on Visual Code</h4>

Firstly, please ensure that your Visual Studio Code had been installed `C/C++ extension`. Following the instruction below if you haven't installed it.

1. Open VS Code and choose <b>Extension</b> on the side menu.

   ![Extension](https://user-images.githubusercontent.com/66297538/118797279-9f43fb00-b8c6-11eb-89d8-6fa0865bebc0.png)
   
2. Search the name "C/C++" and download the first one.

   ![C++ Extension](https://user-images.githubusercontent.com/66297538/118797363-b682e880-b8c6-11eb-8d2a-cf556c2a0ca8.png)

   <b><u>Note:</u></b> Visual Studio Code provides a lot of extensions to make your coding more comfortable. See them  <a href="https://blog.logrocket.com/top-10-vs-code-extensions-2021/#importcost">here</a>.

<h4> II. C++ Compiler</h4>

Next, you must download a C++ compiler to build and debug on Visual Studio Code.

1. **Windows**

 There are a lot of tools and software that provide the C/C++ compiler for Windows like MinGW, Cygwin, ... But in this tutorial, I will use the MinGW x64 (download <a href="https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/" target="_blank">here</a>):

![MinGW download](https://user-images.githubusercontent.com/66297538/118797421-c4d10480-b8c6-11eb-9a1c-28b22cfdf435.png)
![image](https://user-images.githubusercontent.com/66297538/120953780-f592b400-c777-11eb-99ec-952065180966.png)


After that you need to create an enviroment variable for MinGW by following the steps below:
   - Step 1: Find the `env` in the window search bar.
   
   ![image](https://user-images.githubusercontent.com/66297538/120768256-24c1df00-c546-11eb-841c-b3e8d504fb0c.png)
   - Step 2: Choose the `Environment Variables` button.

   ![image](https://user-images.githubusercontent.com/66297538/120768431-58046e00-c546-11eb-813e-043163b11612.png)
   - Step 3: Click the `New` button like the image.

   ![image](https://user-images.githubusercontent.com/66297538/120768587-83875880-c546-11eb-970a-633766cdfdf7.png)
   - Step 4: Fill the information like the image then click `OK` and the `Environment` window.

   ![image](https://user-images.githubusercontent.com/66297538/120768738-aade2580-c546-11eb-9d77-96b2d900542c.png)


2. **Linux**

   The GCC has already been installed in Linux. Open the `terminal window` and check its version by entering the following command:

   > gcc -v

   If GCC isn't installed, run the following command from the `terminal window` to Update the Linux package lists. An out-of-date Linux distribution can sometimes interfere with attempts to install new packages.

   > sudo apt-get update

   Next install the GNU compiler tools and the GDB debugger with this command:

   > sudo apt-get install build-essential gdb

3. **macOS**

   Clang may already be installed on your Mac. To verify that it is, open a macOS `terminal window` and enter the following command:

   > clang --version

   If Clang isn't installed, enter the following command to install the command line developer tools:

   > xcode-select --install

<h4>III. Add your shader path</h4>


You need to enter the path of your shader source into `Main.cpp`

![Shader source path](https://user-images.githubusercontent.com/66297538/118797645-03ff5580-b8c7-11eb-8149-0b49f9331330.png)

<u>Example:</u> `{path of your disk}/OpenGL-template/src`

<h4>IV. Add the necessary libraries</h4>

Open file `external.json` to add the libraries you want to import into the project with the format:

- "repo_name" : "{your library name}"
- "repo_url" : "{your library download link}"
- "clone_location" : "{your location you want place it in}"

Then run the `getExternal.py` to clone all the libraries you need.

**<u>Note</u>**: The `getExternal.py` just can download the libraries which have repository on git. To download specific file libraries (dll, other cpp files) will be update later.

<h3 style="text-align:left"><b>B. Build and Debug</b></h3>

1. **Build**

   There are two ways to build:

   - Press `F5` to build and run the program.
   - Press `Ctrl+Shift+B` to build only.

2. **Debug**

You just do the same with Visual Studio.

I. Create your breakpoint in two ways :

1. Click on the red circle on the left of the row number.

![Place breakpoint](https://user-images.githubusercontent.com/66297538/118797730-14afcb80-b8c7-11eb-89fe-99d4405dbc4d.png)


2. Choose the row you want to place the breakpoint and press `F9` 

II. Build and run the program by press `F5`

III. Let's debug

* `F6` : Pause
* `F10` : Step Over
* `F11` : Step Into
* `Shift + F11` : Step Out
* `Ctrl + Shift + F5` : Restart
* `Shift + F5` : Stop

Visual Studio Code not only provides us an area to visualize the `variables` , `stack`, `breakpoint` but also they have a `Debug Console` for us.

![Debug](https://user-images.githubusercontent.com/66297538/118797799-209b8d80-b8c7-11eb-8e5b-f58356a878e9.png)




## Thank you for reading this document

<h4 style="text-align:center; font-family:time New Roman">
    <div><b><u>Contact me</u></b></div>
    <div>Tan Phat Huynh</div>
    <div>phattanhuynh1324@gmail.com</div></h4>
