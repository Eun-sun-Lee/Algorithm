import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.awt.Point;
import java.util.Collections;

public class Main{
    static final int dx[] = {0,0,1,-1};
    static final int dy[] = {1,-1,0,0};
    static int n,m,loop;
    static int visited [][];
    static ArrayList<Integer> area = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw =  new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        loop = Integer.parseInt(st.nextToken());

        visited = new int[n][m];

        for(int i=0; i<loop; i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for(int y=y1; y<y2; y++ ){
                for (int x=x1; x<x2; x++){
                    visited[y][x] = 1;
                }
            }
        }

        Queue<Point> queue = new LinkedList<Point>();
        for(int nn=0; nn<n; nn++){
            for (int mm=0; mm<m; mm++){
                if (visited[nn][mm]!=1){
                    visited[nn][mm]=1;
                    queue.add(new Point(mm, nn));
                    area.add(1);
                    while (queue.size()>0){
                        Point point = queue.poll();
                        int x = point.x;
                        int y = point.y;
                        for(int k=0; k<4; k++){
                            int nx = x+dx[k];
                            int ny = y+dy[k];
                            if (((0 <= nx && nx < m && 0 <=ny && ny < n))&& visited[ny][nx]!=1){
                                visited[ny][nx] = 1;
                                queue.add(new Point(nx,ny));
                                int oldValue = area.get(area.size()-1) ;
                                int newValue= oldValue + 1;
                                area.set(area.size()-1, newValue);
                            }
                        }
                    }
                }
            }
        }
        Collections.sort(area);

        System.out.println(area.size());
        for (int ii=0; ii<area.size(); ii++){
            System.out.print(area.get(ii) + " ");
        }


    }
}