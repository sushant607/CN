import java.io.*;
import java.net.*;
class MyClient1 {
public static void main(String[] args) throws Exception {
// Create a socket connection to the server
Socket s = new Socket("localhost", 3333);
// Create input and output streams
DataInputStream din = new DataInputStream(s.getInputStream());
DataOutputStream dout = new DataOutputStream(s.getOutputStream());
BufferedReader br = new BufferedReader(new
InputStreamReader(System.in));
String str = "", str2 = "";
// Keep communicating until "BYE" is sent
while (!str.equals("BYE")) {
str = br.readLine();
dout.writeUTF(str);
dout.flush();
str2 = din.readUTF();
System.out.println("Server says: " + str2);

}
// Close resources
dout.close();
s.close();
}