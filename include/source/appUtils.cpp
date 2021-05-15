#include "header/appUtils.h"

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// -------------------------------------------
void framebuffer_size_callback(GLFWwindow *window, int width, int height)
{
    // make sure the viewport matches the new window dimensions;
    //note that width and height will be significantly larger than specified on retina displays
    glViewport(0, 0, width, height);
}

// process all input : query GLFW whether relevant keys are pressed/released this frame and react accordingly
// ----------------------------------
void processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}

// glfw: initialize and configure
//---------------------------
void init()
{
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif
}

// glfw window creation
// --------------------
bool createWindow(GLFWwindow *&window, unsigned int width, unsigned int height, const char *title)
{
    window = glfwCreateWindow(width, height, title, NULL, NULL);

    if (window == NULL)
    {
        return false;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    return true;
}