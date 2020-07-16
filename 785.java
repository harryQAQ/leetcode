import java.util.LinkedList;
import java.util.Queue;

class Solution{
    public boolean isBipartite(int[][] graph){
        //bfs
        // 定义 visited 数组，初始值为 0 表示未被访问，赋值为 1 或者 -1 表示两种不同的颜色。
        int[] visited = new int[graph.length];
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < graph.length; i++){
            if(visited[i] != 0){
                continue;
            }
            // 每出队一个顶点，将其所有邻接点染成相反的颜色并入队。
            queue.offer(i);
            visited[i] = 1;
            while(!queue.isEmpty()){
                //出队
                int v = queue.poll();
                for (int w: graph[v]){
                    if (visited[w] == visited[v]) {
                        return false;
                    }
                    visited[w] = 
                }
            }

        }


        return true;

    }
}