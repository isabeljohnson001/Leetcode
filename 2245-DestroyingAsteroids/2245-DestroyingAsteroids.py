# Last updated: 10/8/2025, 9:48:00 PM
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if asteroid>mass:
                return False
            mass+=asteroid
        return True
        