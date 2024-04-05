class Solution {
    public String reverseWords(String s) {
    String[] sChar=s.split("\\s+");
        int left=0;
        int right=sChar.length-1;
        while(left<right){
                swapWords(sChar,left,right);
                left++;
                right--;


        }
        return String.join(" ",sChar).trim();
}

    private static void swapWords(String[] arr,int left,int right) {
        String temp=arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
    }
}