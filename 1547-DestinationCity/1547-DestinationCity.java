// Last updated: 10/8/2025, 9:48:59 PM
class Solution {
    public String destCity(List<List<String>> paths) {
        Set<String> hs=new HashSet();
    for(int i=0;i< paths.size();i++){
        hs.add(paths.get(i).get(0));
    }
    for(int j=0;j< paths.size();j++){
        String candidate=paths.get(j).get(1);
        if(!hs.contains(candidate)){
            return candidate;
        }
    }
    return "";
    }
}