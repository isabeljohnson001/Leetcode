class Solution {
    public int lengthOfLongestSubstring(String s) {
         HashMap<Character,Integer> hs=new HashMap<>();
        int left=0;
        int right=0;
        int ans=0;
        while(right<s.length()){
            char r=s.charAt(right);
            hs.put(r,hs.getOrDefault(r,0)+1);
            while(hs.get(r)>1){
                char l=s.charAt(left);
                hs.put(l,hs.get(l)-1);
                left++;
            }
            ans=Math.max(right-left+1,ans);

            right++;
        }

        return ans;
    }
}