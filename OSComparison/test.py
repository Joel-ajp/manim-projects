from manim import *
from manim_slides import Slide

class Intro(Slide):
    def construct(self):
        self.camera.background_color = "#212121"
        title = Text("Free BSD vs. Pop_OS!").scale(2)
        upCenter = Text("Free BSD vs. Pop_OS!").to_edge(UP)
        self.play(Write(title, run_time=2))

        self.next_slide()

        self.play(Transform(title, upCenter))

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

        self.play(Transform(title, freeBSD))
        self.play(ReplacementTransform(freeBSD, pop_OS))

        bsdPoints = VGroup(
            Tex(
                """{itemize}
                    \item Free BSD is a free and open-source Unix-like operating system descended from the Berkeley Software Distribution (BSD), which was based on Research Unix.
                    \item It is used in server environments.
                    \item It is known for its performance, reliability, and advanced networking and security features.
                    \item Free BSD is used in desktop environments as well. 
                """
            )
        )

        popPoints = VGroup(
            """{itemize}
                \item Pop!_OS is a Linux distribution based on Ubuntu, which is based on Debian.
                \item It is developed by System76, a company that manufactures and sells Linux laptops and desktops.
                \item Pop!_OS is known for its focus on simplicity and ease of use.
                \item It is used in desktop environments.
            """
        )

        self.play(FadeIn(bsdPoints))
        self.play(FadeIn(popPoints))




# JP, basically, free bsd is the base for different desktop environments, while pop os is a desktop environment itself
# figure out what pop_os is based on, and which desktop environments are based on free bsd
# I installed xfce on free bsd and it was 