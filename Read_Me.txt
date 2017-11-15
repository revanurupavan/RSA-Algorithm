Programming based project 2: Integration of Instant Messenger with RSA


The code invloves execution of two files, namely Rsa_client.py and Rsa_server.py

Execution of the code:
1.Open Rsa_Client.py
2.open Rsa_Server.py
3.Run Rsa_server.py
4.Run Rsa_client.py
5.Send a text from the client to the server
6.We can see that the cipher text of the sending text is displayed on the client side and server side.
7.The  cipher text is decrypted on the server side and displayed on the window.
8.The next text has to be entered on the server side and the same encryption happens
9.The cipher text is displayed on both the ends and the text is decrypted on the client and displayed
10. If there is a 30 seconds timeout i.e. if the conncetion stays idle for 30 seconds, there will be a timeout meaning the conncetion is terminated for security purposes.


The functions invloved on the client side:

1. First the value of n is sent to the server.
2. Message is entered dynamically
3. Each character is taken individually.
4. It is changed to ASCII first.
5. The result is raised to the power of e.
6. The result is mod with n.
7. The final data is padded to make it equal to 4 digits
8. The final data is sent to the server.
9. If the  client doesnt receive a input for the next 30 seconds, connection gets terminated.
10. If there is an input, it is saved in modmessage
11. Length of modmessage is calculated and divided by 4 to get the number of characters.
12. For loop is executed for the number of times as the number of characters
13. The first digits are taken and raised to the power of d
14. The value is mod with n.
15. The output is converted back to string using chr()
16. The while loop is executed again as it an IM.

The functions invloved on the Serverside:
Length of modmessage is calculated and divided by 4 to get the number of characters.
1. The value of n is received and converted to int from str
2. If there is an input, it is saved in message
3. Length of message is calculated and divided by 4 to get the number of characters.
4. For loop is executed for the number of times as the number of characters
5. The first digits are taken and raised to the power of d
6. The value is mod with n.
7. The output is converted back to string using chr()
8. It's the chance of server to send a message to client. Message is entered dynamically
9. Each character is taken individually.
10. It is changed to ASCII first.
11. The result is raised to the power of e.
12. The result is mod with n.
13. The final data is padded to make it equal to 4 digits
14. The final data is sent to the client.
15. If the  server doesnt receive a input for the next 30 seconds, connection gets terminated.
16. The whole procedure is repeated again as it is an IM.
 
