class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        order = []

        def dfs(course):

            nonlocal order

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]
