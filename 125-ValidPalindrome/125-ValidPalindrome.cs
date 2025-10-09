// Last updated: 10/8/2025, 9:52:19 PM
public class Solution {
    public bool IsPalindrome(string s) {
        List<char> list=new List<char>();
        s=s.ToLower();
        for(int i=0;i<s.Length;i++){
            char c=s[i];
            if(char.IsLetterOrDigit(c)){
                list.Add(c);
            }
        }
        for(int i=0;i<list.Count/2;i++){
            if(list[i]!=list[list.Count-1-i])
            return false;
        }
        return true;
        
        
    }
}