// Last updated: 10/8/2025, 9:51:08 PM
public class Solution {
    public void ReverseString(char[] s)
{
    //s = ["h","e","l","l","o"]
    int left = 0;
    int right = s.Length-1;
    while (left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}
}