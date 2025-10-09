// Last updated: 10/8/2025, 9:49:50 PM
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        HashMap<Character,Integer> hs2=new HashMap<>();
        char[] arr2=stones.toCharArray();
        for(char item :arr2){
            hs2.put(item, hs2.getOrDefault(item,0)+1);
        }

        char[] arr=jewels.toCharArray();
        int count=0;
        for(char key :arr){
            if(hs2.containsKey(key)){
                count+=hs2.get(key);
                }
        }
        return count;
    }
}