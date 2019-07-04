html = """
<html>
	<head>
		<title>
			image
		</title>
	</head>
	<body>
		<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562231356345&di=14d608194de00e8b04ec741b3b107ab9&imgtype=0&src=http%3A%2F%2Fimage.whhost.net%2Fuploads%2F20180413%2F22%2F1523628708-NofpLxkrHM.jpg">
	</body>
</html>
""" #要返回的数据 response 的body
print("content-type:text/html") #返回响应的头部，具体描述的要返回的内容类型，在cgi当中用print进行返回
print("\n") #返回头部结束
print(html) #返回响应的body