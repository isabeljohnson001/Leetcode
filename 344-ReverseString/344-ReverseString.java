// Last updated: 10/8/2025, 9:51:05 PM
class Solution {
    public void reverseString(char[] s) {
    int left = 0;
    int right = s.length-1;
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