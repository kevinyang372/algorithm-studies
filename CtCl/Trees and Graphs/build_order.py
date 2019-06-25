# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project'sdependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c

import collections

def build_order(projects, dependencies):

    if not dependencies: return projects

    require_dependency = collections.defaultdict(list)
    with_dependencies = []

    for i in dependencies:
        require_dependency[i[1]].append(i[0])
        with_dependencies.append(i[1])

    stack = [i for i in projects if i not in with_dependencies]
    res = []

    while require_dependency:
        temp = []
        for t in stack:
            clear = []
            for k, v in require_dependency.items():
                if t in v:
                    v.remove(t)
                    if not v:
                        temp.append(k)

            for k in temp:
                require_dependency.pop(k)

        if not temp:
            return False

        res += stack
        stack = temp

    res += stack

    return res



