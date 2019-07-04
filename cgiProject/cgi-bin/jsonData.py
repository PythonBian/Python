import json
import time
import random

now = time.strftime("%H:%M:%S",time.localtime())
num = random.randint(1,11)

result = {"now":now,"num":num}

josn_result = json.dumps(result) #将字典转换为json
#loads 将json转换为字典

print("content-type:application/json") #返回响应的头部，具体描述的要返回的内容类型，在cgi当中用print进行返回
print("\n") #返回头部结束
print(josn_result) #返回响应的body