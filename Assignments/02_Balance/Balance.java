//============================================================================\\
//-------------  Algorithms and Data Structures - Assignment 02 --------------\\
//                      Frederik Lind - flin@itu.dk - 20921                   \\
//                                 13.02.2023                                 \\
//============================================================================\\

import java.util.ArrayList;
import java.util.List;

public class Balance {

    static String in1 = "([(())])[]";
    static String in2 = ")(";
    static String in3 = "[)";
    static String in4 = "((";
    static String in5 = "[(])";
    static String in6 = "[])[])";
    static String in7 = "(";

    public static void main(String[] args) {

        String[] ins = {in1, in2, in3, in4, in5, in6, in7 };

        for (int i= 0; i < ins.length; i++) {
            System.out.println("" + isBalanced(ins[i]));
        }
    }

    public static int isBalanced(String s) {
        List<Character> symbols = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[') 
                symbols.add(c);
            else if (c != ')' && c != ']'){
                if (symbols.size() == 0) 
                    return 0;
                if ((c == ')' && symbols.get(i-1) == '(') || (c == '(' && symbols.get(i-1) == '['))
                    symbols.remove(c);
                else return 0;        
            }
        } 
        if (symbols.size() == 0)
            return 1;
        else return 0;
    }
}
