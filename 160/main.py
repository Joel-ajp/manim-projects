# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1322035373/

from manim import *

class intro(Scene):
    def construct(self):
        self.camera.background_color = "#12152c"

    # # Intro
    #     title_number = Text("160.", color="#FFFFFF").scale(1.2).shift(UP)
    #     title = Text("Intersection of Two Linked Lists", color="#FFFFFF").scale(1.2).move_to(title_number.get_center() + DOWN)
    #     self.play(Write(title), Write(title_number))
    #     self.wait()
    #     self.play(FadeOut(title), FadeOut(title_number))
    #     self.remove(title, title_number)

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

    #     head_cir = Circle(radius=0.15, color="#04a1cc", fill_color="#017494", fill_opacity=1).to_corner(UP + LEFT)
    #     head_label = Text("Head", color="#ffffff", font_size=17).next_to(head_cir, RIGHT)
    #     inter_cir = Circle(radius=0.15, color="#729762", fill_color="#597445", fill_opacity=1).move_to(head_cir, DOWN).shift(DOWN * 0.5)
    #     inter_label = Text("Intersect Node", color="#ffffff", font_size=17).next_to(inter_cir, RIGHT)

    #     self.play(*[DrawBorderThenFill(node) for node in list_a_nodes + list_b_nodes], Write(label_a), Write(label_b), DrawBorderThenFill(head_cir), Write(head_label), DrawBorderThenFill(inter_cir), Write(inter_label))

    #     lines = []

    #     # for i in range(len(list_a)):
    #     #     line = Line(list_a_nodes[i].get_right(), list_a_nodes[0].get_center(), color="#ffffff")
    #     #     line.set_z_index(-1)
    #     #     lines.append(line)
    #     #
    #     # for i in range(len(list_b)):
    #     #     line = Line(list_b_nodes[i].get_center(), list_b_nodes[0].get_center(), color="#ffffff")
    #     #     line.set_z_index(-1)
    #     #     lines.append(line)

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
    #     # for i in range(len(list_a)):
    #     #     number = Text(str(list_a[i]), color="#ffffff")
    #     #     number.move_to(list_a_nodes[i].get_center())
    #     #     numbers.append(number)
    #     # 
    #     # for i in range(len(list_b)):
    #     #     number = Text(str(list_b[i]), color="#ffffff")
    #     #     number.move_to(list_b_nodes[i].get_center())
    #     #     numbers.append(number)

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
        
    #     self.play(*[DrawBorderThenFill(node) for node in list_c_nodes], (Write(num) for num in nums),
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
    #     self.play(FadeOut(mobject) for mobject in self.mobjects)
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

    #     self.play(FadeIn(mobject) for mobject in _main)
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
    #     self.play(FadeOut(mobject) for mobject in self.mobjects)
    #     self.wait(1)

    # Brute Force
        intu = Text("Intuition", color="#ffffff").scale(1.2)
        self.play(Write(intu))
        self.wait(1)        
        self.play(FadeOut(intu))

        intu_code = Code("brute.go", style="lightbulb", language="go", insert_line_no=True, font="Monospace", tab_width=3, background_stroke_color=WHITE, line_spacing=0.4)
        self.play(Write(intu_code))
        self.wait(3)

