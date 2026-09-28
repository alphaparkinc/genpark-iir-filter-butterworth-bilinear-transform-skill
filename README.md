# Butterworth IIR Filter Skill

Second-order maximally flat magnitude low-pass Infinite Impulse Response (IIR) filter designed using the Bilinear Transform.

```mermaid
flowchart TD
    Cutoff["Cutoff Frequency Ratio (0..1)"] --> Prewarp["Prewarp Angular Frequency: tan(π f_c / 2)"]
    Prewarp --> Bilinear["Bilinear Transform s = 2/T * (z-1)/(z+1)"]
    Bilinear --> Coeffs["Difference Equation Direct Form II: y[n] = ∑ b_k x[n-k] - ∑ a_k y[n-k]"]
    Coeffs --> Filtered["Low-Pass Clean Output Stream"]
```

## Features
- **100% Python Standard Library**: Pure difference equation direct form evaluation.
- **Maximally Flat Passband**: No passband ripples (unlike Chebyshev or Elliptic filters).
