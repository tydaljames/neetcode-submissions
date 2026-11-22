class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def takeCourse(course):
            for blockedCourse in noPrereqs[course]:
                prereqs[blockedCourse].remove(course)
                if not prereqs[blockedCourse]:
                    prereqs.pop(blockedCourse)
                    noPrereqs[blockedCourse] = reverseMap[blockedCourse]

            noPrereqs.pop(course)

        prereqs = defaultdict(set)
        reverseMap = defaultdict(set)
        noPrereqs = defaultdict(set)

        for p in prerequisites:
            course = p[0]
            prereq = p[1]

            prereqs[course].add(prereq)
            reverseMap[prereq].add(course)

        for num in range(numCourses):
            if num not in prereqs:
                if num in reverseMap:
                    noPrereqs[num] = reverseMap[num]
                else:
                    noPrereqs[num] = set()

       
        while noPrereqs:
            course = next(iter(noPrereqs))
            takeCourse(course)


        return not prereqs

    # Approaches:
    # 1. Map courses to prereqs. Find all courses with no prereqs. Take those courses and update the rest. Repeat
    # 2. Map prereqs to courses. 