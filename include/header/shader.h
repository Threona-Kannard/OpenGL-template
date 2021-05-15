#ifndef SHADER_H_
#define SHADER_H_

#include <glad/glad.h>
#include <glm/glm/glm.hpp>

#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;
using namespace glm;

class Shader
{
public:
    unsigned int ID;

    // constructor generates the shader on the fly
    // ----------------------------------------------
    Shader(const char *vertexPath, const char *fragmentPath, const char *geometryPath);

    // destructor of the shader program
    // ----------------------------------------------
    ~Shader();

    // active the shader
    // ----------------------------------------------
    void use();

#pragma region utility uniform functions
    //------------------------------------------------
    void setBool(const string &name, bool value) const;
    //------------------------
    void setInt(const string &name, int value) const;
    //------------------------
    void setFloat(const string &name, float value) const;
    //------------------------
    void setVec2(const string &name, const vec2 &value) const;
    void setVec2(const string &name, float x, float y) const;
    //------------------------
    void setVec3(const string &name, const vec3 &value) const;
    void setVec3(const string &name, float x, float y, float z) const;
    //------------------------
    void setVec4(const string &name, const vec4 &value) const;
    void setVec4(const string &name, float x, float y, float z, float w) const;
    //------------------------
    void setMat2(const string &name, const mat2 &mat) const;
    //------------------------
    void setMat3(const string &name, const mat3 &mat) const;
    //------------------------
    void setMat4(const string &name, const mat4 &mat) const;
#pragma endregion

private:
    // ultility function for checking shader compilation/linking errors.
    void checkCompileErrors(GLuint shader, string type);
};

#endif