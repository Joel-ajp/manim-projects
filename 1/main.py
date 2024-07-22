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
        nums = [3, 2, 7, 11, 15]
        nums_mobs = []
        nums_index_mobs = []
        target = 9
        nodes = []
        index_sq = Square(side_length=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1).to_corner(UL)
        index_sq_index = Text("n", color="#fe5f55", font_size=20).move_to(index_sq.get_center() + DOWN * 0.1 + LEFT * 0.1)
        index_label = Text("Index", color="#ffffff", font_size=20).move_to(index_sq.get_right()).shift(RIGHT * 0.5)
        index_label_ds = index_label.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        # target square
        target_sq = Square(side_length=0.5, color="#729762", fill_color="#597445", fill_opacity=1).to_corner(UL).shift(DOWN * 0.75)
        target_label = Text("Target", color="#ffffff", font_size=20).move_to(target_sq.get_right()).shift(RIGHT * 0.55)
        target_label_ds = target_label.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)

        for i in range(len(nums)):
            n = Square(side_length=1.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
            n.move_to(RIGHT * (i - (len(nums) - 1) / 2) * 2)
            nodes.append(n)
        
        for i in range(len(nums)):
            text = Text(str(nums[i]), color="#FFFFFF").move_to(nodes[i].get_center())
            nums_mobs.append(text)
        
        for i in range(len(nums)):
            text = Text(str(i), color="#FE5F55", font_size=20).move_to(nodes[i].get_center() + DOWN * 0.5 + LEFT * 0.5)
            nums_index_mobs.append(text)

        self.play(*[DrawBorderThenFill(n) for n in nodes],
                  *[Write(num) for num in nums_mobs],
                  *[Write(num) for num in nums_index_mobs],
                  DrawBorderThenFill(index_sq),
                  Write(index_label),
                  Write(index_label_ds),
                  Write(index_sq_index),)

        self.wait(2) 

        target_main = Square(side_length=1.5, color="#729762", fill_color="#597445", fill_opacity=1).move_to(DOWN * 2)
        target_main_label = Text(str(target), color="#ffffff").move_to(target_main.get_center())

        self.play(DrawBorderThenFill(target_main),
        Write(target_main_label),
        DrawBorderThenFill(target_sq),
        Write(target_label),
        Write(target_label_ds),
        *[n.animate.shift(UP * 1) for n in nodes], 
        *[n.animate.shift(UP * 1) for n in nums_mobs],
        *[n.animate.shift(UP * 1) for n in nums_index_mobs],
        )
        
        self.wait(2)

        sum_tag = Square(side_length=0.5, color="#04a1cc", fill_color="#017494", fill_opacity=1).to_corner(UL).shift(RIGHT * 1.75)
        sum_label = Text("Sum", color="#ffffff", font_size=20).move_to(sum_tag.get_right()).shift(RIGHT * 0.45)
        sum_label_ds = sum_label.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        sum = Square(side_length=1.5, color="#04a1cc", fill_color="#017494", fill_opacity=1).move_to(DOWN * 2 + LEFT * 2)
        sum_equal = Text("==", color="#ffffff").move_to(DOWN * 2)
        sum_equal_ds = sum_equal.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        sum_text = Text(f"nums[i]\n     +\nnums[j]", color="#ffffff", font_size=25).move_to(sum.get_center())

        self.play(
        DrawBorderThenFill(sum_tag),
        Write(sum_label),
        Write(sum_label_ds),
        DrawBorderThenFill(sum),
        Write(sum_text),
        Write(sum_equal),
        Write(sum_equal_ds),
        target_main.animate.shift(RIGHT * 2),
        target_main_label.animate.shift(RIGHT * 2),
        )

        self.wait(2)

        _main = []

        for mob in self.mobjects:
            _main.append(mob)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
            
        self.wait(2)

        brute_force = Text("Brute Force", color="#ffffff").scale(1.2)

        self.play(Write(brute_force))
        self.wait(2)
        self.play(FadeOut(brute_force))
        _main.remove(sum_text)
        self.play(*[FadeIn(mob) for mob in _main])
        self.wait(2)

        line_0 = CubicBezier(nodes[0].get_bottom(), (nodes[0].get_right() + DOWN * 2),end_handle=(sum.get_left() + UP * 2), end_anchor=sum.get_top(), color="#ffffff")
        line_1 = Line(nodes[1].get_bottom(), sum.get_top(), color="#ffffff")
        self.play(Create(line_0), Create(line_1))

        self.wait(2)


