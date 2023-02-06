//============================================================================\\
//-------------  Algorithms and Data Structures - Assignment 01 --------------\\
//                      Frederik Lind - flin@itu.dk - 20921                   \\
//                                 05.02.2023                                 \\
//============================================================================\\

// Assignment 01 - Disjoint Sets - translation of Python -> to Java

import java.util.Scanner;

public class DisjointSets {

    String[] nums;
    static int[] data;

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String[] fl = sc.nextLine().split(" ");
        int n = Integer.parseInt(fl[0]);
        int m = Integer.parseInt(fl[1]);
        
        for (int i = 0; i < n; i++) { 
            data[i] = i; 
        }

        for (int i = 0; i < m; i++) {
            int op = sc.nextInt();
            int s = sc.nextInt();
            int t = sc.nextInt();
            int S = find(s);
            int T = find(t);

            if (op == 2) {
                move(s, t);
            } else if (op == 0) {
                System.out.println(S == T ? "1" : "0");
            } else {
                data[S] = T;
            }
        }  
        sc.close();
    }

    static int find(int x) {
        if (data[x] != x) {
            data[x] = find(data[data[x]]);
        }
        return data[x];
    }

    static void move(int s, int t) {
        int S = find(s);
        int T = find(t);
        if (S != T) {
            data[S] = T;
        }
    }
}