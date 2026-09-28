"""Example demonstrating Butterworth IIR filtering."""
from client import ButterworthFilter

def main():
    bf = ButterworthFilter(cutoff_ratio=0.1)
    sig = [1.0] * 10
    filtered = [bf.filter_sample(s) for s in sig]
    print("Step Response of Butterworth Filter:", filtered)

if __name__ == "__main__":
    main()
