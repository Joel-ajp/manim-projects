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
            "Driver installations off-rip (and made easy)",
            "You choose your desktop environment",
            "Alot of typing",
        ).scale(1).shift(LEFT + UP * 0.75)
        self.play(Transform(installation, installBSD), Transform(popInstallBullet, bsdInstallBullet))

        bsdCode = '''$ pkg install xorg
$ pw groupmod video -m <username>
$ pkg install drm-kmod
$ sysrc kld_list+=i915kms
$ pkg install nvidia-driver
$ sysrc kld_list+=nvidia-modeset
$ pkg install xfce
$ sysrc dbus_enable="YES"
$ pkg install lightdm lightdm-gtk-greeter
$ sysrc lightdm_enable="YES"
$ % echo \'. /usr/local/etc/xdg/xfce4/xinitrc\' > ~/.xinitrc
'''
        self.next_slide()

        self.play(FadeOut(popInstallBullet), run_time=0.2)

        codeRender = Code(code=bsdCode, language="bash", background="rectangle",  insert_line_no=False).scale(1).center()

        self.play(Write(codeRender), run_time=3.5)

        self.next_slide()

        self.play(FadeOut(installation), FadeOut(codeRender))

        bsdScoreTxt = Text("0").scale(3).shift(LEFT*3)
        popScoreTxt = Text("0").scale(3).shift(RIGHT*3)
        pop_OS = Text("Pop_OS!").scale(1.5).shift(RIGHT*3).to_edge(UP)

        self.play(FadeIn(title), FadeIn(pop_OS), FadeIn(bsdScoreTxt), FadeIn(popScoreTxt), FadeIn(line))

        bsdScoreTxtNew = Text("1").scale(3).shift(LEFT*3)

        self.play(Transform(bsdScoreTxt, bsdScoreTxtNew), run_time=0.5)

        self.next_slide()

        self.play(FadeOut(title), FadeOut(pop_OS), FadeOut(bsdScoreTxt), FadeOut(popScoreTxt), FadeOut(line))
        self.wait(1)
        userExperience = Text("User Experience").scale(2)
        self.play(Write(userExperience)) 
        self.next_slide()        

        userExperiencePop = Text("User Experience | Pop_OS!").to_corner(UP + LEFT) 
        popOSBullet = BulletedList(
            "Uses a custom GNOME desktop environment",
            "Baked in tiling window manager (Mutter)",
            "Familiar package manager (apt)",
        ).shift(LEFT + UP * 0.75).scale(1)

        self.play(Transform(userExperience, userExperiencePop), FadeIn(popOSBullet))

        self.next_slide()

        userExperienceBsd = Text("User Experience | Free BSD").to_corner(UP + LEFT) 
        bsdBullet = BulletedList(
            "Feels like a Linux distro",
            "Documentation for your needs",
            "You choose your desktop environment",
        ).shift(LEFT + UP * 0.75).scale(1.25)

        self.remove(userExperiencePop)
        self.play(Transform(userExperience, userExperienceBsd), Transform(popOSBullet, bsdBullet))

        self.next_slide()

        self.play(FadeOut(userExperience), FadeOut(popOSBullet))

        bsdScoreTxt = Text("1").scale(3).shift(LEFT*3)
        popScoreTxt = Text("0").scale(3).shift(RIGHT*3)
        pop_OS = Text("Pop_OS!").scale(1.5).shift(RIGHT*3).to_edge(UP)

        self.play(FadeIn(title), FadeIn(pop_OS), FadeIn(bsdScoreTxt), FadeIn(popScoreTxt), FadeIn(line))

        popScoreTxtNew = Text("1").scale(3).shift(RIGHT*3)

        self.play(Transform(popScoreTxt, popScoreTxtNew), run_time=0.5)

        self.next_slide()

        self.play(FadeOut(title), FadeOut(pop_OS), FadeOut(bsdScoreTxt), FadeOut(popScoreTxt), FadeOut(line))
        self.wait(1)
        # Insert point

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

        self.play(FadeOut(perf), FadeOut(project), FadeOut(rectangle), FadeOut(linkedList), FadeOut(output), FadeOut(text),
        FadeOut(linkedListText), FadeOut(outputText), FadeOut(mainText), FadeOut(arrow1), FadeOut(arrow2), run_time=2)

        self.wait()

        pop_OS = Text("Pop_OS!").scale(1.5).shift(RIGHT*3).to_edge(UP)

        self.play(FadeIn(title), FadeIn(pop_OS), FadeIn(line))

        bsdDetails = Text("Average Runtime: ").scale(1).shift(UP + LEFT*3)
        popDetails = Text("Average Runtime: ").scale(1).shift(UP + RIGHT*3)
        bsdAverage = Text("145.34ms").shift(LEFT*3)
        popAverage = Text("16.24ms").shift(RIGHT*3)

        self.play(Write(bsdDetails), Write(popDetails), Write(bsdAverage), Write(popAverage))

        self.next_slide()

        self.play(FadeOut(bsdDetails), FadeOut(popDetails), FadeOut(bsdAverage), FadeOut(popAverage))

        bsdScoreTxt = Text("1").scale(3).shift(LEFT*3)
        popScoreTxt = Text("1").scale(3).shift(RIGHT*3)
        pop_OS = Text("Pop_OS!").scale(1.5).shift(RIGHT*3).to_edge(UP)

        self.play(FadeIn(freeBSD), FadeIn(title), FadeIn(pop_OS), FadeIn(bsdScoreTxt), FadeIn(popScoreTxt), FadeIn(line))

        popScoreTxtNew = Text("2").scale(3).shift(RIGHT*3)

        self.play(Transform(popScoreTxt, popScoreTxtNew), run_time=0.5)

        self.next_slide()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        pop_OS = Text("Pop_OS!").scale(1.5).center()

        self.play(GrowFromCenter(pop_OS), Flash(pop_OS, color=GREEN, line_length=9), run_time=2)

        self.next_slide()
