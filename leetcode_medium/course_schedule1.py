class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        # 1. graph 만들기
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        # 0 = 방문 안 함
        # 1 = 현재 DFS 경로에서 탐색 중
        # 2 = 탐색 완전히 끝남
        state = [0] * numCourses

        def dfs(course):
            # 현재 경로에서 다시 만남 → cycle
            if state[course] == 1:
                return False

            # 이미 검증 끝난 course
            if state[course] == 2:
                return True

            # 현재 DFS 경로에 들어옴
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # 이 course부터 시작하는 경로는 문제 없음
            state[course] = 2
            return True

        # graph가 여러 덩어리일 수도 있으니 모든 course 확인
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
