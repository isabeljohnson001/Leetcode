class Solution {
    public String reverseVowels(String s) {
    int left=0;
    int right=s.length()-1;
    char[] sChar=s.toCharArray();
    while(left<right){
        while(left<s.length() && !isVowel(s.charAt(left))){left++;}
        while(right>=0 && !isVowel(s.charAt(right))){right--;}
        if(left<right){
            swap(sChar,left,right);
            left++;
            right--;
        }
    }
        return new String(sChar);
    }

    private static void swap(char[] arr,int left,int right) {
        char temp=arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
    }


    private static boolean isVowel(char c) {
        if(c=='a' || c=='e' ||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
            return true;
        else
            return false;
    }
}