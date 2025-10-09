// Last updated: 10/8/2025, 9:49:15 PM
class Solution {
    public int maxNumberOfBalloons(String text) {
        int n=text.length();
        String pattern="balloon";
        int result=Integer.MAX_VALUE;
        int m=pattern.length();
        int[] freqText=new int[26];
        int[] freqPattern=new int[26];

        for(int i=0;i<n;i++){
            freqText[text.charAt(i)-'a']++;
        }
        for(int i=0;i<m;i++){
            freqPattern[pattern.charAt(i)-'a']++;
        }

        for (int i=0;i<26;i++){
        if (freqPattern[i] > 0) {
            result = Math.min(result, freqText[i] / freqPattern[i]);
        }
    }
        return result;
    }
}