'''
-Difference between cat and more commands:
CAT is displaying the whole content of a file into the terminal but the MORE command is displaying the content and the content stops to the end of the terminal.
-Difference between rm and rmdir:
Rm is using to delete files but rmdir is used to remove empty directories.
-Copy /etc/passwd/ file to the home directory and rename it as oldpasswd
cp  /etc/passwd/ ~/
mv passwd oldpasswd
-You are in /usr/bin , 4 ways  to go to home directory:
1- cd ../../home
2- cd ~/
3- cd /home/
4- cd –
-get the words  starts with W in the oldpasswd file
Grep ^w oldpasswd
-get the  first 4 lines in the oldpasswd file
Head -4 oldpasswd
-Get the least 7 lines in the oldpasswd file
Tail  -7 oldpasswd
-Display  the passwd file  sequentially
man passwd; man /etc/passwd/
-Display the man page of passwd file
man /etc/passwd/
-Display all list of commands of man
man man


'''