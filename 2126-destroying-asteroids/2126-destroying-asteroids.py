class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()

        for m in asteroids:
            if mass < m:
                return False
            elif mass >= 1e5:
                return True
            else:
                mass += m
        return True