import java.io.*;
public class Main{
    public static void main(String args[]) throws IOException {
        BufferedReader BufferRead = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter BufferWrite = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String A = (BufferRead.readLine());
            String B = (BufferRead.readLine());
            if (A.equals("null")){
                A = null;
            }
            if (B.equals("null")){
                B = null;
            }
            boolean a1 = A.equals(B);
            boolean a2 = A.equalsIgnoreCase(B);
            if (a1){
                BufferWrite.write("true"+ "\n");
            }
            else {
                BufferWrite.write("false" + "\n");
            }
            if (a2){
                BufferWrite.write("true"+ "\n");
            }
            else {
                BufferWrite.write("false" + "\n");
            }

        } catch (NullPointerException e) {
            BufferWrite.write("NullPointerException" + "\n");
            BufferWrite.write("NullPointerException" + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            BufferWrite.flush();
            BufferWrite.close();
            BufferRead.close();
        }

    }
}