public class Solution {
    public void ReverseWords(char[] s) {
        int length=s.Length;
        int start=0;
        for(int i=0;i<length;i++){
            if(s[i]==' ')
            {
                reverse(s,start,i-1);
                start=i+1;
            }
        }
        reverse(s,start,length-1);
        reverse(s,0,length-1);

}

public void reverse(char[] input,int start,int end)
{
    while(start<end)
    {
    char temp=input[start];
    input[start]=input[end];
    start++;
    input[end]=temp;
    end--;
    }
   
}
}