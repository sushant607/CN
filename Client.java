import java.io.*;
import java.net.*;
public class Client {
// Initialize socket and input/output streams
private Socket socket = null;
private DataInputStream input = null;
private DataOutputStream out = null;
// Constructor to specify import java.io.*;
import java.net.*;
class MyServer1 {
public static void main(String[] args) throws Exception {
// Create a server socket listening on port 3333
ServerSocket ss = new ServerSocket(3333);
System.out.println("Server is listening on port 3333");
// Accept client connections
Socket s = ss.accept();
System.out.println("Client connected");
// Create input and output streams
DataInputStream din = new DataInputStream(s.getInputStream());
DataOutputStream dout = new DataOutputStream(s.getOutputStream());
BufferedReader br = new BufferedReader(new
InputStreamReader(System.in));
String str = "", str2 = "";
// Keep communicating until "BYE" is received
while (!str.equals("BYE")) {
str = din.readUTF();
System.out.println("Client says: " + str);

str2 = br.readLine();
dout.writeUTF(str2);
dout.flush();
}
// Close resources
din.close();
dout.close();
s.close();
ss.close();
}
}
IP address and port
public Client(String address, int port) {
// Establish a connection
try {
socket = new Socket(address, port);
System.out.println("Connected");
// Takes input from terminal
input = new DataInputStream(System.in);
// Sends output to the socket
out = new DataOutputStream(socket.getOutputStream());
} catch (UnknownHostException u) {
System.out.println("Unknown host: " + u.getMessage());
return;
} catch (IOException i) {
System.out.println("IO error: " + i.getMessage());
return;
}
// String to read message from input
String line = "";
// Keep reading until "BYE" is input
while (!line.equals("BYE")) {
try {
line = input.readLine();
out.writeUTF(line);

} catch (IOException i) {
System.out.println("IO error: " + i.getMessage());
}
}
// Close the connection
try {
input.close();
out.close();
socket.close();
} catch (IOException i) {
System.out.println("IO error: " + i.getMessage());
}
}
public static void main(String[] args) {
new Client("127.0.0.1", 5000);
}
}