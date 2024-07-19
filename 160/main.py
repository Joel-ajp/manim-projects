
# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1322035373/

from code_style import main_style 
from manim import *

class intro(Scene):

    def construct(self):
    #     self.camera.background_color = "#12152c"

    # # Intro
    #     title_number = Text("160.", color="#FFFFFF").scale(1.2).shift(UP)
    #     title_number_drop_shadow = title_number.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
    #     title = Text("Intersection of Two Linked Lists", color="#FFFFFF").scale(1.2).move_to(title_number.get_center() + DOWN)
    #     title_drop_shadow = title.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
    #     self.play(Write(title), Write(title_number), Write(title_drop_shadow), Write(title_number_drop_shadow))
    #     self.wait()
    #     self.play(FadeOut(title), FadeOut(title_number), FadeOut(title_drop_shadow), FadeOut(title_number_drop_shadow))
    #     self.remove(title, title_number, title_drop_shadow, title_number_drop_shadow)

    #     list_a = [5, 4, 8, 1, 4]
    #     list_b = [5, 4, 8, 1, 6, 5]
    #     list_c = [8, 4, 5]

    #     list_a_nodes = []
    #     list_b_nodes = []
    #     list_c_nodes = []

    #     for i in range(len(list_a)):
    #         if i == len(list_a) - 1:
    #             node = Circle(radius=0.5, color="#04a1cc", fill_color="#017494", fill_opacity=1)
    #         else:
    #             node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
    #         node.move_to(UP * 2 + LEFT * (i - (len(list_a) - 1) / 2) * 1.5)
    #         list_a_nodes.append(node)

    #     for i in range(len(list_b)):
    #         if i == len(list_b) - 1:
    #             node = Circle(radius=0.5, color="#04a1cc", fill_color="#017494", fill_opacity=1)
    #         else:
    #             node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
    #         node.move_to(DOWN * 2 + LEFT * (i - (len(list_b) - 1) / 2) * 1.5)
    #         list_b_nodes.append(node)

    #     label_a = Text("List A", color="#ffffff").move_to(UP * 3)
    #     label_b = Text("List B", color="#ffffff").move_to(DOWN)

        head_cir = Circle(radius=0.15, color="#04a1cc", fill_color="#017494", fill_opacity=1).to_corner(UP + LEFT)
        head_label = Text("Head", color="#ffffff", font_size=17).next_to(head_cir, RIGHT)
        inter_cir = Circle(radius=0.15, color="#729762", fill_color="#597445", fill_opacity=1).move_to(head_cir, DOWN).shift(DOWN * 0.5)
        inter_label = Text("Intersect Node", color="#ffffff", font_size=17).next_to(inter_cir, RIGHT)

    #     self.play(*[DrawBorderThenFill(node) for node in list_a_nodes + list_b_nodes], Write(label_a), Write(label_b), DrawBorderThenFill(head_cir), Write(head_label), DrawBorderThenFill(inter_cir), Write(inter_label))

    #     lines = []

    #     for i in range(len(list_a)):
    #         line = Line(list_a_nodes[i].get_right(), list_a_nodes[0].get_center(), color="#ffffff")
    #         line.set_z_index(-1)
    #         lines.append(line)
        
    #     for i in range(len(list_b)):
    #         line = Line(list_b_nodes[i].get_center(), list_b_nodes[0].get_center(), color="#ffffff")
    #         line.set_z_index(-1)
    #         lines.append(line)

    #     for i in range(len(list_a)):
    #         line = always_redraw(lambda i=i: Line(list_a_nodes[i].get_center(), list_a_nodes[0].get_center(), color="#ffffff").set_z_index(-1))
    #         lines.append(line)
    #         self.add(line)

    #     for i in range(len(list_b)):
    #         line = always_redraw(lambda i=i: Line(list_b_nodes[i].get_center(), list_b_nodes[0].get_center(), color="#ffffff").set_z_index(-1))
    #         lines.append(line)
    #         self.add(line)

        
    #     numbers = []

    #     # add numbers to the nodes
    #     for i in range(len(list_a)):
    #         number = always_redraw(lambda i=i: Text(str(list_a[i]), color="#ffffff").move_to(list_a_nodes[i].get_center()))
    #         numbers.append(number)
    #         self.add(number)

    #     for i in range(len(list_b)):
    #         number = always_redraw(lambda i=i: Text(str(list_b[i]), color="#ffffff").move_to(list_b_nodes[i].get_center()))
    #         numbers.append(number)
    #         self.add(number)
        

    #     self.play(*[Create(line) for line in lines], *[Write(num) for num in numbers])
    #     self.wait()

    #     l_a = Text("a. ", color="#ffffff").move_to(list_a_nodes[-1], LEFT * 2).to_edge(LEFT)
    #     l_b = Text("b. ", color="#ffffff").move_to(list_b_nodes[-1], LEFT * 2).to_edge(LEFT)

    #     self.play(FadeOut(label_a), FadeOut(label_b))

    #     for i in range(len(list_c)):
    #         if i == 0:
    #             # Green
    #             node = Circle(radius=0.5, color="#729762", fill_color="#597445", fill_opacity=1)
    #         else:
    #             node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
    #         node.move_to(RIGHT * 2 + RIGHT * (i - (len(list_c) - 1) / 2) * 1.5)
    #         list_c_nodes.append(node)
    #         self.add(node)

    #     nums = [] 

    #     for i in range(len(list_c)):
    #         number = always_redraw(lambda i=i: Text(str(list_c[i]), color="#ffffff").move_to(list_c_nodes[i].get_center()))
    #         nums.append(number)
    #         self.add(number)
        
    #     self.play(*[DrawBorderThenFill(node) for node in list_c_nodes], 
    #               *[(Write(num) for num in nums)],
    #               *[FadeOut(list_a_nodes[i]) for i in range(2, -1, -1)],
    #               *[FadeOut(list_b_nodes[i]) for i in range(2, -1, -1)],
    #               *[FadeOut(numbers[i]) for i in range(2, -1, -1)],
    #               *[FadeOut(numbers[i + 5]) for i in range(2, -1, -1)],
    #               *[FadeOut(line) for line in lines],
    #               *[list_b_nodes[i].animate.shift(LEFT * 0.705) for i in range(len(list_b_nodes) - 3, len(list_b_nodes))], Write(l_a), Write(l_b)
    #               )
                
    #     lines = []

    #     _lines = []

    #     a_line_0 = Line(list_a_nodes[4].get_right(), list_a_nodes[3].get_left(), color="#ffffff")

    #     a_start_point = list_a_nodes[3].get_right()
    #     a_end_point = list_c_nodes[0].get_left()
    #     a_control_point1 = list_a_nodes[3].get_right() + RIGHT 
    #     a_control_point2 = list_c_nodes[0].get_left() + LEFT 

    #     # Create the backwards "S" shape using CubicBezier
    #     a_backwards_s = CubicBezier(a_start_point, a_control_point1, a_control_point2, a_end_point, color=WHITE)

    #     b_start_point = list_b_nodes[3].get_right()
    #     b_end_point = list_c_nodes[0].get_left()
    #     b_control_point1 = list_b_nodes[3].get_right() + RIGHT
    #     b_control_point2 = list_c_nodes[0].get_left() + LEFT

    #     b_backwards_s = CubicBezier(b_start_point, b_control_point1, b_control_point2, b_end_point, color=WHITE)

    #     # Add the shape to the scene

    #     b_line_0 = Line(list_b_nodes[5].get_right(), list_b_nodes[4].get_left(), color="#ffffff")
    #     b_line_1 = Line(list_b_nodes[4].get_right(), list_b_nodes[3].get_left(), color="#ffffff")

    #     c_line_0 = Line(list_c_nodes[0].get_right(), list_c_nodes[1].get_left(), color="#ffffff")
    #     c_line_1 = Line(list_c_nodes[1].get_right(), list_c_nodes[2].get_left(), color="#ffffff")

    #     _lines.append(a_line_0)
    #     _lines.append(b_line_0)
    #     _lines.append(b_line_1)
    #     _lines.append(c_line_0)
    #     _lines.append(c_line_1)

    #     self.play((Create(line) for line in _lines), Create(a_backwards_s), Create(b_backwards_s))
    #     self.wait(2)

    #     _main = self.mobjects
    #     self.play(*[FadeOut(mobject) for mobject in self.mobjects])
    #     self.wait()
        
    # # Node def
    #     node = Circle(radius=1, color="#FE5F55", fill_color="#A64942", fill_opacity=1).center()
    #     node_def = Text("type ListNode struct {\n\n\tVal int\n\n\tNext *ListNode\n\n}", color="#ffffff", font_size=30).next_to(node, LEFT).shift(LEFT * 1.25)
    #     node_val = Text("Val", color="#ffffff", font_size=30).move_to(node.get_center())

    #     node_next = Circle(radius=1, color="#FE5F55", fill_color="#A64942", fill_opacity=1).next_to(node, RIGHT).shift(RIGHT * 1.25)
    #     next_text = Text("Val", color="#ffffff", font_size=30).move_to(node_next.get_center())
    #     node_line = Line(node.get_right(), node_next.get_left(), color="#ffffff").set_z_index(-1)

    #     node_nil = DashedVMobject(Circle(radius=1, color="#FE5F55").next_to(node, RIGHT).shift(RIGHT * 1.25), dashed_ratio=0.55)
    #     next_nil = Text("nil", color="#ffffff", font_size=30).move_to(node_nil.get_center())

    #     self.play(DrawBorderThenFill(node), Write(node_def), Write(node_val))
    #     self.wait(1)
    #     self.play(DrawBorderThenFill(node_next), Create(node_line), Write(next_text))
    #     self.wait(1)
    #     self.play(Transform(node_next, node_nil), Transform(next_text, next_nil))
    #     self.wait(1)
    #     self.play(FadeOut(node), FadeOut(node_def), FadeOut(node_val), FadeOut(node_next), FadeOut(next_text), FadeOut(node_line), FadeOut(node_nil), FadeOut(next_nil))
    #     self.remove(node, node_def, node_val, node_next, next_text, node_line, node_nil, next_nil)

    #     self.play(*[FadeIn(mobject) for mobject in _main])
    #     self.wait(1)

    #     dot_a = Dot(color=WHITE).move_to(a_start_point)
    #     self.add(dot_a)
    #     dot_b = Dot(color=WHITE).move_to(b_start_point)
    #     self.add(dot_b)
    #     self.play(MoveAlongPath(dot_a, a_backwards_s), MoveAlongPath(dot_b, b_backwards_s), run_time=2)
    #     self.remove(dot_b)
    #     self.add(nums[0])
    #     self.play(Transform(dot_a, list_c_nodes[0].copy()), run_time=1)
    #     self.wait()
    #     self.wait(2)
    #     self.play(*[FadeOut(mobject) for mobject in self.mobjects])
    #     self.wait(1)

    # # Brute Force
    #     intu = Text("Brute Force", color="#ffffff").scale(1.2)
    #     intu_drop_shadow = intu.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
    #     self.play(Write(intu), Write(intu_drop_shadow))
    #     self.wait(1)        
    #     self.play(FadeOut(intu), FadeOut(intu_drop_shadow))

    #     a_arrow = Arrow(start=UP * 0.7, end=DOWN * 0.7, color=WHITE, ).next_to(list_a_nodes[-1], UP)
    #     b_arrow = Arrow(start=DOWN * 0.7, end=UP * 0.7, color=WHITE, ).next_to(list_b_nodes[-1], DOWN)

    #     # This is the worst code I have ever written, no joke
    #     self.play(FadeIn(mobject) for mobject in _main)    
    #     self.wait()

    #     # Add a nil node to the end of the list_c_nodes
    #     c_nil = DashedVMobject(Circle(radius=0.5, color="#FE5F55").move_to(list_c_nodes[-1].get_center() + RIGHT * 1.5), dashed_ratio=0.45)
    #     c_nil_text = Text("nil", color="#ffffff", font_size=25).move_to(c_nil.get_center())
    #     c_nil_line = Line(list_c_nodes[-1].get_right(), c_nil.get_left(), color="#ffffff").set_z_index(-1)

    #     self.play(DrawBorderThenFill(c_nil), Create(c_nil_line), Write(c_nil_text))
    #     self.wait(1)
    #     self.play(Create(a_arrow), Create(b_arrow))
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-2], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-3], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[0], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[1], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[2], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(c_nil, DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(a_arrow.animate.next_to(list_a_nodes[-2], UP), b_arrow.animate.next_to(list_b_nodes[-1], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-2], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-3], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[0], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[1], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[2], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(c_nil, DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(a_arrow.animate.next_to(list_c_nodes[0], UP), b_arrow.animate.next_to(list_b_nodes[-1], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-2], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_b_nodes[-3], DOWN), run_time=0.5)
    #     self.wait(0.5)
    #     self.play(b_arrow.animate.next_to(list_c_nodes[0], DOWN), run_time=0.5)
    #     self.wait(1)

    #     # circle transition
        cir_trans = Circle(radius=1, color="#ffffff", fill_color="#31355a", fill_opacity=1).scale(0.1)
    #     self.add(cir_trans)
    #     self.play(GrowFromCenter(cir_trans), cir_trans.animate.scale(100), run_time=3)

    #     for mob in self.mobjects:
    #         self.remove(mob)

    #     brute_force = Text("Brute Force", color="#ffffff", font_size=30).scale(1.2)
    #     brute_force.to_corner(UP + RIGHT)
    #     brute_force_drop_shadow = brute_force.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025)
    #     brute_force_drop_shadow.set_z_index(-1)
    #     brute_force_drop_shadow.set_opacity(0.5)

    #     self.camera.background_color = "#31355a"
    #     intu_code = Code("brute.go", style="github-dark", language="Go", font="Monospace", tab_width=3, line_spacing=0.4)
    #     intu_code.line_numbers.set_color(WHITE)
    #     intu_code_copy = intu_code.copy()
    #     intu_code_copy.set_color(BLACK)
    #     intu_code_copy.set_opacity(0.5)
    #     intu_code_copy.shift(DOWN * 0.1 + LEFT * 0.1)
    #     intu_code_copy.set_z_index(-1)
    #     cursor = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).next_to(intu_code.code[-1], RIGHT * 0.5)
    #     turn_animation_into_updater(FadeIn(cursor), FadeOut(cursor), run_time=1)

    #     self.play(Write(intu_code), Write(intu_code_copy), Write(brute_force), Write(brute_force_drop_shadow), run_time=2)
    #     self.add(cursor)
    #     self.wait(5)
    #     cursor_0 = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).move_to(intu_code.code[1].get_center()).shift(LEFT * 1.95 + DOWN * 0.1)
    #     turn_animation_into_updater(FadeIn(cursor_0), FadeOut(cursor_0), run_time=1)

    #     self.remove(cursor)
    #     self.add(cursor_0)
    #     self.wait(5)

    #     hightlight = Rectangle(color="#04a1cc", fill_color="#017494", height=0.35, width=5, fill_opacity=0.1).move_to(intu_code.code[1].get_left()).shift(DOWN * 0.1 + RIGHT * 1.25)
    #     hightlight0 = Rectangle(color="#04a1cc", fill_color="#017494", height=0.35, width=6, fill_opacity=0.1).move_to(intu_code.code[10].get_left()).shift(DOWN * 0.1 + RIGHT * 1)
    #     cursor_1 = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).move_to(cursor_0)
    #     self.add(cursor_1)
    #     self.remove(cursor_0)
    #     self.play(Transform(cursor_1, hightlight), FadeIn(hightlight0), run_time=1)
    #     self.wait(2)
    #     hightlight1 = Rectangle(color="#729762", fill_color="#597445", height=0.35, width=3, fill_opacity=0.1).move_to(intu_code.code[2].get_left()).shift(DOWN * 0.1 + RIGHT * 1.25)
    #     self.play(FadeIn(hightlight1), run_time=1)
    #     self.wait(2)
    #     hightlight2 = hightlight1.copy().move_to(intu_code.code[7].get_left()).shift(DOWN * 0.1 + RIGHT * 1.3)
    #     self.play(hightlight1.animate.move_to(intu_code.code[3].get_left()).shift(DOWN * 0.1 + RIGHT * 1.3), FadeIn(hightlight2), run_time=1)
    #     self.wait(2)
    #     highlight3 = Rectangle(color="#ffffff", fill_color="#ffffff", height=0.75, width=3, fill_opacity=0.1).move_to(intu_code.code[4].get_left()).shift(DOWN * 0.3 + RIGHT * 1.5)
    #     self.play(FadeIn(highlight3), run_time=1)
    #     self.wait(2)
    #     highlight4 = Rectangle(color="#FE5F55", fill_color="#A64942", height=0.35, width=2.25, fill_opacity=0.1).move_to(intu_code.code[12].get_left()).shift(DOWN * 0.1 + RIGHT * 1)
    #     self.play(FadeIn(highlight4), run_time=1)
    #     self.wait(2)
    #     time_complexity = Tex("$O(m \cdot n)$", color="#ffffff").scale(2.5).move_to(intu_code.get_corner(DOWN + RIGHT)).shift(UP * 1.75 + LEFT * 3.25)
    #     self.play(Write(time_complexity), run_time=2)
    #     self.wait(2)
    #     self.play(*[FadeOut(mobject) for mobject in self.mobjects], run_time=1)

        # self.camera.background_color = "#12152c"

        # a_list = [1, 9, 1,] 
        # b_list = [3,] 
        # c_list = [2, 4]

        # _a_list = []
        # _b_list = []
        # _c_list = []
        # num_a_list = []
        # num_b_list = []
        # num_c_list = []

        # for i in range(len(a_list)):
        #     if i == 0:
        #         node = Circle(radius=0.5, color="#04a1cc", fill_color="#017494", fill_opacity=1)
        #     else:
        #         node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
        #     node.move_to(UP * 2 + RIGHT * (i - (len(a_list) - 1) / 2) * 1.5)
        #     node.shift(LEFT * 1.5)
        #     _a_list.append(node)
        #     self.add(node)

        # for i in range(len(b_list)):
        #     if i == 0:
        #         node = Circle(radius=0.5, color="#04a1cc", fill_color="#017494", fill_opacity=1)
        #     else:
        #         node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
        #     node.move_to(DOWN * 2 + RIGHT * (i - (len(b_list) - 1) / 2) * 1.5)
        #     _b_list.append(node)
        #     self.add(node)

        # for i in range(len(c_list)):
        #     if i == 0:
        #         node = Circle(radius=0.5, color="#729762", fill_color="#597445", fill_opacity=1)
        #     else:
        #         node = Circle(radius=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
        #     node.move_to(ORIGIN + RIGHT * (i - (len(c_list) - 1) / 2) * 1.5)
        #     node.shift(RIGHT*3.5)
        #     _c_list.append(node)
        #     self.add(node)
        
        # # Add numbers to the nodes
        # for i in range(len(a_list)):
        #     number = Text(str(a_list[i]), color="#ffffff")
        #     number.move_to(_a_list[i].get_center())
        #     num_a_list.append(number)
        #     self.add(number)

        # for i in range(len(b_list)):
        #     number = Text(str(b_list[i]), color="#ffffff")
        #     number.move_to(_b_list[i].get_center())
        #     num_b_list.append(number)
        #     self.add(number)

        # for i in range(len(c_list)):
        #     number = Text(str(c_list[i]), color="#ffffff")
        #     number.move_to(_c_list[i].get_center())
        #     num_b_list.append(number)
        #     self.add(number)

        # # Add lines to the nodes
        # _a_lines = []
        # _b_lines = []
        # _c_lines = []

        # for i in range(len(a_list) - 1):
        #     line = always_redraw(lambda i=i: Line(_a_list[i].get_right(), _a_list[i + 1].get_left(), color="#ffffff").set_z_index(-1))
        #     _a_lines.append(line)
        
        # for i in range(len(b_list) - 1):
        #     line = always_redraw(lambda i=i: Line(_b_list[i].get_right(), _b_list[i + 1].get_left(), color="#ffffff").set_z_index(-1))
        #     _b_lines.append(line)

        # for i in range(len(c_list) - 1):
        #     line = always_redraw(lambda i=i: Line(_c_list[i].get_right(), _c_list[i + 1].get_left(), color="#ffffff").set_z_index(-1))
        #     _c_lines.append(line)

        # _a_start_point = _a_list[-1].get_right()
        # _a_end_point = _c_list[0].get_left()
        # _a_control_point1 = _a_list[-1].get_right() + RIGHT
        # _a_control_point2 = _c_list[0].get_left() + LEFT

        # _a_backwards_s = CubicBezier(_a_start_point, _a_control_point1, _a_control_point2, _a_end_point, color=WHITE)

        # _b_start_point = _b_list[-1].get_right()
        # _b_end_point = _c_list[0].get_left()
        # _b_control_point1 = _b_list[-1].get_right() + RIGHT
        # _b_control_point2 = _c_list[0].get_left() + LEFT

        # _b_backwards_s = CubicBezier(_b_start_point, _b_control_point1, _b_control_point2, _b_end_point, color=WHITE)

        # _c_nil = DashedVMobject(Circle(radius=0.5, color="#FE5F55").move_to(_c_list[-1].get_center() + RIGHT * 1.5), dashed_ratio=0.45)
        # _c_nil_text = Text("nil", color="#ffffff", font_size=25).move_to(_c_nil.get_center())
        # _c_nil_line = Line(_c_list[-1].get_right(), _c_nil.get_left(), color="#ffffff").set_z_index(-1)

        # lab_a = Text("a. ", color="#ffffff").move_to(_a_list[-1], LEFT * 2).to_edge(LEFT)
        # lab_b = Text("b. ", color="#ffffff").move_to(_b_list[-1], LEFT * 2).to_edge(LEFT)
        # self.add(head_cir, head_label, inter_cir, inter_label, lab_a, lab_b)

        # sol = Text("Final Solution", color="#000000").scale(1.2).shift(DOWN * 0.025, LEFT * 0.025)
        # sol_drop_shadow = sol.copy().set_color(WHITE).shift(UP * 0.025 + RIGHT * 0.025)
        # trans_cir = Circle(radius=1, color="#12152c", fill_color="#31355a", fill_opacity=1).scale(15)
        # self.add(trans_cir)
        # self.play(Write(sol), Write(sol_drop_shadow))
        # self.wait(2)
        # self.play(ShrinkToCenter(trans_cir), FadeOut(sol), FadeOut(sol_drop_shadow), run_time=1.5)
        # self.play(*[Create(line) for line in _a_lines], *[Create(line) for line in _b_lines], *[Create(line) for line in _c_lines], Create(_a_backwards_s), Create(_b_backwards_s), Write(_c_nil_text), Create(_c_nil_line), DrawBorderThenFill(_c_nil), run_time=1)
        # self.wait(2)

        # rec_flash = Rectangle(color="#ffffff", width=4.5, height=1.5).move_to(_c_list[-1])

        # self.play(ShowPassingFlash(rec_flash), run_time=2)
        # self.wait(2)


        # len_a = DecimalNumber(0, color="#ffffff", num_decimal_places=0).next_to(lab_a, RIGHT * 1.5).scale(1.75)
        # len_b = DecimalNumber(0, color="#ffffff", num_decimal_places=0).next_to(lab_b, RIGHT * 1.5).scale(1.75)

        # dot_a = Dot(color=WHITE).move_to(_a_list[0].get_right())
        # dot_b = Dot(color=WHITE).move_to(_b_list[0].get_right())
        # _a = _a_list[0].copy().set_opacity(0)
        # _b = _b_list[0].copy().set_opacity(0)
        # len_a.increment_value(1)
        # len_b.increment_value(1)
        # self.play(Transform(_a, dot_a), Transform(_b, dot_b), FadeIn(len_a), FadeIn(len_b), run_time=1)
        # self.wait(0.5)
        # self.play(MoveAlongPath(_b, _b_backwards_s), MoveAlongPath(_a, _a_lines[0]),  run_time=1)
        # dot_b = _c_list[0].copy().set_opacity(0)
        # dot_a = _a_list[1].copy().set_opacity(0)
        # len_a.increment_value(1)
        # len_b.increment_value(1)
        # self.play(Transform(_b, dot_b), Transform(_a, dot_a), run_time=1)
        # _a = Dot(color=WHITE).move_to(_a_list[1].get_right())
        # _b = Dot(color=WHITE).move_to(_c_list[0].get_right())
        # self.play(Transform(dot_a, _a), Transform(dot_b, _b), run_time=1)
        # self.wait(0.5)
        # self.play(MoveAlongPath(dot_b, _c_lines[0]), MoveAlongPath(dot_a, _a_lines[1]),  run_time=1)
        # len_a.increment_value(1)
        # len_b.increment_value(1)
        # _a = _a_list[2].copy().set_opacity(0)
        # _b = _c_list[1].copy().set_opacity(0)
        # self.play(Transform(dot_a, _a), Transform(dot_b, _b), run_time=1)
        # _a = Dot(color=WHITE).move_to(_a_list[2].get_right())
        # self.play(Transform(dot_a, _a), run_time=1)
        # self.wait(0.5)
        # self.play(MoveAlongPath(dot_a, _a_backwards_s),  run_time=1)
        # len_a.increment_value(1)
        # _a = _c_list[0].copy().set_opacity(0)
        # self.play(Transform(dot_a, _a), run_time=0.5)
        # dot_a = Dot(color=WHITE).move_to(_c_list[0].get_right())
        # self.play(Transform(_a, dot_a), run_time=0.5)
        # self.wait(0.5)
        # self.play(MoveAlongPath(_a, _c_lines[0]), run_time=0.5)
        # len_a.increment_value(1)
        # dot_a = _c_list[1].copy().set_opacity(0)
        # self.play(Transform(_a, dot_a), run_time=0.5)

                  
        # self.wait(2)

        # _a_arrow = Arrow(start=UP * 0.7, end=DOWN * 0.7, color=WHITE, ).next_to(_a_list[0], UP)
        # _b_arrow = Arrow(start=DOWN * 0.7, end=UP * 0.7, color=WHITE, ).next_to(_b_list[0], DOWN)

        # self.play(Create(_a_arrow), Create(_b_arrow))
        # self.play(_a_arrow.animate.next_to(_a_list[1], UP), run_time=1)
        # len_a.increment_value(-1)
        # self.play(_a_arrow.animate.next_to(_a_list[2], UP), run_time=1)
        # len_a.increment_value(-1)
        # self.wait(2)

        # self.play(
        #     FadeOut(_a_list[0]),
        #     FadeOut(_a_list[1]),
        #     FadeOut(_a_lines[0]),
        #     FadeOut(_a_lines[1]),
        #     FadeOut(num_a_list[0]),
        #     FadeOut(num_a_list[1]),)

        # self.wait(2)
        # self.play(_a_list[2].animate.set_color("#04a1cc").set_fill("#017494"), run_time=1)
        # self.wait(2)

        # self.play(
        #     _a_arrow.animate.next_to(_c_list[0], UP),
        #     _b_arrow.animate.next_to(_c_list[0], DOWN),
        # )

        # self.wait(2)

        # self.add(cir_trans)
        # self.play(GrowFromCenter(cir_trans), cir_trans.animate.scale(100), run_time=3)

        # for mob in self.mobjects:
        #     self.remove(mob)

        self.camera.background_color = "#31355a"

        self.wait(1)

        solution = Text("Final Solution", color="#ffffff", font_size=30).scale(1.2)
        solution.to_corner(UP + RIGHT)
        solution_ds = solution.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025)
        solution_ds.set_z_index(-1)
        solution_ds.set_opacity(0.5)

        len_code = Code("len.go", style="github-dark", language="Go", font="Monospace", tab_width=3, line_spacing=0.4)
        len_code.line_numbers.set_color(WHITE)
        len_code_copy = len_code.copy()
        len_code_copy.set_color(BLACK)
        len_code_copy.set_opacity(0.5)
        len_code_copy.shift(DOWN * 0.1 + LEFT * 0.1)
        len_code_copy.set_z_index(-1)
        cursor = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).next_to(len_code.code[-1], RIGHT * 0.5)
        turn_animation_into_updater(FadeIn(cursor), FadeOut(cursor), run_time=1)

        self.play(Write(len_code), Write(len_code_copy), Write(solution), Write(solution_ds), run_time=2)
        self.add(cursor)
        self.wait(5)

        self.remove(cursor)

        self.play(len_code.animate.scale(0.35), len_code_copy.animate.scale(0.35), run_time=1)
        self.play(len_code.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), len_code_copy.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), run_time=1)
        self.wait(3)

        sol_code = Code("sol.go", style="github-dark", language="Go", font="Monospace", tab_width=3, line_spacing=0.4).scale(0.825)
        sol_code.line_numbers.set_color(WHITE)
        sol_code_copy = sol_code.copy()
        sol_code_copy.set_color(BLACK)
        sol_code_copy.set_opacity(0.5)
        sol_code_copy.shift(DOWN * 0.1 + LEFT * 0.1)
        sol_code_copy.set_z_index(-1)
        cursor = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).next_to(sol_code.code[-1], RIGHT * 0.5)
        turn_animation_into_updater(FadeIn(cursor), FadeOut(cursor), run_time=1)

        self.play(Write(sol_code), Write(sol_code_copy), run_time=2)
        self.add(cursor)
        self.wait(5)

        self.remove(cursor)

        cursor_0 = Rectangle(width=0.125, height=0.25, color=WHITE).set_fill(WHITE).set_opacity(1).move_to(sol_code.code[1].get_center()).shift(DOWN * 0.1 + RIGHT * 0.4)
        turn_animation_into_updater(FadeIn(cursor_0), FadeOut(cursor_0), run_time=1)
        self.add(cursor_0)
        self.wait(5)

        cursor_1 = cursor_0.copy()
        self.remove(cursor_0)
        self.add(cursor_1)
        _rec_highlight = Rectangle(color="#04a1cc", fill_color="#017494", height=1.45, width=6, fill_opacity=0.1).move_to(sol_code.code[1].get_left()).shift(DOWN * 0.665 + RIGHT * 2)

        self.play(Transform(cursor_1, _rec_highlight), run_time=1)
        self.wait(3)

        _rec_highlight0 = Rectangle(color="#04a1cc", fill_color="#017494", height=1.25, width=5, fill_opacity=0.1).move_to(sol_code.code[6].get_left()).shift(DOWN * 0.5 + RIGHT * 1.25)

        self.play(Transform(cursor_1, _rec_highlight0), run_time=1)
        self.wait(3)

        _rec_highlight1 = Rectangle(color="#ffffff", fill_color="#ffffff", height=0.35, width=4.5, fill_opacity=0.1).move_to(sol_code.code[10].get_left()).shift(DOWN * 0.1 + RIGHT * 1.05)
        self.play(Transform(cursor_1, _rec_highlight1), run_time=1)
        self.wait(3)

        _rec_highlight2 = Rectangle(color="#729762", fill_color="#597445", height=0.35, width=2.25, fill_opacity=0.1).move_to(sol_code.code[14].get_left()).shift(DOWN * 0.1 + RIGHT * 1)
        self.play(Transform(cursor_1, _rec_highlight2), run_time=1)
        self.wait(3)

        self.play(FadeOut(cursor_1))
        self.wait(1)

        self.play(sol_code.animate.scale(0.2875), sol_code_copy.animate.scale(0.2875), run_time=1)
        big_o_expression = Tex("$O( ? )$", color="#ffffff").scale(2.5).shift(LEFT)
        big_o_expression_ds = big_o_expression.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)

        self.play(sol_code.animate.move_to(len_code.get_top()).shift(UP), sol_code_copy.animate.move_to(len_code.get_top()).shift(UP), Write(big_o_expression), Write(big_o_expression_ds), run_time=1)

        self.wait(2)

        self.play(FadeOut(big_o_expression), FadeOut(big_o_expression_ds), run_time=1)
        self.play(len_code.animate.center(), len_code_copy.animate.center().shift(DOWN * 0.1 + LEFT * 0.1), sol_code.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), sol_code_copy.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), run_time=2)
        self.play(len_code.animate.scale(3), len_code_copy.animate.scale(3), run_time=1)

        self.wait(2)

        _rec_highlight3 = Rectangle(color="#04a1cc", fill_color="#017494", height=0.45, width=8, fill_opacity=0.1).move_to(len_code.code[2].get_left()).shift(DOWN * 0.15 + RIGHT * 3.5)

        self.play(Create(_rec_highlight3))
        self.wait(2)
        self.play(FadeOut(_rec_highlight3),
        len_code.animate.scale(0.335), len_code_copy.animate.scale(0.335), run_time=1)
        big_o_expression = Tex("$O(m + n)$", color="#ffffff").scale(2.5).shift(LEFT)
        big_o_expression_ds = big_o_expression.copy().set_color(BLACK).shift(DOWN * 0.025 + LEFT * 0.025).set_z_index(-1)
        self.play(len_code.animate.move_to(sol_code.get_top()).shift(UP * 0.65), len_code_copy.animate.move_to(sol_code.get_top()).shift(UP * 0.65), Write(big_o_expression), Write(big_o_expression_ds), run_time=1)
        self.wait(2)

        self.play(FadeOut(big_o_expression), FadeOut(big_o_expression_ds), run_time=1)

        self.play(sol_code.animate.center(), sol_code_copy.animate.center().shift(DOWN * 0.1 , LEFT * 0.1), len_code.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), len_code_copy.animate.to_corner(DOWN + RIGHT).shift(DOWN * 0.25), run_time=2)
        self.play(sol_code.animate.scale(3.5), sol_code_copy.animate.scale(3.5), run_time=1)

        self.wait(2)
