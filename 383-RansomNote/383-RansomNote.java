// Last updated: 10/8/2025, 9:50:55 PM
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
         HashMap<Character,Integer> hs2=new HashMap<>();
        char[] arr2=magazine.toCharArray();
        for(char item :arr2){
            hs2.put(item, hs2.getOrDefault(item,0)+1);
        }

        char[] arr=ransomNote.toCharArray();
        for(char key :arr){
            if(hs2.containsKey(key)){
                int count=hs2.get(key);
                if(count==0){
                    return false;
                }
            hs2.put(key,count-1);}else{return false;}
        }
        return true;

    }
}