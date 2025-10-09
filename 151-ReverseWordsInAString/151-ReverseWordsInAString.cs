// Last updated: 10/8/2025, 9:52:11 PM
public class Solution {
    public string ReverseWords(string s) {
            string[] split = s.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
            Array.Reverse(split);
            string output = string.Join(" ", split);
            return output;
        
    }
}