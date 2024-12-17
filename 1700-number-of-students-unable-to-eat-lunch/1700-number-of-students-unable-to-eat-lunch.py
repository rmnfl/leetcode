from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_stack = deque(sandwiches)
        student_queue = deque(students)

        cnt_served = 0

        while cnt_served < len(student_queue) and (sandwich_stack or student_queue):
            if sandwich_stack[0] == student_queue[0]:
                sandwich_stack.popleft()
                student_queue.popleft()
                cnt_served = 0
            else:
                student_queue.rotate(-1)
                cnt_served += 1

        return len(student_queue)