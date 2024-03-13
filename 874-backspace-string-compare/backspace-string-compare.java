class Solution {
    public boolean backspaceCompare(String s, String t) {
        String word1=prepareString(s);
        String word2=prepareString(t);
        if(word1.equals(word2))
            return true;
        else 
            return false;
        
    }
    
    public String prepareString(String word){
        StringBuilder s=new StringBuilder();
        for(char c :word.toCharArray()){
            if(c!='#'){
                s.append(c);
            }else{
                if(s.length()>0)
                    s.deleteCharAt(s.length()-1);
            }
        }
        return s.toString();
    }
}





