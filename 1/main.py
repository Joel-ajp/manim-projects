# https://leetcode.com/problems/two-sum/
from manim import *

# hightlight node
# color="#04a1cc"
# fill_color="#017494"

# main node
# color="#FE5F55"
# fill_color="#A64942"

# green node
# color="#729762"
# fill_color="#597445"

class TwoSum(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#12152c"

    # Intro
        title_number = Text("1.", color="#FFFFFF").scale(1.2).shift(UP)
        title_number_drop_shadow = title_number.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        title = Text("Two Sum", color="#FFFFFF").scale(1.2).move_to(title_number.get_center() + DOWN)
        title_drop_shadow = title.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        self.play(Write(title), Write(title_number), Write(title_drop_shadow), Write(title_number_drop_shadow))
        self.wait()
        self.play(FadeOut(title), FadeOut(title_number), FadeOut(title_drop_shadow), FadeOut(title_number_drop_shadow))
        self.remove(title, title_number, title_drop_shadow, title_number_drop_shadow)
 
    # Problem
        nums = [2, 7, 11, 15]
        target = 9
        nodes = VGroup()

        for i in range(len(nums)):
            n = Square(side_length=1, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
            n.move_to(RIGHT * (i - (len(nums) - 1) / 2) * 1.5)
            nodes.add(n)

        self.play(Create(nodes))
        
        self.wait(2)
