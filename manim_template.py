from manim import *

class intro(Scene):
    def construct(self):
        theme = set_theme(self)




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
def circle_transition(scene, color="#ffffff", fill_color="#31355a", run_time=3, scale_factor=100):
    cir_trans = Circle(radius=1, color=color, fill_color=fill_color, fill_opacity=1).scale(0.1)
    scene.add(cir_trans)
    scene.play(GrowFromCenter(cir_trans), cir_trans.animate.scale(scale_factor), run_time=run_time)
    scene.remove(cir_trans)


def add_text_drop_shadow(text_obj, shadow_color=BLACK, offset=DOWN * 0.025 + LEFT * 0.025, opacity=1, z_index=-1):
    """
    Adds a drop shadow to a text object.
    :param text_obj: The original Text or Tex object.
    :param shadow_color: Color of the drop shadow.
    :param offset: Offset of the shadow relative to the text.
    :param opacity: Opacity of the shadow.
    :param z_index: z_index to control rendering order.
    :return: A VGroup containing the original text and its drop shadow.
    """
    shadow = text_obj.copy().set_color(shadow_color).shift(offset).set_opacity(opacity).set_z_index(z_index)
    return VGroup(shadow, text_obj)

from manim import *

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
def circle_transition(scene, color="#ffffff", fill_color="#31355a", run_time=3, scale_factor=100):
    cir_trans = Circle(radius=1, color=color, fill_color=fill_color, fill_opacity=1).scale(0.1)
    scene.add(cir_trans)
    scene.play(GrowFromCenter(cir_trans), cir_trans.animate.scale(scale_factor), run_time=run_time)
    scene.remove(cir_trans)

# Utility to add a drop shadow to text
def add_text_drop_shadow(text_obj, shadow_color=BLACK, offset=DOWN * 0.025 + LEFT * 0.025, opacity=1, z_index=-1):
    shadow = text_obj.copy().set_color(shadow_color).shift(offset).set_opacity(opacity).set_z_index(z_index)
    return VGroup(shadow, text_obj)

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
