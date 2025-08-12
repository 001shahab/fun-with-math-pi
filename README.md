# π Visualization Suite - The Magic of Mathematics

**Author:** Prof. Shahab Anbarjafari  
**Copyright:** (c) 2025 - 3S Holding OÜ  
**License:** MIT License

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.7.1-green.svg)
![NumPy](https://img.shields.io/badge/numpy-1.24.3-orange.svg)

## 🌟 Overview

This interactive visualization suite demonstrates the fascinating emergence of π (pi) through six different mathematical methods simultaneously. It creates a stunning visual experience that showcases how this fundamental constant appears across various branches of mathematics - from geometry to probability theory to infinite series.

## 🎯 Features

### Six Simultaneous π Calculation Methods:

1. **Monte Carlo Method** - Statistical approach using random sampling
2. **π Circle Pattern** - Overlapping circles creating geometric patterns
3. **Archimedes Polygon Method** - Classical geometric approximation
4. **Buffon's Needle Problem** - Probability-based calculation
5. **π Cardioid Pattern** - Geometric pattern visualization (n=314)
6. **π Digits Spiral** - Artistic visualization of π's decimal expansion

### Visual Design:
- Light blue background for a calming, educational atmosphere
- Dark color scheme for better contrast and readability
- Smooth animations with interactive pause/resume functionality
- **Continuous animations**: Both circle and cardioid patterns loop infinitely, showing the emergence of patterns over time

## 📋 Requirements

- Python 3.8 or higher
- NumPy 1.24.3
- Matplotlib 3.7.1
- SciPy 1.10.1 (optional, for enhanced calculations)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pi-visualization.git
cd pi-visualization
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the visualization:
```bash
python pi_visualization.py
```

### Controls:
- **Pause/Resume Button**: Click to pause or resume all animations
- **Close**: Use the window's close button or press 'Q' to exit

## 🔬 Mathematical Methods Explained

### 1. Monte Carlo Method
- **Principle**: Randomly throws points in a square with an inscribed circle
- **Formula**: π ≈ 4 × (points inside circle) / (total points)
- **Visualization**: Dark blue dots (inside), Dark red dots (outside)

### 2. π Circle Pattern
- **Concept**: Multiple overlapping circles arranged in a circular pattern
- **Animation**: Circles appear one by one, creating a flower-like pattern
- **Geometry**: 20 circles of radius 1, centers placed on a circle of radius 1
- **Pattern**: Creates a mandala-like design that relates to π through circle geometry
- **Visualization**: Dark green circles appearing sequentially, then resetting for continuous animation

### 3. Archimedes Polygon Method
- **Principle**: Approximates a circle using regular polygons
- **Process**: As polygon sides increase, perimeter approaches 2π
- **Visualization**: Dark golden polygon inscribed in a circle

### 4. Buffon's Needle Problem
- **Setup**: Drop needles on parallel lines spaced 1 unit apart
- **Probability**: P(crossing) = 2/(π) for needle length = 1
- **Formula**: π ≈ 2 × (total needles) / (crossing needles)
- **Visualization**: Dark magenta (crossing), Dark gray (not crossing)

### 5. π Cardioid Pattern
- **Concept**: Creates a cardioid/spirograph pattern using modular arithmetic
- **Animation**: Lines are drawn one by one, showing the pattern emerge
- **Method**: Connects points on a circle where each point i connects to point 2i mod n
- **Pattern**: With n=314 points, creates a beautiful heart-shaped curve
- **Visualization**: Dark red lines appearing sequentially, creating an intricate geometric pattern that loops infinitely

### 6. π Digits Spiral
- **Concept**: First 100 digits of π arranged in a spiral
- **Color Coding**: Each digit (0-9) has a unique color from the viridis colormap
- **Size**: Digit value determines point size

## 🎨 Customization

You can modify various parameters in the code:

```python
# In pi_visualization.py

# Change figure size
self.fig = plt.figure(figsize=(16, 10), facecolor='lightblue')

# Adjust animation speed
anim = animation.FuncAnimation(self.fig, self.animate, interval=50)

# Modify number of points per frame (Monte Carlo)
for _ in range(10):  # Change 10 to adjust speed

# Change color schemes
circle = Circle((0, 0), 1, fill=False, color='darkblue', linewidth=2)

# Adjust cardioid pattern points
self.cardioid_n = 314  # Change to create different patterns
```

## 📊 Performance Tips

1. **Reduce Points**: For slower systems, reduce the number of points added per frame
2. **Adjust Interval**: Increase animation interval for smoother performance
3. **Limit Needles**: Set a maximum number of needles in Buffon's method

## 🐛 Troubleshooting

### Common Issues:

1. **ImportError**: Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. **Slow Performance**: 
   - Close other applications
   - Reduce figure size in the code
   - Increase animation interval

3. **Display Issues**:
   - Update matplotlib: `pip install matplotlib --upgrade`
   - Check your display backend: `python -c "import matplotlib; print(matplotlib.get_backend())"`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Educational Use

This visualization is perfect for:
- Mathematics education
- Programming workshops
- Scientific visualization courses
- Demonstrating Monte Carlo methods
- Teaching infinite series convergence
- Exploring probability theory

## 🔗 Additional Resources

- [History of π](https://en.wikipedia.org/wiki/Pi)
- [Monte Carlo Methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Buffon's Needle](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 - 3S Holding OÜ
Author: Prof. Shahab Anbarjafari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- Inspired by the beauty of mathematics and the mysterious nature of π
- Thanks to the matplotlib community for excellent visualization tools
- Special recognition to historical mathematicians who discovered these methods

---

**Enjoy exploring the magic of π!** 🎉

For questions or collaboration: shb@3sholding.com