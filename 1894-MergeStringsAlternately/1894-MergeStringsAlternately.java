// Last updated: 10/8/2025, 9:48:45 PM
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res=new StringBuilder();
        for(int i=0;i<word1.length()||i<word2.length();i++){
            if(i<word1.length())
            {
                res.append(word1.charAt(i));
            }
            if(i<word2.length()){
                res.append(word2.charAt(i));
            }
        }
        return res.toString();
    }
}