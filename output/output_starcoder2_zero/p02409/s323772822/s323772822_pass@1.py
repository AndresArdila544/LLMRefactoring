Here is the original Java program:

import java.io.*;
class Main{
    public static void main(String[] args)throws IOException {
        int n=Integer.parseInt(br.readLine());
        int[][][] a=new int[4][3][10];
        for (int i=0;i<n;++i){
            String[] t=br.readLine().split(" ");
            ++a[Integer.parseInt(t[0])-1][Integer.parseInt(t[1])-1][Integer.parseInt(t[2])-1];
        }
        for (int i=0;i<4;++i){
            for (int j=0;j<3;++j) {
                for (int k = 0; k < 10; ++k) System.out.print("  "+a[i][j][k]);
                System.out.println();
            }
            if(i!=3)System.out.println("####################");
        }
    }

    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
}


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Java code.