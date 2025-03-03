import time
import heapq
class Timecache:
    def __init__(self):#Here im creating an object of the class cache which calls itself automaticall i.e a constructor
        self.cache={}#here im storing the keys and values of the dict where the value is a tuple having (value, expiry time)
        self.expiry_heap=[]#this helps in tracking which key expires first
    def set(self,key,value,expiryTime):
        exp_time=time.time()+expiryTime#Calculates the number of seconds after which the key should expire according to the current time
        self.cache[key]=(value,exp_time)
        heapq.heappush(self.expiry_heap,(exp_time,key))#keeps trach of which expires first and by default early expiry time is at the top
    def get(self,key):
        now_time=time.time()
        while(self.expiry_heap and self.expiry_heap[0][0]<=now_time):#suppose the time now is 10, the expiry time of a key is 8, which is less than time now (10), hence its already expired, so i remove the key
            _,exp_key=heapq.heappop(self.expiry_heap)
            if exp_key in self.cache:
                del self.cache[exp_key]
        if key in self.cache:
            return self.cache[key][0]#if key still valid it prints the value
        return None
cache=Timecache()
k=input("Enter key: ")
v=int(input("Enter value: "))
t=int(input("Enter expiry time: "))
w=int(input("Enter waiting time: "))
cache.set(k,v,t)
print("Value before waiting: ")
print(cache.get(k))
time.sleep(w)#waits for w seconds so a expires
res=cache.get(k)
if res is None:
    print("Key is expired")
else:
    print(res)
