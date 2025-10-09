# Last updated: 10/8/2025, 9:49:29 PM
class TimeMap:

    def __init__(self):
        self.hash=defaultdict(list)



    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((timestamp,value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        val=self.hash.get(key,[])
        l=0
        r=len(val)-1
        ans=""
        while l<=r:
            m=(l+r)//2

            if val[m][0]>timestamp:
                r=m-1
            else:
                ans=val[m][1]
                l=m+1
        return ans
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)