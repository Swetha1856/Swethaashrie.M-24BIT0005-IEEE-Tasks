# Swethaashrie.M-24BIT0005-IEEE-Tasks

Heyy, My name is Swetha and i'll give u a brief explanation on how i coded for each level of my tasks.

Level 1(Custom data structure implementation):



I have asked the user to input the following

-->Length of the stack  
-->Each element of the original stack  
-->The users choice out of the Menu options  
-->Asking the user if the user wants to continue manipulating the stack  

I have created functions to simplify my task and make the program more readable.

I have also tried to make it easy for the user to keep in track of the user's previous changes on the current stack as the user makes changes to the stack in future by showing the user the original stack alongside the resultant stack.

At the end i ask the user if they want to continue , based on yes or no the loop runs or stops.

My output:

![image](https://github.com/user-attachments/assets/f37cacfb-d5c3-44aa-bf63-2b6e616a2bab)
![image](https://github.com/user-attachments/assets/b862cb55-31b7-4383-8ef9-79789bde21b7)
![image](https://github.com/user-attachments/assets/67b506f6-09e8-4c12-b5af-e41f9cf6b1a9)
![image](https://github.com/user-attachments/assets/9d633a1c-62fd-4747-9316-57c92406ea7c)

Level 2: Composite data structure implementation



I have asked the user to input the following:

-->The choice the user wants to choose on which operation to be done  
-->the start and end value of the interval the user wants to add  

After accepting start and end value of interval, I added all intervals to a list in the form of [[start,end]]

Then I sorted the elements of the list based on the start value of each interval added.

I compared the end of the last interval with the start of the new interval to check if they are overlapping or not

If overlapping , I update the new list's end value with the max of nlst[-1][1] or (i[1] which is the end of the new interval)

If they dont overlap then i just update the new list

At the end i ask the user if they want to continue , based on yes or no the loop runs or stops.

My output 1:

![image](https://github.com/user-attachments/assets/f8257d32-573d-49ab-835d-2de93666633c)
![image](https://github.com/user-attachments/assets/a13fcbc8-2770-48ca-be68-02e7857ca788)

My output 2:

![image](https://github.com/user-attachments/assets/69bdc80f-fbc9-479e-a263-945eff2ef5d5)
![image](https://github.com/user-attachments/assets/5cdf89f6-b00b-4201-927b-01284a0fad85)

My output 3:

![image](https://github.com/user-attachments/assets/5fe9ca58-78d9-4561-8eb1-2d1e61f43405)
![image](https://github.com/user-attachments/assets/e75f645b-bfe4-4225-b1ff-906bc9051e9f)


Level 3: Cache with Expiry(Time-Based Cache)



General idea: 

1.You give an key, value and the expiration of the key.  
2.Get the current time you are running the program.  
3.With respect to your current time and waiting time, finds out if the value has expired or not.  
4.If not display value of key, if expired then deletes the key from cache.  

	
Steps involved:

1.I set “a” with value 10 and time of expiry as 5 sec  
2.I assumed current time as t=0  
3.expiry_time=t+5=5  
4.Heap: [(5,”a”)]  
5.Cache: {“a”(10,5)}  
6.get(“a”)  
	7.current time t=0  
	8.”a” is still valid(expiry_time=5)  
	9.returns 10  
10.time.sleep(6) makes the execution stop for 6 seconds  
11.now checks if the key is valid or not again  
	12.current time t=6  
	13.”a” expired so “a” is removed from cache and hence prints key expired  

My output 1:  
![image](https://github.com/user-attachments/assets/732705de-cfb6-4519-987f-f9a43b42020b)

My output 2:  
![image](https://github.com/user-attachments/assets/e6cbb6eb-f043-4831-a1ce-ff16a52fd825)

My output 3:  
![image](https://github.com/user-attachments/assets/14c8b57b-dce0-4076-bb6e-3050c2d53346)

My output 4:  
![image](https://github.com/user-attachments/assets/d4da5391-ed5c-44fc-8950-0adf68cd8b20)


















