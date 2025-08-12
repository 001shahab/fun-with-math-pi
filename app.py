import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.widgets import Button, Slider
import random

class PiVisualization:
    def __init__(self):
        self.fig = plt.figure(figsize=(16, 10), facecolor='lightblue')
        self.fig.suptitle('The Magic of π - Interactive Visualization', 
                          fontsize=20, color='darkblue', fontweight='bold')
        
        # Create subplots for different methods
        self.ax1 = plt.subplot(2, 3, 1, facecolor='lightblue')
        self.ax2 = plt.subplot(2, 3, 2, facecolor='lightblue')
        self.ax3 = plt.subplot(2, 3, 3, facecolor='lightblue')
        self.ax4 = plt.subplot(2, 3, 4, facecolor='lightblue')
        self.ax5 = plt.subplot(2, 3, 5, facecolor='lightblue')
        self.ax6 = plt.subplot(2, 3, 6, facecolor='lightblue')
        
        # Initialize methods
        self.setup_monte_carlo()
        self.setup_circle_pattern()
        self.setup_archimedes()
        self.setup_buffon_needle()
        self.setup_pi_cardioid()
        self.setup_spiral()
        
        # Animation control
        self.paused = False
        self.setup_controls()
        
    def setup_monte_carlo(self):
        """Monte Carlo method - throwing darts"""
        self.ax1.set_xlim(-1.1, 1.1)
        self.ax1.set_ylim(-1.1, 1.1)
        self.ax1.set_aspect('equal')
        self.ax1.set_title('Monte Carlo Method', color='darkblue', fontsize=12)
        
        # Draw circle and square
        circle = Circle((0, 0), 1, fill=False, color='darkblue', linewidth=2)
        square = Rectangle((-1, -1), 2, 2, fill=False, color='black', linewidth=2)
        self.ax1.add_patch(circle)
        self.ax1.add_patch(square)
        
        self.monte_carlo_points = {'inside': [], 'outside': []}
        self.monte_carlo_text = self.ax1.text(0, -1.3, '', ha='center', 
                                              color='darkblue', fontsize=10)
        
    def setup_circle_pattern(self):
        """Circle pattern visualization - overlapping circles forming a flower"""
        self.ax2.set_xlim(-2.5, 2.5)
        self.ax2.set_ylim(-2.5, 2.5)
        self.ax2.set_aspect('equal')
        self.ax2.set_title('π Circle Pattern (n = 314)', 
                          color='darkgreen', fontsize=12)
        
        # Draw outer circle
        outer_circle = Circle((0, 0), 2, fill=False, color='darkgray', 
                            linewidth=1, alpha=0.5)
        self.ax2.add_patch(outer_circle)
        
        # Initialize pattern parameters
        self.circle_pattern_index = 0
        self.n_circles = 20  # Number of circles in the pattern
        self.circle_patches = []
        
    def setup_archimedes(self):
        """Archimedes polygon method"""
        self.ax3.set_xlim(-1.2, 1.2)
        self.ax3.set_ylim(-1.2, 1.2)
        self.ax3.set_aspect('equal')
        self.ax3.set_title('Archimedes Polygon Method', color='darkgoldenrod', fontsize=12)
        
        circle = Circle((0, 0), 1, fill=False, color='darkgoldenrod', linewidth=2)
        self.ax3.add_patch(circle)
        
        self.archimedes_n = 3
        self.archimedes_polygon = None
        self.archimedes_text = self.ax3.text(0, -1.4, '', ha='center', 
                                            color='darkblue', fontsize=10)
        
    def setup_buffon_needle(self):
        """Buffon's needle problem"""
        self.ax4.set_xlim(0, 10)
        self.ax4.set_ylim(0, 10)
        self.ax4.set_title("Buffon's Needle Problem", color='darkmagenta', fontsize=12)
        
        # Draw parallel lines
        for i in range(11):
            self.ax4.axvline(x=i, color='gray', alpha=0.5)
        
        self.buffon_needles = []
        self.buffon_crosses = 0
        self.buffon_total = 0
        self.buffon_text = self.ax4.text(5, -0.5, '', ha='center', 
                                        color='darkblue', fontsize=10)
        
    def setup_pi_cardioid(self):
        """Pi Cardioid/Spirograph visualization"""
        self.ax5.set_xlim(-2.5, 2.5)
        self.ax5.set_ylim(-2.5, 2.5)
        self.ax5.set_aspect('equal')
        self.ax5.set_title('π Cardioid Pattern (n = 314 points)', 
                          color='darkred', fontsize=12)
        
        # Initialize cardioid parameters
        self.cardioid_n = 314  # Number of points as shown in the image
        self.cardioid_lines = []
        self.cardioid_index = 0
        self.cardioid_multiplier = 2  # For cardioid pattern
        
        # Draw base circle
        circle = Circle((0, 0), 2, fill=False, color='darkgray', linewidth=1, alpha=0.3)
        self.ax5.add_patch(circle)
        
        # Add points on circle
        angles = np.linspace(0, 2*np.pi, self.cardioid_n, endpoint=False)
        x_points = 2 * np.cos(angles)
        y_points = 2 * np.sin(angles)
        self.ax5.scatter(x_points, y_points, s=1, color='darkred', alpha=0.3)
        
    def setup_spiral(self):
        """Spiral visualization of π digits"""
        self.ax6.set_xlim(-2, 2)
        self.ax6.set_ylim(-2, 2)
        self.ax6.set_aspect('equal')
        self.ax6.set_title('π Digits Spiral', color='darkviolet', fontsize=12)
        
        # π digits (first 100)
        self.pi_digits = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        self.spiral_points = []
        
    def setup_controls(self):
        """Setup animation controls"""
        # Add pause button
        self.pause_ax = plt.axes([0.45, 0.02, 0.1, 0.03])
        self.pause_btn = Button(self.pause_ax, 'Pause', color='gray')
        self.pause_btn.on_clicked(self.toggle_pause)
        
    def toggle_pause(self, event):
        self.paused = not self.paused
        self.pause_btn.label.set_text('Resume' if self.paused else 'Pause')
        
    def update_monte_carlo(self, frame):
        """Update Monte Carlo visualization"""
        if not self.paused and frame % 2 == 0:  # Update every 2 frames
            for _ in range(10):  # Add 10 points per update
                x, y = random.uniform(-1, 1), random.uniform(-1, 1)
                if x**2 + y**2 <= 1:
                    self.monte_carlo_points['inside'].append((x, y))
                    self.ax1.plot(x, y, 'o', color='darkblue', markersize=2, alpha=0.6)
                else:
                    self.monte_carlo_points['outside'].append((x, y))
                    self.ax1.plot(x, y, 'o', color='darkred', markersize=2, alpha=0.6)
            
            inside = len(self.monte_carlo_points['inside'])
            total = inside + len(self.monte_carlo_points['outside'])
            if total > 0:
                pi_estimate = 4 * inside / total
                self.monte_carlo_text.set_text(f'π ≈ {pi_estimate:.6f} ({total} points)')
    
    def update_circle_pattern(self, frame):
        """Update circle pattern - creates overlapping circles iteratively"""
        if not self.paused and frame % 10 == 0:  # Update every 10 frames
            # Add next circle
            if self.circle_pattern_index < self.n_circles:
                angle = 2 * np.pi * self.circle_pattern_index / self.n_circles
                
                # Position for circle center on the main circle
                cx = np.cos(angle)
                cy = np.sin(angle)
                
                # Draw circle with animation
                circle = Circle((cx, cy), 1, fill=False, 
                              color='darkgreen', linewidth=0.8, 
                              alpha=0.6 - 0.3 * (self.circle_pattern_index / self.n_circles))
                self.ax2.add_patch(circle)
                self.circle_patches.append(circle)
                
                self.circle_pattern_index += 1
            
            # After all circles are drawn, add central decorative circles
            elif self.circle_pattern_index == self.n_circles:
                for r in [0.3, 0.5, 0.7]:
                    center_circle = Circle((0, 0), r, fill=False, 
                                         color='darkgreen', linewidth=0.5, alpha=0.4)
                    self.ax2.add_patch(center_circle)
                self.circle_pattern_index += 1
                
                # Add text
                self.ax2.text(0, -2.3, 'Overlapping circles create patterns related to π', 
                             ha='center', color='darkgreen', fontsize=10, style='italic')
            
            # Reset and clear to restart animation
            elif self.circle_pattern_index > self.n_circles + 30:  # Wait 30 frames before reset
                # Remove all circles
                for circle in self.circle_patches:
                    circle.remove()
                self.circle_patches = []
                
                # Clear and reset
                self.ax2.clear()
                self.ax2.set_xlim(-2.5, 2.5)
                self.ax2.set_ylim(-2.5, 2.5)
                self.ax2.set_aspect('equal')
                self.ax2.set_title('π Circle Pattern (n = 314)', 
                                  color='darkgreen', fontsize=12)
                self.ax2.set_facecolor('lightblue')
                
                # Redraw outer circle
                outer_circle = Circle((0, 0), 2, fill=False, color='darkgray', 
                                    linewidth=1, alpha=0.5)
                self.ax2.add_patch(outer_circle)
                
                self.circle_pattern_index = 0
            else:
                self.circle_pattern_index += 1
            
    def update_archimedes(self, frame):
        """Update Archimedes polygon"""
        if not self.paused and frame % 30 == 0:  # Update every 30 frames
            if self.archimedes_polygon:
                self.archimedes_polygon.remove()
            
            # Create regular polygon
            angles = np.linspace(0, 2*np.pi, self.archimedes_n + 1)
            vertices = [(np.cos(a), np.sin(a)) for a in angles]
            self.archimedes_polygon = Polygon(vertices, fill=False, 
                                            edgecolor='darkgoldenrod', linewidth=2)
            self.ax3.add_patch(self.archimedes_polygon)
            
            # Calculate perimeter
            perimeter = self.archimedes_n * 2 * np.sin(np.pi / self.archimedes_n)
            pi_estimate = perimeter / 2
            self.archimedes_text.set_text(f'n = {self.archimedes_n}, π ≈ {pi_estimate:.6f}')
            
            # Increase polygon sides
            self.archimedes_n = min(self.archimedes_n + 1, 50)
            if self.archimedes_n >= 50:
                self.archimedes_n = 3  # Reset
    
    def update_buffon(self, frame):
        """Update Buffon's needle"""
        if not self.paused and frame % 3 == 0:  # Update every 3 frames
            # Clear old needles if too many
            if len(self.buffon_needles) > 200:
                for needle in self.buffon_needles[:50]:
                    needle.remove()
                self.buffon_needles = self.buffon_needles[50:]
            
            # Drop a needle
            x = random.uniform(0.5, 9.5)
            y = random.uniform(0.5, 9.5)
            angle = random.uniform(0, np.pi)
            
            # Needle endpoints (length = 1)
            x1 = x - 0.5 * np.cos(angle)
            x2 = x + 0.5 * np.cos(angle)
            y1 = y - 0.5 * np.sin(angle)
            y2 = y + 0.5 * np.sin(angle)
            
            # Check if needle crosses a line
            crosses = (int(x1) != int(x2))
            color = 'darkmagenta' if crosses else 'darkgray'
            
            needle, = self.ax4.plot([x1, x2], [y1, y2], color=color, 
                                   linewidth=1, alpha=0.6)
            self.buffon_needles.append(needle)
            
            self.buffon_total += 1
            if crosses:
                self.buffon_crosses += 1
            
            if self.buffon_crosses > 0:
                pi_estimate = 2 * self.buffon_total / self.buffon_crosses
                self.buffon_text.set_text(f'π ≈ {pi_estimate:.6f} ({self.buffon_total} needles)')
    
    def update_pi_cardioid(self, frame):
        """Update Pi Cardioid/Spirograph pattern - animate line by line"""
        if not self.paused and frame % 2 == 0:  # Update every 2 frames
            # Add next line
            if self.cardioid_index < self.cardioid_n:
                i = self.cardioid_index
                
                # Calculate positions on circle
                angle1 = 2 * np.pi * i / self.cardioid_n
                angle2 = 2 * np.pi * (i * self.cardioid_multiplier) / self.cardioid_n
                
                x1 = 2 * np.cos(angle1)
                y1 = 2 * np.sin(angle1)
                x2 = 2 * np.cos(angle2)
                y2 = 2 * np.sin(angle2)
                
                # Create line with gradient color based on position
                progress = i / self.cardioid_n
                alpha = 0.1 + 0.4 * (1 - progress)
                line, = self.ax5.plot([x1, x2], [y1, y2], 
                                     color='darkred', linewidth=0.3, alpha=alpha)
                self.cardioid_lines.append(line)
                
                self.cardioid_index += 1
            
            # Once complete, wait a bit then clear and restart
            elif self.cardioid_index >= self.cardioid_n + 50:  # Wait 50 frames
                # Remove all lines
                for line in self.cardioid_lines:
                    line.remove()
                self.cardioid_lines = []
                
                # Reset
                self.cardioid_index = 0
                
                # Optionally change multiplier for different patterns
                # self.cardioid_multiplier = 2 + (frame // 1000) % 5  # Changes pattern over time
            else:
                self.cardioid_index += 1
    
    def update_spiral(self, frame):
        """Update spiral visualization"""
        if not self.paused and frame % 5 == 0:
            # Clear and redraw spiral
            self.ax6.clear()
            self.ax6.set_xlim(-2, 2)
            self.ax6.set_ylim(-2, 2)
            self.ax6.set_aspect('equal')
            self.ax6.set_title('π Digits Spiral', color='darkviolet', fontsize=12)
            self.ax6.set_facecolor('lightblue')
            
            # Create spiral points
            n_points = min(frame // 5, len(self.pi_digits))
            theta = np.linspace(0, 4*np.pi, n_points)
            r = np.linspace(0, 1.8, n_points)
            
            for i in range(n_points):
                digit = int(self.pi_digits[i])
                color = plt.cm.viridis(digit / 9)
                size = 20 + digit * 5
                self.ax6.scatter(r[i] * np.cos(theta[i]), 
                               r[i] * np.sin(theta[i]), 
                               c=[color], s=size, alpha=0.8)
                
                if i < 20:  # Show first 20 digits as text
                    self.ax6.text(r[i] * np.cos(theta[i]), 
                                r[i] * np.sin(theta[i]), 
                                str(digit), color='darkblue', 
                                fontsize=8, ha='center', va='center')
    
    def animate(self, frame):
        """Main animation function"""
        self.update_monte_carlo(frame)
        self.update_circle_pattern(frame)
        self.update_archimedes(frame)
        self.update_buffon(frame)
        self.update_pi_cardioid(frame)
        self.update_spiral(frame)
        
        # Set light blue background for all axes
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6]:
            ax.set_facecolor('lightblue')
            ax.tick_params(colors='darkblue')
            for spine in ax.spines.values():
                spine.set_color('darkblue')
        
        return []
    
    def run(self):
        """Run the animation"""
        anim = animation.FuncAnimation(self.fig, self.animate, 
                                     interval=50, blit=False)
        plt.tight_layout()
        plt.show()
        return anim

# Create and run the visualization
if __name__ == "__main__":
    viz = PiVisualization()
    anim = viz.run()