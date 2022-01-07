from manim import *
import numpy as np

"""
Video was succesfully compiled under the following OS/packages version.

Windows 11 64 bit (build 22000.376).

ffmpeg version 2021-12-30-git-12f21849e5-essentials_build-www.gyan.dev Copyright (c) 2000-2021 the FFmpeg developer built with gcc 11.2.0 (Rev5, Built by MSYS2 project).

Manim Community v0.13.1.

Python 3.9.9.

numPy 1.22.0.
"""

def get_treevector_str(t):
    return np.array2string(t, separator=',')

def get_tree(t, radius_scaling, color="#343434"):
    def get_location(l, div): return np.linspace(0, l*div, div+1)-l/2*div
    x_min = -6.2
    x_max = 6.2
    y_min = -4.5
    y_max = 2.8
    dot_radius = DEFAULT_DOT_RADIUS * radius_scaling
    deepest_depth_divisions = np.prod(t) - 1
    l0 = (x_max-x_min)/deepest_depth_divisions
    h0 = (y_max-y_min)/(len(t)+1)

    VTree = VGroup(*[VGroup() for i in range(len(t)+1)])
    current_y_divisions = len(t)
    current_y_locations = get_location(h0, current_y_divisions)
    VTree[0].add(Dot([0, current_y_locations[-1], 0],
                    radius=dot_radius,color=RED))  # Root Qubit
    for i in range(len(t)):
        current_x_divisions = np.prod(t[:i+1]) - 1
        if i == len(t)-1:
            factor = 1
        else:
            factor = np.prod(t[np.arange(-(len(t)-1)+i, 0)])
        current_x_locations = get_location(factor*l0, current_x_divisions)
        for x_location in current_x_locations:
            VTree[i+1].add(Dot([x_location,
                            current_y_locations[len(t)-1-i], 0], radius=dot_radius).set_color(color))
        parent_index = 0
        for c, dot in enumerate(VTree[i+1]):
            if i == 0:
                # we are at the zeroth level (i.e. at the root qubit)
                VTree.add(Line(dot.get_center(), VTree[i][0].get_center()).set_color(color))
            else:
                VTree.add(
                    Line(dot.get_center(), VTree[i][parent_index].get_center()).set_color(color))
                if (c+1) % t[i] == 0:
                    parent_index += 1
    return VTree

class TreeClusterStates(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        my_black = "#343434"
        radius_scaling = 2.2
        array_of_treevectors = np.array([
                                         np.array([2, 2]), 
                                         np.array([2, 4]), 
                                         np.array([2, 4, 2]), 
                                         np.array([4, 2, 2]),
                                         np.array([3, 3, 2]),
                                         np.array([2, 2, 2, 2]),
                                         np.array([3, 3, 2, 2])
                                         ], 
                                         dtype=object)

        my_titles = VGroup(
            Tex("\\underline{Qubit - Tree cluster states}").to_corner(UL)
        ).set_color(my_black)
        
        VTrees = [get_tree(t, radius_scaling, color=my_black) for t in array_of_treevectors]

        def treevector_display(t): return Tex("$\\Vec{t}="+get_treevector_str(t)+"$")

        treevector_Tex = [treevector_display(t).set_color(my_black).to_corner(UR) for t in array_of_treevectors]


        self.add(my_titles[0])
        self.play(
            Write(VTrees[0]),
            Write(treevector_Tex[0])
        )
        for i in range(1, len(array_of_treevectors)):
            self.wait(1.8)
            self.play(
                TransformMatchingShapes(
                    VTrees[i-1], VTrees[i], transform_mismatches=True),
                TransformMatchingTex(
                    treevector_Tex[i-1], treevector_Tex[i], transform_mismatches=True),
                run_time=0.5
            )
        self.wait()
        self.play(
            FadeOut(my_titles[0]),
            FadeOut(VTrees[-1]),
            FadeOut(treevector_Tex[-1])
        )
        self.wait()

