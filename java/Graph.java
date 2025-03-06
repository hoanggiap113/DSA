import java.util.*;
import java.util.Collections;

public class Graph {
    private static ArrayList<List<Integer>> ke = new ArrayList<>(1000);
    private static boolean[] visited = new boolean[1000];
    private static int[] parent = new int[1000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        for (int i = 0; i <= n; i++) {
            ke.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            ke.get(x).add(y);

        }
        visited = new boolean[n + 1];
        Arrays.fill(visited, false);

        sc.close();
        dfs(s);
        if (!visited[t]) {
            System.out.println("No path");
        } else {
            List<Integer> path = new ArrayList<>();
            while (t != s) {
                path.add(t);
                t = parent[t];
            }
            path.add(s);
            Collections.reverse(path);
            for (int x : path) {
                System.out.print(x + " ");
            }
        }

    }

    public static void dfs(int u) {
        System.out.print(u + " ");
        visited[u] = true;
        for (int v : ke.get(u)) {
            if (!visited[v]) {
                parent[v] = u;
                dfs(v);
            }
        }
    }

    public static void bfs(int u) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(u);
        visited[u] = true;
        while (!q.isEmpty()) {
            int v = q.poll();
            System.out.print(v + " ");
            for (int x : ke.get(v)) {
                if (!visited[x]) {
                    q.offer(x);
                    visited[x] = true;
                }
            }
        }
    }

}
