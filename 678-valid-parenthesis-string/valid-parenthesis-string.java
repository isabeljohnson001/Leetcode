class Solution {
    public boolean checkValidString(String s) {
    int minOpen = 0; // Minimum open parentheses needed
    int maxOpen = 0; // Maximum open parentheses possible

    for (char c : s.toCharArray()) {
        if (c == '(') {
            minOpen++;
            maxOpen++;
        } else if (c == ')') {
            if (minOpen > 0) {
                minOpen--; // A matching '(' can balance this ')'
            }
            maxOpen--;
        } else { // c == '*'
            if (minOpen > 0) {
                minOpen--; // '*' acts as ')'
            }
            maxOpen++; // '*' acts as '('
        }

        if (maxOpen < 0) {
            // More ')' than '(' + '*' can account for
            return false;
        }
    }

    // Valid if minOpen is 0 (all '(' can be matched)
    return minOpen == 0?true:false; 
    }
}
