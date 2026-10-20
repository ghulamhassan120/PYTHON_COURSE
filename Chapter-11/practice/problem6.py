
class Vector:
    def __init__(self, elements):
        self.v = elements
        self.n = len(elements)

    # Overload + operator for vector addition
    def __add__(self, other):
        result = []
        for i in range(self.n):
            result.append(self.v[i] + other.v[i])
        return Vector(result)

    # Overload * operator for dot product
    def __mul__(self, other):
        dot = 0
        for i in range(self.n):
            dot += self.v[i] * other.v[i]
        return dot

    def display(self):
        print(self.v)


# Main program
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

sum_vector = v1 + v2
dot_product = v1 * v2

print("First vector:", end=" ")
v1.display()

print("Second vector:", end=" ")
v2.display()

print("Sum of vectors:", end=" ")
sum_vector.display()

print("Dot product:", dot_product)
