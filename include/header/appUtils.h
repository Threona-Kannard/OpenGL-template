#ifndef APP_UTILS_H_
#define APP_UTILS_H_

#include <glad/glad.h>
#include <GLFW/glfw3.h>

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// -------------------------------------------
void framebuffer_size_callback(GLFWwindow *window, int width, int height);

// process all input : query GLFW whether relevant keys are pressed/released this frame and react accordingly
// ----------------------------------
void processInput(GLFWwindow *window);

// glfw: initialize and configure
//---------------------------
void init();

// glfw window creation
// --------------------
bool createWindow(GLFWwindow *&window, unsigned int width, unsigned int height, const char *title);

#endif