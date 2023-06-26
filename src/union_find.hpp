#pragma once

#include <vector>

struct UnionFind {
    UnionFind(int n) {

    }

    int find(int x) {
        return x;
    }

    void _union(int x, int y) {
    }

    std::vector<std::vector<int>> groups() const {
    }

    std::vector<int> group_of(int x) const {
    }

    private:
    mutable std::vector<int> parent;
    mutable std::vector<int> rank;
};