class SparseVector:
    def __init__(self, elements=None):
        if elements is None:
            elements = {}
        if not isinstance(elements, dict):
            raise TypeError("Ошибка типа")
        self.elements = {k: v for k, v in elements.items() if v != 0}

    def __add__(self, other):
        if not isinstance(other, SparseVector):
            raise TypeError("Ошибка типа")

        res = self.elements.copy()
        for i, val in other.elements.items():
            if i in res:
                res[i] += val
                if res[i] == 0:
                    del res[i]
            else:
                res[i] = val
        return SparseVector(res)

    def __sub__(self, other):
        if not isinstance(other, SparseVector):
            raise TypeError("Ошибка типа")

        res = self.elements.copy()
        for i, val in other.elements.items():
            if i in res:
                res[i] -= val
                if res[i] == 0:
                    del res[i]
            else:
                res[i] = -val
        return SparseVector(res)

    def dot(self, other):
        if not isinstance(other, SparseVector):
            raise TypeError("Ошибка типа")
        result = 0
        common_indices = set(self.elements.keys()) & set(other.elements.keys())
        for idx in common_indices:
            result += self.elements[idx] * other.elements[idx]
        return result

    def __repr__(self):
        return f"SparseVector({self.elements})"

    def validate_indices(self):
        if not all(isinstance(idx, int) and idx >= 0 for idx in self.elements):
            raise ValueError("индексы неотрицательные целые числа")

if __name__ == "__main__":
    v1 = SparseVector({1: 3, 3: 5, 10: 2})
    v1.validate_indices()
    v2 = SparseVector({3: -5, 5: 7})
    v2.validate_indices()

    print("Вектор1:", v1)
    print("Вектор2:", v2)
    print("Вектор1+Вектор2:", v1 + v2)
    print("Вектор1-Вектор2:", v1 - v2)
    print("Скалярное произведение Вектор1 на Вектор2:", v1.dot(v2))

    v3 = SparseVector({})
    v4 = SparseVector({2: 4, 4: 6, 8: 0})
    v4.validate_indices()
    print("Вектор3:", v3)
    print("Вектор4:", v4)
    print("Вектор3+Вектор4:", v3 + v4)
    print("Скалярное произведение:", v1.dot(v3))
