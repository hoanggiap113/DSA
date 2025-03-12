import java.util.*;

public class Test {
    // public static int numberOfSubStrings(String s){
    // HashMap<Character,Integer> hashMap = new HashMap<>();
    // for(char x : s.toCharArray()){
    // if(hashMap.containsKey(x)){
    // hashMap.put(x,hashMap.get(x) + 1);
    // }else{
    // hashMap.put(x,1);
    // }
    // }

    // return 1;
    // }
    public static int numberOfSubstrings(String s) {
        int start = 0;
        HashSet<Character> set = new HashSet<>();
        set.add('a');
        set.add('b');
        set.add('c');
        int cnt = 0;

        for (int end = 2; end <= s.length() - 1; end++) {
            String str = s.substring(start, end + 1);
            int check = 0;

            for (char c : str.toCharArray()) {
                if (set.contains(c)) {
                    check += 1;
                }

            }
            if (check == 3) {
                cnt += s.length() - end;
            }
            start++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = "aaacb";
        int result = numberOfSubstrings(s);
        System.out.println(result);
    }
}
