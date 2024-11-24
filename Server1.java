import java.net.*;
import java.io.*;
public class Server1 {
// Initialize socket and input stream
private Socket socket = null;
private ServerSocket server = null;
private DataInputStream in = null;
// Constructor with port
public Server1(int port) {
// Starts server and waits for a connection
try {
server = new ServerSocket(port);
System.out.println("Server started");
System.out.println("Waiting for a client ...");

socket = server.accept();
System.out.println("Client accepted");
// Takes input from the client socket
in = new DataInputStream(new
BufferedInputStream(socket.getInputStream()));

String line = "";
// Reads message from client until "BYE" is sent
while (!line.equals("BYE")) {
try {
line = in.readUTF();
System.out.println(line);
} catch (IOException i) {
System.out.println(i);
}
}
System.out.println("Closing connection");
// Close connection
socket.close();
in.close();
} catch (IOException i) {
System.out.println(i);
}
}
public static void main(String[] args) {
new Server1(5000);
}
}