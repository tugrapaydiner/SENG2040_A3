// ------------------------------------------------------
// Date: 2025-02-25
// Author: Tugrap Turker Aydiner
// Description: Java client that sends logs to the Python server.
// ------------------------------------------------------

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TestClient 
{
    private static String serverHost = "127.0.0.1"; // default host
    private static int serverPort = 5001; // default port

    public static void main(String[] args) 
    {
        if (args.length >= 2) // have 2 or more arguments
        {
            serverHost = args[0]; // first is host
            try // try to parse port
            {
                serverPort = Integer.parseInt(args[1]); // parse second arg
            } catch (NumberFormatException ex) // fails
            {
                System.out.println("Port argument invalid, using 5001."); // fallback
                serverPort = 5001; // fallback
            }
        } else if (args.length == 1) //  exactly 1 argument
        {
            serverHost = args[0]; // act as the host
        } else  // zero arguments
        {
            // then i dont need anything its the defult again
        }

        System.out.println("Connecting to " + serverHost + ":" + serverPort); // printing connection info

        Scanner scanner = new Scanner(System.in); // scanner for console
        while (true) 
        {
            System.out.println("----------------------------------");
            System.out.println("Menu Options:");
            System.out.println("1) Send a manual log message");
            System.out.println("2) Send 10 spam log messages"); 2
            System.out.println("3) Quit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine().trim(); // read choice

            if ("1".equals(choice)) // if  1
            {
                doManualLogs(scanner); // call manual logs
            } else if ("2".equals(choice)) // typed 2
            { 
                doAutoLogs(); // call auto logs
            } else if ("3".equals(choice)) // if typed 3
            { 
                System.out.println("Exiting client, bye bye."); // message
                break; // break  loop
            } else //  not recognized?
            {
                System.out.println("This choice is Invalid, please try again."); // prompt user
            }
        }
        scanner.close(); // close scanner
    }

    private static void doManualLogs(Scanner sc) 
    {
        System.out.println("Manual Log Mode. Type 'exit' to return to the menu."); // instructions
        while (true) // loop
        {
            System.out.print("Enter log level or 'exit': ");
            String level = sc.nextLine().trim(); // read line
            if ("exit".equalsIgnoreCase(level)) // if user typed exit
            {
                break; // exit
            }
            System.out.print("Enter your log message (or 'exit'): "); // prompt message
            String msg = sc.nextLine(); // read message
            if ("exit".equalsIgnoreCase(msg)) // if exit
            { 
                break; // then we exit
            }
            sendLogMessage(level, msg); // call function to send log
        }
    }

    private static void doAutoLogs() 
    {
        System.out.println("Auto logs: sending 10 messages.");
        for (int i = 1; i <= 10; i++) // loop from 1 to 10 ( I can change this if needed)
        { 
            String chosenLevel;
            if (i % 2 == 0) // if even
            {
                chosenLevel = "DEBUG"; // set debug
            } else if (i % 3 == 0) // if multiple of 3
            { 
                chosenLevel = "INFO"; // set info
            } else 
            {
                chosenLevel = "WARN"; // set warn
            }
            String message = "AutoMessage #" + i; // build message
            sendLogMessage(chosenLevel, message); // send it
            try
            {
                Thread.sleep(300); // 300ms
            } catch (InterruptedException e) // catch interrupt
            { 
                // ignoring
            }
        }
        System.out.println("Done sending auto logs. Check the server log file."); // final note
    }

    private static void sendLogMessage(String level, String message) 
    {
        Socket sock = null;
        PrintWriter out = null;
        try 
        {
            sock = new Socket(serverHost, serverPort); // open a socket
            out = new PrintWriter(sock.getOutputStream(), true); // create writer
            String payload = level + "::" + message; // format log string
            out.println(payload); // send line
        } catch (IOException e) // if there's an IO error
        {
            System.out.println("Error sending log: " + e.getMessage()); // print error
        } finally // finally block
        {
            if (out != null) // if writer open
            {
                out.close(); // close writer
            }
            if (sock != null) // socket  open
            {
                try // try close
                {
                    sock.close(); // close
                } catch (IOException ex) // catch
                {
                    // ignore
                }
            }
        }
    }
}