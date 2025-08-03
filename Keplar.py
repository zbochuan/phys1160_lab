from manimlib import *
import numpy as np

class KeplersLaws(Scene):
    def construct(self):
        # Title screen
        title = Text("Kepler's Three Laws", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # First Law
        self.first_law()
        
        # Second Law  
        self.second_law()
        
        # Third Law
        self.third_law()

    def first_law(self):
        # Law 1 Title
        title = Text("First Law: Elliptical Orbits", font_size=36, color=BLUE)
        title.to_edge(UP)
        
        desc = Text("Planets orbit the Sun in elliptical paths", font_size=24)
        desc.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(desc))
        
        # Define ellipse parameters
        a = 3  # semi-major axis
        b = 2  # semi-minor axis  
        c = np.sqrt(a**2 - b**2)  # focal distance
        
        # Create ellipse with Sun at focus
        ellipse = Ellipse(width=2*a, height=2*b, color=WHITE)
        # Keep ellipse centered at origin
        
        # Sun at the LEFT focus of the ellipse  
        sun = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
        sun.shift(LEFT * c)
        
        # Planet
        planet = Circle(radius=0.15, color=BLUE, fill_opacity=1)
        
        self.play(ShowCreation(ellipse))
        self.play(FadeIn(sun))
        self.play(FadeIn(planet))
        
        # Position planet at starting point ON the ellipse  
        planet.move_to([a, 0, 0])  # Perihelion position (rightmost point)
        
        # Animate planet moving exactly on the ellipse path
        def orbit_updater(mob, alpha):
            angle = alpha * 2 * PI
            # Calculate position on ellipse centered at origin
            x = a * np.cos(angle)
            y = b * np.sin(angle)  
            mob.move_to([x, y, 0])
        
        self.play(UpdateFromAlphaFunc(planet, orbit_updater), run_time=4)
        
        # Add labels
        sun_label = Text("Sun", font_size=16, color=YELLOW)
        sun_label.next_to(sun, DOWN)
        self.play(Write(sun_label))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def second_law(self):
        # Law 2 Title
        title = Text("Second Law: Equal Areas", font_size=36, color=GREEN)
        title.to_edge(UP)
        
        desc = Text("Planets sweep equal areas in equal time", font_size=24)
        desc.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(desc))
        
        # Define ellipse parameters (same as first law)
        a = 3
        b = 2
        c = np.sqrt(a**2 - b**2)
        
        # Create ellipse with Sun at focus (same as first law)
        ellipse = Ellipse(width=2*a, height=2*b, color=WHITE)
        # Don't shift the ellipse - keep it centered at origin
        
        # Sun at the LEFT focus of the ellipse
        sun = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
        sun.shift(LEFT * c)  # This puts sun at the focus
        
        planet = Circle(radius=0.15, color=BLUE, fill_opacity=1)
        
        self.play(ShowCreation(ellipse))
        self.play(FadeIn(sun))
        self.play(FadeIn(planet))
        
        # Position planet on the ellipse at perihelion
        planet.move_to([a, 0, 0])  # Perihelion (rightmost point of ellipse)
        
        # Create sector area near perihelion using arc
        start_angle = 0
        end_angle = 0.3
        
        # Create points for the sector area
        sector_points = [sun.get_center()]  # Start from sun
        # Add points along the ellipse arc
        for i in range(int(end_angle * 20) + 1):  # More points for smooth curve
            angle = start_angle + i * (end_angle - start_angle) / (end_angle * 20)
            x = a * np.cos(angle)
            y = b * np.sin(angle)
            sector_points.append([x, y, 0])
        
        area1 = Polygon(*sector_points, color=RED, fill_opacity=0.3, stroke_color=RED)
        
        # Animate planet moving along this small arc ON the ellipse
        def perihelion_updater(mob, alpha):
            angle = alpha * 0.3  # Small arc near perihelion
            x = a * np.cos(angle)  # Ellipse centered at origin
            y = b * np.sin(angle)
            mob.move_to([x, y, 0])
        
        self.play(ShowCreation(area1))
        self.play(UpdateFromAlphaFunc(planet, perihelion_updater), run_time=2)
        
        time1_label = Text("Short time - fast motion", font_size=18, color=RED)
        time1_label.to_corner(DR)
        self.play(Write(time1_label))
        
        self.wait(2)
        
        # Now show area near aphelion (far from sun)
        planet.move_to([-a, 0, 0])  # Move to aphelion (leftmost point of ellipse)
        
        # Create larger sector area near aphelion
        start_angle2 = np.pi
        end_angle2 = np.pi + 0.8
        
        sector_points2 = [sun.get_center()]  # Start from sun
        # Add points along the ellipse arc
        for i in range(int(0.8 * 20) + 1):  # More points for smooth curve
            angle = start_angle2 + i * (end_angle2 - start_angle2) / (0.8 * 20)
            x = a * np.cos(angle)
            y = b * np.sin(angle)
            sector_points2.append([x, y, 0])
        
        area2 = Polygon(*sector_points2, color=BLUE, fill_opacity=0.3, stroke_color=BLUE)
        
        # Animate planet moving along this larger arc ON the ellipse
        def aphelion_updater(mob, alpha):
            angle = np.pi + alpha * 0.8  # Larger arc near aphelion
            x = a * np.cos(angle)  # Ellipse centered at origin
            y = b * np.sin(angle)
            mob.move_to([x, y, 0])
        
        self.play(ShowCreation(area2))
        self.play(UpdateFromAlphaFunc(planet, aphelion_updater), run_time=2)
        
        time2_label = Text("Same time - slow motion", font_size=18, color=BLUE)
        time2_label.next_to(time1_label, UP)
        self.play(Write(time2_label))
        
        # Show they're equal
        equal_text = Text("Equal Areas!", font_size=24, color=YELLOW)
        equal_text.to_edge(DOWN)
        self.play(Write(equal_text))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def third_law(self):
        # Law 3 Title
        title = Text("Third Law: T² ∝ a³", font_size=36, color=PURPLE)
        title.to_edge(UP)
        
        desc = Text("Farther planets take longer to orbit", font_size=24)
        desc.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(desc))
        
        # Show sun
        sun = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
        self.play(FadeIn(sun))
        
        # Three orbits with different sizes
        orbit1 = Circle(radius=1.5, color=RED, stroke_width=2)
        orbit2 = Circle(radius=2.5, color=BLUE, stroke_width=2)
        orbit3 = Circle(radius=3.5, color=GREEN, stroke_width=2)
        
        planet1 = Circle(radius=0.1, color=RED, fill_opacity=1)
        planet2 = Circle(radius=0.1, color=BLUE, fill_opacity=1)
        planet3 = Circle(radius=0.1, color=GREEN, fill_opacity=1)
        
        # Position planets
        planet1.move_to([1.5, 0, 0])
        planet2.move_to([2.5, 0, 0])
        planet3.move_to([3.5, 0, 0])
        
        self.play(ShowCreation(orbit1), ShowCreation(orbit2), ShowCreation(orbit3))
        self.play(FadeIn(planet1), FadeIn(planet2), FadeIn(planet3))
        
        # Labels
        inner_label = Text("Fast", font_size=14, color=RED)
        inner_label.next_to(planet1, UP)
        
        middle_label = Text("Medium", font_size=14, color=BLUE)
        middle_label.next_to(planet2, UP)
        
        outer_label = Text("Slow", font_size=14, color=GREEN)
        outer_label.next_to(planet3, UP)
        
        self.play(Write(inner_label), Write(middle_label), Write(outer_label))
        
        # Animate planets with different speeds
        def circular_orbit(planet, radius, speed_factor, label):
            def updater(mob, alpha):
                angle = alpha * 2 * PI * speed_factor
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                mob.move_to([x, y, 0])
                label.next_to(mob, UP, buff=0.1)
            return updater
        
        # Inner planet fastest, outer slowest (realistic ratios)
        self.play(
            UpdateFromAlphaFunc(planet1, circular_orbit(planet1, 1.5, 4, inner_label)),
            UpdateFromAlphaFunc(planet2, circular_orbit(planet2, 2.5, 2, middle_label)),
            UpdateFromAlphaFunc(planet3, circular_orbit(planet3, 3.5, 1, outer_label)),
            run_time=8
        )
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class SimpleKeplersDemo(Scene):
    def construct(self):
        # Summary of all three laws
        title = Text("Kepler's Three Laws Summary", font_size=36, color=GOLD)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Law summaries
        law1 = Text("1. Elliptical Orbits", font_size=24, color=BLUE)
        law2 = Text("2. Equal Areas in Equal Time", font_size=24, color=GREEN) 
        law3 = Text("3. T² ∝ a³", font_size=24, color=PURPLE)
        
        laws = VGroup(law1, law2, law3).arrange(DOWN, buff=0.8)
        laws.to_edge(LEFT)
        
        for law in laws:
            self.play(Write(law))
            self.wait(1)
        
        # Simple demo on the right
        sun = Circle(radius=0.2, color=YELLOW, fill_opacity=1)
        sun.shift(RIGHT * 2)
        
        # Two planets
        planet1 = Circle(radius=0.08, color=RED, fill_opacity=1)
        planet2 = Circle(radius=0.1, color=BLUE, fill_opacity=1)
        
        self.play(FadeIn(sun))
        self.play(FadeIn(planet1), FadeIn(planet2))
        
        # Animate simple orbiting
        def simple_orbit(planet, radius, speed):
            def updater(mob, alpha):
                angle = alpha * 2 * PI * speed
                x = radius * np.cos(angle) + 2  # +2 to center on sun
                y = radius * np.sin(angle)
                mob.move_to([x, y, 0])
            return updater
        
        self.play(
            UpdateFromAlphaFunc(planet1, simple_orbit(planet1, 1.0, 3)),
            UpdateFromAlphaFunc(planet2, simple_orbit(planet2, 1.8, 1.5)),
            run_time=6
        )
        
        final_text = Text("The laws that govern planetary motion", font_size=20, color=YELLOW)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        
        self.wait(3)
