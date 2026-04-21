import java.io.*;
public class Main{
	public static void main(String args[]){
		BufferedReader BufferRead = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BufferWrite = new BufferedWriter(new OutputStreamWriter(System.out));
		try {
			int N =Integer.parseInt(BufferRead.readLine());
			int x1, y1, r1, x2, y2, r2, L2, rR, rr;
			x1 = y1 = r1= x2 = y2 = r2 = L2 = rR = rr = 0;
			for (int i=0; i<N; i++) {
				String[] temp = BufferRead.readLine().split(" ");
				x1 = Integer.valueOf(temp[0]);
				y1 = Integer.valueOf(temp[1]);
				r1 = Integer.valueOf(temp[2]);
				x2 = Integer.valueOf(temp[3]);
				y2 = Integer.valueOf(temp[4]);
				r2 = Integer.valueOf(temp[5]);
				L2=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
				rR=(r1+r2)*(r1+r2);
				rr=(r1-r2)*(r1-r2);
				if (L2==0 && r1==r2) {
					BufferWrite.write(String.valueOf(-1) + "\n");}
				else if(rR>L2 && L2>rr) {
					BufferWrite.write(String.valueOf(2) + "\n");}
				else if(rR==L2 || rr==L2) {
					BufferWrite.write(String.valueOf(1) + "\n");}
				else {
				BufferWrite.write(String.valueOf(0) + "\n");}
			}
			BufferWrite.flush();
			BufferWrite.close();
			BufferRead.close();
		} catch (NumberFormatException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
}
 