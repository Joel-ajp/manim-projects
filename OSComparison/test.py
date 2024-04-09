from manim import *
from manim_slides import Slide
import random

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

        bsdScoreTxt = Text("0").scale(3).shift(LEFT*3)
        popScoreTxt = Text("0").scale(3).shift(RIGHT*3)

        self.play(GrowFromCenter(bsdScoreTxt), GrowFromCenter(popScoreTxt), run_time=0.2)

        self.next_slide()

        bsdVal = 0
        popVal = 3
        for i in range(6):
            # Increment the value
            bsdVal += 1
            popVal += 1

            # Update the text to the new value
            bsdScoreTxt.set_text(str(bsdVal))
            popScoreTxt.set_text(str(popScoreTxt))

            # Animate the change in the number quickly
            self.play(Transform(bsdScoreTxt, Text(str(bsdVal)).scale(3).shift(LEFT*3)), Transform(popScoreTxt, Text(str(popVal)).scale(3).shift(RIGHT*3)), run_time=0.05)


        self.play(Transform(pop_OS, Text("Pop_OS!").set_color(GREEN).scale(2).shift(RIGHT*3).to_edge(UP)))

        self.next_slide()

        self.play(FadeOut(title), FadeOut(pop_OS), FadeOut(bsdScoreTxt), FadeOut(popScoreTxt), FadeOut(line))

        self.wait(1)

        installation = Text("Installation").scale(2)
        self.play(Write(installation)) 

        self.next_slide()
        installPop = Text("Installation | Pop_OS!").to_corner(UP + LEFT)
        self.play(Transform(installation, installPop))
        popInstallScreen = ImageMobject("popOs.png").scale(1.5)

        popInstallBullet = BulletedList(
            "Ease of Use",
            "Comes with all of the basics",
            "Quick Install!",
        ).shift(LEFT + UP * 0.75).scale(1.5)

        self.play(FadeIn(popInstallBullet))

        self.next_slide()

        # This is for the funnies
        self.play(FadeIn(popInstallScreen), run_time=0.5)
        self.next_slide()

        straightFace = ImageMobject("straight.png").scale(1.5)
        self.play(FadeIn(straightFace), run_time=3)

        self.next_slide()

        self.play(FadeOut(straightFace), FadeOut(popInstallScreen))

        self.next_slide()


        installBSD = Text("Installation | Free BSD").to_corner(UP + LEFT)

        self.remove(installPop)
        bsdInstallBullet = BulletedList(
            "Complete Customization",
            "You feel like you are doing work",
        ).shift(LEFT + UP * 0.75).scale(1.5)
        self.play(Transform(installation, installBSD), Transform(popInstallBullet, bsdInstallBullet))




# JP, basically, free bsd is the base for different desktop environments, while pop os is a desktop environment itself
# figure out what pop_os is based on, and which desktop environments are based on free bsd
# I installed xfce on free bsd and it was 