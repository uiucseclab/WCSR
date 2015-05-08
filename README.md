# WCSR

Website Connection Security Rater (WCSR)
This project was created by Alison, Duyen, and Karolina for CS 460 Spring 2015.

Although many browsers show the connection information on a website, it is difficult to understand what it all means. The purpose of this project was to create a browser plugin that would be able to automatically read this information, explain what it means in layman’s terms, and appropriately rate the security of that connection. However, most of the time given for this project was spent researching different key exchange mechanisms, connection encryption algorithms, message authentication schemes, and certificate authorities. There wasn’t enough time to learn how to create a browser plugin, so instead, we wrote a Python script that would provide the same information. In the future, we hope to expand on the information we collected and create a working plugin.

To start the program, run the python script called wcsr.py. You are given the option to rate your connection or learn more about the criteria the rating is based off of. If you choose to rate your connection, you are asked to select the type of key exchange mechanism your connection uses, the encryption scheme, and the message authentication (this can be found on Firefox). The score of each component is tallied up and the total score out of 30 is displayed. A larger number means a more secure connection.

If you choose to learn more, you can select from the three criteria as well as from certificate authorities. Each option gives a brief description of the purpose and importance of each, and some provide further detail on select versions.
