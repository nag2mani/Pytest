Here's the solution and explanation for the given problem. We'll use Python to compute the roots of the quadratic equation \(ax^2 + bx + c = 0\), taking into account both real and complex roots.

### Steps to Solve:
1. **Understanding the Quadratic Formula**:
   The roots of a quadratic equation are given by:
   \[
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   \]
   Here, \(b^2 - 4ac\) is called the discriminant (\(D\)).

2. **Handling Complex Roots**:
   If \(D < 0\), the square root of the discriminant becomes imaginary. To avoid explicitly taking the square root of a negative number, we split the computation into real and imaginary parts:
   - Real part: \(-\frac{b}{2a}\)
   - Imaginary part: \(\frac{\sqrt{|D|}}{2a}\)

3. **Output Format**:
   - If the roots are real, the output should be \([(real1, 0), (real2, 0)]\).
   - If the roots are complex, the output should be \([(real, imag), (real, -imag)]\).

4. **Implementation**:
   Using the above logic, we can write the Python function.

### Code Implementation:
```python
import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    real_part = -b / (2 * a)  # Real part of the roots

    if discriminant >= 0:
        # Roots are real
        root1 = real_part + math.sqrt(discriminant) / (2 * a)
        root2 = real_part - math.sqrt(discriminant) / (2 * a)
        return [(root1, 0), (root2, 0)]
    else:
        # Roots are complex
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return [(real_part, imaginary_part), (real_part, -imaginary_part)]

# Example usage
a, b, c = 1, -2, 5  # Coefficients for the equation x^2 - 2x + 5 = 0
roots = solve_quadratic(a, b, c)
print("Roots:", roots)
```

### Explanation:
1. **Discriminant Calculation**:
   The discriminant (\(D\)) determines if the roots are real or complex:
   - \(D > 0\): Two distinct real roots.
   - \(D = 0\): One real root (repeated).
   - \(D < 0\): Two complex conjugate roots.

2. **Handling Complex Roots**:
   When \(D < 0\), we calculate the imaginary part using \(\sqrt{-D}\).

3. **Formatting the Output**:
   Roots are returned as a list of tuples, ensuring compliance with the required format.

### Example:
For \(a = 1, b = -2, c = 5\):
- \(D = (-2)^2 - 4(1)(5) = 4 - 20 = -16\)
- Real part: \(-(-2) / 2(1) = 1\)
- Imaginary part: \(\sqrt{16} / 2 = 2\)
- Roots: \([(1, 2), (1, -2)]\)

### Output:
```
Roots: [(1, 2), (1, -2)]
```

This approach avoids taking the square root of a negative number directly, ensuring correctness for both real and complex roots.
