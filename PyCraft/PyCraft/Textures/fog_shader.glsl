#vertex shader
#version 140
uniform mat4 p3d_ModelViewProjectionMatrix;

in vec4 p3d_Vertex;
in vec4 p3d_Color;
in vec2 p3d_MultiTexCoord0;

out vec4 color;
out vec2 uv;

void main() {
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
    color = p3d_Color;
    uv = p3d_MultiTexCoord0;
}

#fragment shader
#version 140
uniform vec4 fog_color;
uniform float fog_density;
uniform float fog_distance;

in vec4 color;
in vec2 uv;

out vec4 fragColor;

void main() {
    float distance = gl_FragCoord.z / gl_FragCoord.w;
    float fog_factor = exp(-pow((distance / fog_distance) * fog_density, 2.0));
    fog_factor = clamp(fog_factor, 0.0, 1.0);
    vec4 fogged_color = mix(fog_color, color, fog_factor);
    fragColor = fogged_color;
}
