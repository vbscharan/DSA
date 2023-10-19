//{ Driver Code Starts
import java.io.*;
import java.util.*;

class IntArray {
    public static int[] input(BufferedReader br, int n) throws IOException {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(s[i]);

        return a;
    }

    public static void print(int[] a) {
        for (int e : a) System.out.print(e + " ");
        System.out.println();
    }

    public static void print(ArrayList<Integer> a) {
        for (int e : a) System.out.print(e + " ");
        System.out.println();
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            int N;
            N = Integer.parseInt(br.readLine());

            int K;
            K = Integer.parseInt(br.readLine());

            int target;
            target = Integer.parseInt(br.readLine());

            int[] coins = IntArray.input(br, N);

            Solution obj = new Solution();
            boolean res = obj.makeChanges(N, K, target, coins);

            int _result_val = (res) ? 1 : 0;
            System.out.println(_result_val);
        }
    }
}

// } Driver Code Ends


class Solution {
    public static boolean makeChanges(int N, int K, int target, int[] coins) {
        // code here
        boolean dp[][][] = new boolean[N+1][target+1][K+1];
        dp[0][0][0] = true;
        for(int i = 1; i <= N;i++){
            for(int j = 0; j <= target; j++){
                for(int k = 0;k <= K; k++){
                   if(coins[i-1] <= j && k > 0 && dp[i][j-coins[i-1]][k - 1]){
                      dp[i][j][k] = true;
                   }else if(dp[i-1][j][k]){
                      dp[i][j][k] = true;
                  }
                }
            }
        }
        return dp[N][target][K];
    }
}
