from fake_useragent import UserAgent
import requests
   
if __name__ == "__main__":
    print("nike\n")
    #ua = UserAgent()
    #print(ua.chrome)
    #header = {'User-Agent':str(ua.chrome)}
    #print(header)
    url = "https://www.nike.com/launch/t/air-jordan-13-playoffs"
    htmlContent = requests.get(url)
    print(type(htmlContent.content))
    
    with open('output.txt', 'w') as f:
        f.write(str(htmlContent.content))