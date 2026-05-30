import bisect

class Solution(object):
    # use a segment tree because looking at 
    #objects and distances between them. 
    def getResults(self, queries):
        # first get max possible x to size segment tree dynamically
        #this would be maximum of the x's in queries, plus 1 to account for 0
        max_x = max(q[1] for q in queries) + 1
        
        # setup segment tree array, which is 2*N because
        #of the binary structure
        tree = [0] * (2 * max_x)
        
        def update(i, val):
            #update max gap ending at i
            i += max_x
            tree[i] = val
            while i > 1:
                i //= 2
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                
        def query_max(left, right):
            #return max gap betw coordinates [left, right)
            left += max_x
            right += max_x
            res = 0
            while left < right:
                if left % 2 == 1:
                    res = max(res, tree[left])
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    res = max(res, tree[right])
                left //= 2
                right //= 2
            return res

        # number line always starts w obstacle at 0
        obstacles = [0]
        ans = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # find where new obstacle is in sorted list
                idx = bisect.bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]
                
                # insert new obstacle
                obstacles.insert(idx, x)
                
                # gap ending at new obstacle= x - prev_obs
                update(x, x - prev_obs)
                
                # if obstacle AFTER x, gap shrank bc we dropped a wall!!
                if idx + 1 < len(obstacles):
                    next_obs = obstacles[idx + 1]
                    update(next_obs, next_obs - x)
                    
            else:
                x, sz = q[1], q[2]
                
                # get last obstacle appearing BEFORE or AT our boundary x
                idx = bisect.bisect_right(obstacles, x) - 1
                last_obs = obstacles[idx]
                
                # maximum gap is either:
                # 1. max fully-formed gap ending at or before last_obs
                # 2. partial gap from the last_obs to our boundary x
                max_gap = max(query_max(0, last_obs + 1), x - last_obs)
                
                # append answers for type 2 queries!!
                ans.append(max_gap >= sz)
                
        return ans