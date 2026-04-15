"""
Module for creating animations using manim to highlight the geometric
properties of the octonions.
"""

import sys
sys.path.insert(0, 'octonions')
from manim import *
import octonions.factoring as factoring
import octonions.cayley_integers as ci
import octonions.algebra as alg
import numpy as np

class MultiplicationDemonstration(MovingCameraScene):
    """
    Displays the non-associative nature of octonion multiplication.
    Strategy:
    1. Pick three starter octonions and label them by their components.
    2. Show multiplying just two of them both ways to show non-commutativity.
    3. Show multiplying all three, and then show the two different ways.
    Pick and example where results are vastly different.
    Plot each point onto the Coxeter plane.
    Color code everything effectively to show the differences.
    """
    def construct(self):
            self.wait(2)
            # Generate the 3 octonions and make their labels.
            oct1, oct2, oct3, dot1, dot2, dot3 = self.pick_octonions()
            oct1_text = Text(f"Octonion 1: {oct1.components[0]}, {oct1.components[1]}, {oct1.components[2]}, {oct1.components[3]}, {oct1.components[4]}, {oct1.components[5]}, {oct1.components[6]}, {oct1.components[7]}", color=RED, font_size=20).next_to(dot1, UP)
            oct2_text = Text(f"Octonion 2: {oct2.components[0]}, {oct2.components[1]}, {oct2.components[2]}, {oct2.components[3]}, {oct2.components[4]}, {oct2.components[5]}, {oct2.components[6]}, {oct2.components[7]}", color=GREEN, font_size=20).next_to(dot2, UP)
            oct3_text = Text(f"Octonion 3: {oct3.components[0]}, {oct3.components[1]}, {oct3.components[2]}, {oct3.components[3]}, {oct3.components[4]}, {oct3.components[5]}, {oct3.components[6]}, {oct3.components[7]}", color=BLUE, font_size=20).next_to(dot3, UP)
            self.camera.frame.set_width(20)

            # Provide an origin for reference.
            center = Dot(point=[0, 0, 0], radius=0.1, color=WHITE)
            origin_text = Text("Origin", color=WHITE, font_size = 24).next_to(center)

            # Add everything to the scene.
            self.play(FadeIn(center), FadeIn(origin_text), run_time=2)
            self.play(FadeIn(oct1_text), FadeIn(dot1), run_time=2)
            self.play(FadeIn(oct2_text), FadeIn(dot2), run_time=2)
            self.play(FadeIn(oct3_text), FadeIn(dot3), run_time=2)
            self.play(FadeOut(origin_text), run_time=2)

            # Highlight dot 1 and dot 3
            mult_label1 = Text("Oct 1 * Oct 3", color=WHITE, font_size=20).to_corner(UP)
            highlight1 = Circle(radius=0.1, color=YELLOW,stroke_width=3).move_to(dot1.get_center())
            highlight3 = Circle(radius=0.1, color=YELLOW,stroke_width=3).move_to(dot3.get_center())
            self.play(FadeIn(highlight1), FadeIn(highlight3), FadeIn(mult_label1), run_time=2)
            self.wait(2)

            # Show the result
            result1 = oct1 * oct3
            result1_dot = Dot(point=[project_to_coxeter_plane(result1)[0], project_to_coxeter_plane(result1)[1], 0], radius=0.1, color=PURPLE)
            result1_text = Text(f"{result1.components[0]}, {result1.components[1]}, {result1.components[2]}, {result1.components[3]}, {result1.components[4]}, {result1.components[5]}, {result1.components[6]}, {result1.components[7]}", color=WHITE, font_size=20).next_to(result1_dot, DOWN)
            self.play(self.camera.frame.animate.set_width(20).move_to(result1_dot.get_center()), run_time=2)
            result1_highlight = Circle(radius=0.1, color=YELLOW,stroke_width=3).move_to(result1_dot.get_center())
            self.play(FadeIn(result1_text), FadeIn(result1_dot), FadeIn(result1_highlight), mult_label1.animate.next_to(result1_dot, UP), run_time=2)
            self.wait(2)

            # Now show the other way of multiplying and the result.
            result2 = oct3 * oct1
            result2_dot = Dot(point=[project_to_coxeter_plane(result2)[0], project_to_coxeter_plane(result2)[1], 0], radius=0.1, color=PURPLE)
            mult_label2 = Text("Oct 3 * Oct 1", color=WHITE, font_size=20).to_corner(UP)
            result2_highlight = Circle(radius=0.1, color=YELLOW,stroke_width=3).move_to(result2_dot.get_center())
            result2_text = Text(f"{result2.components[0]}, {result2.components[1]}, {result2.components[2]}, {result2.components[3]}, {result2.components[4]}, {result2.components[5]}, {result2.components[6]}, {result2.components[7]}", color=WHITE, font_size=20).next_to(result2_dot, DOWN)
            self.play(FadeIn(mult_label2), run_time=2)
            self.play(FadeIn(result2_dot), FadeIn(result2_highlight), FadeIn(result2_text), mult_label2.animate.next_to(result2_dot, UP), run_time=3)
            self.play(FadeOut(highlight1), FadeOut(highlight3), run_time=2)

            # Now show the two different ways of multiplying all three octonions.
            result3 = oct1 * (oct2 * oct3)
            result4 = (oct1 * oct2) * oct3
            result3_dot = Dot(point=[project_to_coxeter_plane(result3)[0], project_to_coxeter_plane(result3)[1], 0], radius=0.1, color=ORANGE)
            result4_dot = Dot(point=[project_to_coxeter_plane(result4)[0], project_to_coxeter_plane(result4)[1], 0], radius=0.1, color=ORANGE)
            result3_text = Text(f"{result3.components[0]}, {result3.components[1]}, {result3.components[2]}, {result3.components[3]}, {result3.components[4]}, {result3.components[5]}, {result3.components[6]}, {result3.components[7]}", color=WHITE, font_size=20).next_to(result3_dot, DOWN)
            result4_text = Text(f"{result4.components[0]}, {result4.components[1]}, {result4.components[2]}, {result4.components[3]}, {result4.components[4]}, {result4.components[5]}, {result4.components[6]}, {result4.components[7]}", color=WHITE, font_size=20).next_to(result4_dot, DOWN)
            mult_label3 = Text("Oct 1 * (Oct 2 * Oct 3)", color=WHITE, font_size=20).to_corner(UL)
            mult_label4 = Text("(Oct 1 * Oct 2) * Oct 3", color=WHITE, font_size=20).to_corner(UR)
            self.play(FadeIn(mult_label3), FadeIn(mult_label4), run_time=2)
            self.play(mult_label3.animate.next_to(result3_dot, UP), mult_label4.animate.next_to(result4_dot, UP), self.camera.frame.animate.move_to(result3_dot.get_center()), FadeIn(result3_dot), FadeIn(result3_text), FadeIn(result4_dot), FadeIn(result4_text), run_time=2)
            self.play(self.camera.frame.animate.set_width(28), run_time=2)
            self.wait(5)




    def pick_octonions(self):
        """
        Picks three octonions and turns them into manim objects.
        Can be any, so these three just represent a sample.
        """
        oct1 = factoring.generate_primitive_octonion(2)
        oct2 = factoring.generate_primitive_octonion(7)
        oct3 = factoring.generate_primitive_octonion(15)
        dot1 = Dot(point=[project_to_coxeter_plane(oct1)[0], project_to_coxeter_plane(oct1)[1], 0], radius=0.1, color=RED)
        dot2 = Dot(point=[project_to_coxeter_plane(oct2)[0], project_to_coxeter_plane(oct2)[1], 0], radius=0.1, color=GREEN)
        dot3 = Dot(point=[project_to_coxeter_plane(oct3)[0], project_to_coxeter_plane(oct3)[1], 0], radius=0.1, color=BLUE)
        return oct1, oct2, oct3, dot1, dot2, dot3

class RehmAnimation(MovingCameraScene):
    """
    Constructs a scence of Rehm's Algorithm for factoring octonions.
    """
    def construct(self):
        """
        Constructs the Rehm's Algorithm scene.
        """
        self.wait(2)
        self.camera.frame.set_width(16)
        origin_text = Text("Origin", color=WHITE, font_size = 24).to_corner(UP)
        center = Dot(point=[0, 0, 0], radius=0.05, color=WHITE)
        self.play(FadeIn(center), FadeIn(origin_text), run_time=3)
        primitive_dot, primitive_octonion = self.pick_primitive_octavian_integer()
        primitive_text = Text("Primitive Octavian Integer", color=YELLOW, font_size=24).next_to(primitive_dot, DOWN)
        self.play(FadeIn(primitive_dot), FadeIn(primitive_text), run_time=3)
        self.wait(1)

        # Zoom all the way in on the primitive octavian integer.
        self.play(self.camera.frame.animate.scale(0.01).move_to(primitive_dot.get_center()), run_time=3)
        self.wait(1)
        self.remove(primitive_text, origin_text)

        # Add a yellow background while zoomed in
        self.camera.background_color = YELLOW

        # Build the factor sets while zoomed in.
        left_dots, right_dots = self.make_factor_dots(primitive_octonion)

        # Make text labels for the factor dots
        left_text = Text("Left Divisors", color=BLUE).to_corner(UL).shift(UP*0.3)
        right_text = Text("Right Divisors", color=RED).to_corner(UR).shift(UP*0.3)
        
        # Zoom back out and reveal the divisors over the yellow background
        self.play(self.camera.frame.animate.set_width(16).move_to([0, 0, 0]), run_time=2)
        self.play(FadeIn(left_dots), FadeIn(left_text), run_time=6)
        self.play(FadeIn(right_dots), FadeIn(right_text), run_time=6)
        
        # Isolate the groups and delete the origin to show the geometric structure of each.
        self.play(left_dots.animate.shift(LEFT*4.5), right_dots.animate.shift(RIGHT*4.5), FadeOut(center), run_time=3)
        self.wait(8)

    def pick_primitive_octavian_integer(self):
        """
        Picks a primitive octavian integer to factor.
        """
        # Generate an octonion with norm 50.
        primitive_octonion = factoring.generate_primitive_octonion(20)
        # Project it onto the Coxeter plane and display it as a dot.
        x, y = project_to_coxeter_plane(primitive_octonion)
        dot = Dot(point=[x, y, 0], radius=0.1, color=YELLOW)
        return dot, primitive_octonion
    
    def make_factor_dots(self, primitive_octonion):
        """
        Uses Rehm's Algorithm to build 240 left hand divisor and 240 right hand divisor sets,
        then projects them to the Coxeter plane and converts them to manim dots.
        """
        left_divisors, right_divisors = factoring.factor_octonion(primitive_octonion)
        left_dots = VGroup(*[
            Dot(point=[project_to_coxeter_plane(o)[0], project_to_coxeter_plane(o)[1], 0], radius=0.05, color=BLUE)
            for o in left_divisors
        ])
        right_dots = VGroup(*[
            Dot(point=[project_to_coxeter_plane(o)[0], project_to_coxeter_plane(o)[1], 0], radius=0.05, color=RED)
            for o in right_divisors
        ])
        return left_dots, right_dots
    

class CayleyPlotting(Scene):
    """
    Constructs a scene of the 240 unit cayley integers being projected onto the 2D Coxeter plane.
    """
    def construct(self):
        """
        Constructs the scene.
        """
        self.wait(2)
        tups, projected, scale = self.make_scene()
        lines = self.make_lines(tups, projected, scale)
        dots = self.make_dots(projected, scale)
        self.play(FadeIn(lines), run_time=2)
        self.play(FadeIn(dots), run_time=2)
        self.wait(5)

    def make_scene(self, scale=4.5):
        """
        Collect all the data to construct the scene.
        """
        cayley_integers = [ci.oct_int(1, k) for k in range(1, 241)
                           if ci.oct_int(1, k) is not None]
        tups = [np.array(factoring.oct_to_e8(o)) for o in cayley_integers]
        projected = [project_to_coxeter_plane(o) for o in cayley_integers]
        return tups, projected, scale

    def make_dots(self, projected, scale):
        """
        Takes in the points and converts them to manim dots.
        Color codes by by the rings of the e8 lattice.
        """
        # Calculate euclidian distance from the center, round, and store.
        distances = [np.sqrt(x**2 + y**2) for x,y in projected]
        rounded = [round(d, 1) for d in distances]
        unique_dists = sorted(set(rounded))

        # Map the colors to all the unique distances to create a gradient effect.
        colors = color_gradient([PINK, RED, YELLOW,GREEN, BLUE, PURPLE], len(unique_dists))
        color_map = {d: colors[i] for i, d in enumerate(unique_dists)}
        return VGroup(*[
        Dot(point=[x*scale, y*scale, 0], radius=0.05,
            color=color_map[round(np.sqrt(x**2+y**2), 1)])
        for x, y in projected
        ])
    
    def make_lines(self, tups, projected, scale):
        """
        Makes lines between the points that are a distance of 1 apart in the e8 lattice.
        """
        # Compare each pair and check to see if their dot product is ~1.
        lines = VGroup()
        for i in range(len(tups)):
            for j in range(i+1, len(tups)):
                if abs(np.dot(tups[i], tups[j]) -1) < 0.01:
                    # If distance = 1, connect them with a line.
                    x1, y1 = projected[i]
                    x2, y2 = projected[j]
                    lines.add(Line(
                        start=[x1*scale, y1*scale, 0],
                        end=[x2*scale, y2*scale, 0],
                        color=GREY,
                        stroke_width=0.5
                    ))
        return lines


# Module level hepler functions for the animations.

def compute_points():
        """
        Holds the logic for where the 240 cayley integers lie in the Coxeter plane.
        Returns the list of points to be plotted.
        """
        # The simple roots of the coxeter plane, used to project the octonions to 2D.
        simple_roots = np.array([
        [ 1,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 1,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 1,-1, 0, 0, 0, 0],
        [ 0, 0, 0, 1,-1, 0, 0, 0],
        [ 0, 0, 0, 0, 1,-1, 0, 0],
        [ 0, 0, 0, 0, 0, 1, 1, 0],
        [-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5],
        [ 0, 0, 0, 0, 0, 1,-1, 0],
        ])

        # Build the reflection matrices using the simple roots and identity matrix and find Coxeter Element.
        # Coxeter Element = product of all simple relections, so C ends up as the coxeter element after all iterations.
        # C is an 8x8 matrix that, when applied, performs all simple relections to an octavian integer.
        I = np.eye(8)
        C = I.copy()
        for i in simple_roots:
            R = I - np.outer(i,i)
            C = R @ C
        
        # Eigenvalue of C for smallest exponent is e^(2pi i / 30).
        eigenvalues, eigenvectors = np.linalg.eig(C)
        # We want to find the eigenvector closest to e^(2pi i / 30)   (j is the imaginary unit)
        target = np.exp(2j * np.pi / 30)
        index = np.argmin(np.abs(eigenvalues - target))
        # Once we find the target, grab the corresponding eigenvector, which is 1 of 8 columns in eigenvectors.
        v = eigenvectors[:, index]

        # Extract the real and imaginary parts of the eigenvector, used for projection.
        v1 = v.real
        v2 = v.imag
        return v1, v2

def project_to_coxeter_plane(oct):
    """
    Projects a given octonion to the 2D Coxeter plane.
    """
    # Use compute points to get the two necessary vectors for projection.
    v1, v2 = compute_points()
    # For projection, convert the octonion to the e8 space.
    tup = np.array(factoring.oct_to_e8(oct))
    # Return (x,y) cooridinates of the octonion on the Coxeter Plane by taking the dot product of real and imaginary.
    return float(tup @ v1), float(tup @ v2)