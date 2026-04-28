class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> countsS= new HashMap<>();
        Map<Character, Integer> countsT = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            countsS.put(s.charAt(i), countsS.getOrDefault(s.charAt(i), 0) + 1);
            countsT.put(t.charAt(i), countsT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return countsS.equals(countsT);

    }
}
