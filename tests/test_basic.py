from pybind11_union_find import UnionFind as PybindUnionFind
from pybind11_union_find import PythonUnionFind


def test_main():
    assert m.__version__ == "0.0.1"


for UnionFind in [PythonUnionFind, PybindUnionFind]:
    uf = UnionFind(5)
    uf.union(0, 2)
    uf.union(1, 3)
    uf.union(2, 4)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 0
    assert uf.find(3) == 1
    assert uf.find(4) == 0
    groups = uf.groups()
    assert groups == [[0, 2, 4], [1, 3]]


print()