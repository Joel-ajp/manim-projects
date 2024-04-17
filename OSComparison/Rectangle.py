from manim import *
from manim_slides import Slide
import random

class Test(Slide):
    def construct(self):
        self.camera.background_color = "#212121"

        perf = Text("Performance Comparison (I/O Specific)").scale(1)
        self.play(Write(perf)) 
        self.next_slide()        

        project = Text("Benchmark Details").to_corner(UP)

        self.play(Transform(perf, project))

        # Create a rectangle
        rectangle = Rectangle(width=3, height=2, color=RED)
        rectangle.rotate(PI/2).shift(LEFT * 4.5)

        # Create text
        text = Text("words.txt").scale(0.5)
        text.move_to(rectangle)

        # Group rectangle and text
        group = VGroup(rectangle, text)


        linkedList = Rectangle(width=3, height=1, color=BLUE)
        linkedListText = Text("Linked List").scale(0.5)
        linkedListText.move_to(linkedList)

        # Create a rectangle
        output = Rectangle(width=3, height=2, color=RED)
        output.rotate(PI/2).shift(RIGHT * 4.5)

        # Create text
        outputText = Text("output.txt").scale(0.5)
        outputText.move_to(output)

        self.play(Create(rectangle), Write(text), run_time=2)

        self.next_slide()

        arrow1 = Arrow(rectangle.get_right(), linkedList.get_left(), color=WHITE)
        mainText = Text("main.go").scale(0.5)
        mainText.shift(UP)
        self.play(Create(linkedList), Write(linkedListText), Write(mainText), GrowArrow(arrow1), run_time=2)

        self.next_slide(loop=True)

        self.play(Flash(linkedList, color=WHITE), run_time=2)

        self.next_slide()

        arrow2 = Arrow(linkedList.get_right(), output.get_left(), color=WHITE)
        self.play(Create(output), Write(outputText), GrowArrow(arrow2), run_time=2)

        self.next_slide()

        self.play(FadeOut(rectangle), FadeOut(linkedList), FadeOut(output), FadeOut(text), FadeOut(linkedListText), FadeOut(outputText), FadeOut(mainText), FadeOut(arrow1), FadeOut(arrow2), run_time=2)