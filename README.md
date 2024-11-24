### Steps to Solve:
![image](https://github.com/user-attachments/assets/2b5a0379-59d1-4d99-b097-3c5832bfab5b)

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
