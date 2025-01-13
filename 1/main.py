from manim import *

class Main(Scene):
    def construct(self):
        theme = set_theme(self)
        title = add_text_drop_shadow("1.\nTwo Sum")

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        self.remove(title)
        self.wait(3)

        index_sq = Square(side_length=0.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1).to_corner(UL)
        index_sq_index = Text("n", color="#fe5f55", font_size=20).move_to(index_sq.get_center() + DOWN * 0.1 + RIGHT * 0.1)
        index_label = add_text_drop_shadow("Element", font_size=20).move_to(index_sq.get_right() + RIGHT * 0.65)

        target_sq = Square(side_length=0.5, color="#729762", fill_color="#597445", fill_opacity=1).to_corner(UL).shift(DOWN * 0.75)
        target_label = add_text_drop_shadow("Target", font_size=20).move_to(target_sq.get_right() + RIGHT * 0.55)

        squares = create_indexed_squares_vgroup([2, 7, 11, 15]).move_to(ORIGIN)
        self.play(Create(squares))
        self.wait()
        self.play(Create(index_sq), Create(index_sq_index), Write(index_label))
        self.wait()
        self.play(Create(target_sq), Write(target_label))
        self.wait(3)


# Utility to set color theme and background
def set_theme(scene, background_color="#12152c", primary_color="#FE5F55", secondary_color="#04a1cc", fill_primary="#A64942", fill_secondary="#017494", text_color="#ffffff"):
    scene.camera.background_color = background_color
    theme = {
        "primary_color": primary_color,
        "secondary_color": secondary_color,
        "fill_primary": fill_primary,
        "fill_secondary": fill_secondary,
        "text_color": text_color
    }
    return theme

# Utility to create a circle transition effect
def circle_transition_in(scene, color="#ffffff", fill_color="#31355a", run_time=3, scale_factor=100):
    cir_trans = Circle(radius=1, color=color, fill_color=fill_color, fill_opacity=1).scale(0.1)
    scene.add(cir_trans)
    scene.play(GrowFromCenter(cir_trans), cir_trans.animate.scale(scale_factor), run_time=run_time)
    scene.camera.background_color = fill_color
    scene.remove(cir_trans)

def circle_transition_out(scene, color="#ffffff", fill_color="#31355a", background_color="#12152c", run_time=3, scale_factor=100):
    """
    You have to add mobjects before using this function and make sure to send them to back of the frame. This way when the circle shrinks, it will reveal the mobjects. 
    """
    cir_trans = Circle(radius=scale_factor, color=color, fill_color=fill_color, fill_opacity=1)
    cir_trans.move_to(scene.camera.frame_center)
    scene.add(cir_trans)
    scene.camera.background_color = background_color
    scene.play(ShrinkToCenter(cir_trans), run_time=run_time)
    scene.remove(cir_trans)

def add_text_drop_shadow(text, shadow_color=BLACK, offset=DOWN * 0.025 + LEFT * 0.025, opacity=1, z_index=-1, font_size=50):
    """
    Adds a drop shadow to a text object.
    :param text_obj: The original Text or Tex object.
    :param shadow_color: Color of the drop shadow.
    :param offset: Offset of the shadow relative to the text.
    :param opacity: Opacity of the shadow.
    :param z_index: z_index to control rendering order.
    :return: A VGroup containing the original text and its drop shadow.
    """

    text_obj = Text(text, font_size=font_size).set_color(WHITE)
    shadow = text_obj.copy().set_color(shadow_color).shift(offset).set_opacity(opacity).set_z_index(z_index)
    return VGroup(text_obj, shadow)

# Utility to create a code block with drop shadow
def create_code_block(file_name, language="Go", style="github-dark", font="Monospace", tab_width=3, line_spacing=0.4, shadow_offset=DOWN * 0.1 + LEFT * 0.1, shadow_opacity=0.5):
    """
    Creates a formatted code block with a drop shadow.
    :param file_name: The name of the file or placeholder text for the code block.
    :param language: The language for syntax highlighting.
    :param style: Style for syntax highlighting.
    :param font: Font for the code.
    :param tab_width: Tab width inside the code.
    :param line_spacing: Spacing between lines.
    :param shadow_offset: Offset for the shadow.
    :param shadow_opacity: Opacity of the shadow.
    :return: A VGroup containing the code block and its shadow.
    """
    code = Code(file_name, style=style, language=language, font=font, tab_width=tab_width, line_spacing=line_spacing)
    code.line_numbers.set_color(WHITE)

    # Create drop shadow for the code block
    shadow = code.copy()
    shadow.set_color(BLACK)
    shadow.set_opacity(shadow_opacity)
    shadow.shift(shadow_offset)
    shadow.set_z_index(-1)

    return VGroup(shadow, code)

def create_indexed_squares_vgroup(_nums):
    """Creates a VGroup of squares with indices at the bottom right."""
    _nodes = []
    _nums_mobs = []
    _nums_index_mobs = []

    for i in range(len(_nums)):
        # Create a square and position it
        n = Square(side_length=1.5, color="#FE5F55", fill_color="#A64942", fill_opacity=1)
        n.move_to(RIGHT * (i - (len(_nums) - 1) / 2) * 2)
        _nodes.append(n)
    
    for i in range(len(_nums)):
        # Create the number text in the center of the square
        text = Text(str(_nums[i]), color="#FFFFFF").move_to(_nodes[i].get_center())
        _nums_mobs.append(text)
    
    for i in range(len(_nums)):
        # Create the index text at the bottom right of the square
        index_text = Text(str(i), color="#FE5F55", font_size=20)
        index_text.move_to(_nodes[i].get_center() + DOWN * 0.5 + RIGHT * 0.5)
        _nums_index_mobs.append(index_text)

    # Create a VGroup containing all squares, numbers, and indices
    return VGroup(*_nodes, *_nums_mobs, *_nums_index_mobs)
