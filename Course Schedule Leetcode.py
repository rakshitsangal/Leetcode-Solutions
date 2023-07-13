class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort
        alist = collections.defaultdict(list)
        order = [0]*numCourses
        for i,j in prerequisites:
            alist[j].append(i)
            order[i]+=1
        q = collections.deque()
        for i in range(len(order)):
            if order[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            current = q.popleft()
            count+=1
            for i in alist[current]:
                order[i]-=1
                if order[i]==0:
                    q.append(i)
        
        return count == numCourses
