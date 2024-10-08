class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandies=0;
        for(int candy: candies){
            maxCandies=Math.max(candy,maxCandies);
        }
        ArrayList ls=new ArrayList();
        for(int candy :candies){
            ls.add(candy+extraCandies>=maxCandies);
        }
        return ls;
    }
}