from manim import *
from manim_slides import Slide

class Intro(Slide):
    def construct(self):
        self.camera.background_color = "#212121"
        title = Text("Free BSD vs. Pop_OS!").scale(2)
        center = Text("Free BSD vs. Pop_OS!").to_edge(UP)
        self.play(Write(title, run_time=2))

        self.next_slide()

        self.play(Transform(title, center))

        self.wait()

        self.next_slide()

        freeBSD = Text("Free BSD").scale(1.5).shift(LEFT*3).to_edge(UP)
        pop_OS = Text("Pop_OS!").scale(1.5).shift(RIGHT*3).to_edge(UP)

        # Create a white line
        line = Line(start=UP, end=DOWN, color=WHITE)
        
        # Set the position of the line to be in the middle of the screen
        line.move_to(ORIGIN)
        
        # Change the size of the line
        line.set_height(0.7 * config["frame_height"])
        
        # Add the line to the scene
        self.add(line)

        # Display the scene
        self.play(Create(line))

        self.play(FadeOut(center))
        self.play(Transform(center, freeBSD))
        self.play(ReplacementTransform(freeBSD, pop_OS))
