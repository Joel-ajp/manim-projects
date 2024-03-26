from manim import *
from manim_slides import Slide

class Intro(Slide):
    def construct(self):
        define = Tex(r"$form$")
        define.to_corner(UP + LEFT)
        func = MathTex(r"\text{f(x)} = y").scale(2)
        base1 = Tex(r"With $x$ as the input and $y$ as the output.").scale(1.5)
        self.camera.background_color = "#212121"
        VGroup(func, base1).arrange(DOWN).space_out_submobjects(1.5)


        tx = Text("What is a function?")
        self.play(Write(tx))

        self.next_slide()


        self.play(Transform(tx, define))


        self.play(Write(func))

        self.next_slide()

        self.play(Write(base1))

        self.next_slide()

        self.play(FadeOut(tx), FadeOut(func), FadeOut(base1))