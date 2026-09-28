"""Butterworth IIR Filter via Bilinear Transform.
100% Python Standard Library.
"""

import math

class ButterworthFilter:
    """Second-order Butterworth IIR low-pass filter."""
    def __init__(self, cutoff_ratio=0.2):
        wc = math.tan(math.pi * cutoff_ratio / 2.0)
        k = math.sqrt(2.0) * wc
        wc2 = wc**2
        norm = 1.0 + k + wc2
        self.b0 = wc2 / norm
        self.b1 = 2.0 * self.b0
        self.b2 = self.b0
        self.a1 = 2.0 * (wc2 - 1.0) / norm
        self.a2 = (1.0 - k + wc2) / norm
        self.x1, self.x2 = 0.0, 0.0
        self.y1, self.y2 = 0.0, 0.0

    def filter_sample(self, x):
        y = self.b0 * x + self.b1 * self.x1 + self.b2 * self.x2 - self.a1 * self.y1 - self.a2 * self.y2
        self.x2, self.x1 = self.x1, x
        self.y2, self.y1 = self.y1, y
        return round(y, 5)
