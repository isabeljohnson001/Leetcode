class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
         int[] res=new int[nums1.length];
        HashMap<Integer,Integer> hs=new HashMap<>();
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i< nums2.length;i++){
            while(!stack.isEmpty()&& nums2[i]>stack.peek()){
                hs.put(stack.pop(),nums2[i]);
            }
            stack.push(nums2[i]);
        }
        while (!stack.isEmpty()){
            hs.put(stack.pop(),-1);
        }
        for(int i=0;i<nums1.length;i++){
            res[i]=hs.get(nums1[i]);
        }
        return res;
    }
}







