public class Solution {
    public int MyAtoi(string s) {
        List<char> a=new List<char>();
        s=s.TrimStart();
        for(int i=0;i<s.Length;i++){
            if(Char.IsDigit(s[i])){
                a.Add(s[i]);
                continue;
            }
            if(i==0&&s[i]=='-'){
                continue;
            }
            if(i==0&&s[i]=='+'){
                continue;
            }
            break;
            }
            if(a.Count==0)
            {return 0;}
            bool cor=int.TryParse(String.Join("",a),out int result);
            if(cor && s[0]=='-'){return -result;}
            if(cor){return result;}
            if(!cor && s[0]=='-'){return int.MinValue;}
            else{return int.MaxValue;}
}
}