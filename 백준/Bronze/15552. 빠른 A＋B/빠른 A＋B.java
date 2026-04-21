import java.io.*;
public class Main{
	public static void main(String args[]){
		BufferedReader BufferRead = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BufferWrite = new BufferedWriter(new OutputStreamWriter(System.out));
		int A=0;
		int B=0;
		try {
			int T =Integer.parseInt(BufferRead.readLine());
			for (int i=0; i<T; i++) {
				String[] temp = BufferRead.readLine().split(" ");
				A = Integer.parseInt(temp[0]);
				B = Integer.parseInt(temp[1]);
				BufferWrite.write(String.valueOf(A+B) + "\n");
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