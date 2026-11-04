class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        id_to_pt = []
        pf = set(positive_feedback)
        nf = set(negative_feedback)

        for i in range(len(report)):
            points = 0
            tokenized_report = report[i].split(' ')
            for t in tokenized_report:
                if t in pf:
                    points += 3
                elif t in nf:
                    points -= 1
            
            sid = student_id[i]
            id_to_pt.append((sid, points))
        
        student_ranks = sorted(id_to_pt, key=lambda pair: (-pair[1], pair[0]))
        result = []
        for i in range(k):
            student_id = student_ranks[i][0]
            result.append(student_id)
        
        return result