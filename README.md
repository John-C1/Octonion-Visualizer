# Octonion Visualizer

A computational and visual exploration of the **octonions** — an 8-dimensional number system
with remarkable algebraic structure and surprising connections to modern mathematics.

> *"The real numbers are the dependable breadwinner of the
> family, the complete ordered field we all rely on. The complex numbers are a slightly flashier but
> still respectable younger brother: not ordered, but algebraically complete. The quaternions, being
> noncommutative, are the eccentric cousin who is shunned at important family gatherings. But the
> octonions are the crazy old uncle nobody lets out of the attic: they are nonassociative."*
> ~ John C. Baez, 'The Octonions'

---

## What Are Octonions?

The octonions (𝕆) are an 8-dimensional normed division algebra, the last in a sequence built
from the reals by the **Cayley-Dickson construction**: ℝ → ℂ → ℍ → 𝕆. Each doubling
sacrifices an algebraic property:

| Algebra | Dimension | Commutative? | Associative? |
|---------|-----------|--------------|--------------|
| ℝ (Reals) | 1 | ✓ | ✓ |
| ℂ (Complex) | 2 | ✓ | ✓ |
| ℍ (Quaternions) | 4 | ✗ | ✓ |
| 𝕆 (Octonions) | 8 | ✗ | ✗ |

Despite losing associativity — meaning `(i·j)·k ≠ i·(j·k)` in general — the octonions
possess deep symmetry and appear unexpectedly in areas ranging from string theory to the
exceptional Lie groups.

---

## Project Structure

```
.
├── algebra.py           # Core octonion arithmetic via Cayley-Dickson construction
├── cayley_integers.py   # Cayley integer generator and E₈ lattice interface
├── factoring.py         # Rehm's Algorithm for factoring primitive octonions
└── animations.py        # Visualizations of algebraic properties and symmetry
```

### `algebra.py`
A fully functional octonion calculator. Implements multiplication using the
Cayley-Dickson construction, along with conjugation, norm, and other core operations.

### `cayley_integers.py`
Generates the **Cayley integers**, the natural "integer" analog of the octonions.
These 240 unit elements are deeply tied to the **E₈ root lattice** — one of the most
remarkable objects in mathematics. This module provides a computational bridge between
octonions and E₈ lattice points, enabling seamless conversion between the two representations.

### `factoring.py`
Implements **Rehm's Algorithm**, which factors primitive octonions into 2 sets of 240 octonions.
Notably, the algorithm works correctly even in the absence of associativity, by carefully
controlling the order of multiplication at each step.

### `animations.py`
The visual centerpiece of the project. Uses the above modules to produce three animations:

- **Non-commutativity & non-associativity** — demonstrates how octonion multiplication
  depends on the order and grouping of operands
- **The 240 unit Cayley integers** — visualizes the stunning symmetry of the unit sphere
  in 𝕆, projected into lower dimensions
- **Rehm's factorization** — shows how the two sets of 240 prime factors of a primitive
  octonion exhibit the same E₈ symmetry as the Cayley integers themselves

---

## Getting Started

### Prerequisites
```bash
pip install numpy, manim
```

### Generating Animations
```bash
manim -pql animations.py <animation_class_name>
```

---

## Mathematical Background

The **Cayley integers** are the largest subalgebra of 𝕆 satisfying the norm-integrality
criterion: every element has an integer squared norm. Their 240 unit elements correspond
exactly to the minimal vectors of the **E₈ lattice**, which achieves the densest known
sphere packing in 8 dimensions (proven optimal in 2016 by Maryna Viazovska).

The **triality** of the octonions — a 3-fold symmetry of the rotation group SO(8) unique
to 8 dimensions — is also directly tied to the algebraic structure implemented here. It
arises from the D₄ Dynkin diagram, the only root system with S₃ symmetry.

---

## Authors

John Calame and Yukun Du

---

## References

- John C. Baez, *The Octonions*
- John H. Conway & Derek A. Smith, *On Quaternions and Octonions*
