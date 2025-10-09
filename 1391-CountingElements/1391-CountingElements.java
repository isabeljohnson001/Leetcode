// Last updated: 10/8/2025, 9:49:12 PM
class Solution {
    public int countElements(int[] arr) {
        Set<Integer> hs=new HashSet<>();
        for(int x :arr){
            hs.add(x);
        }
        int count=0;
        for(int x:arr){
            if(hs.contains(x+1)){
                count++;
            }
        }
        return count;
    }
}