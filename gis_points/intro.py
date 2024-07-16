from manim import *

class EarthSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-65 * DEGREES)
        
        # Create a sphere
        sphere = Sphere(radius=2, resolution=(24, 24)).scale(1.75)
        
        # Apply texture to the sphere
        sphere.set_color(BLUE)

        # Add sphere to the scene
        self.add(sphere)
        
        # Rotate the sphere to make it more dynamic
        self.play(Rotate(sphere, angle=PI / 2, axis=UP), run_time=10, rate_func=linear)
        self.wait()


if __name__ == "__main__":
    scene = EarthSphere()
    scene.render()