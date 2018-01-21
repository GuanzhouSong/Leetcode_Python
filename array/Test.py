import urllib.error

try:
  url = input("address:")
  fhand = urllib.request.urlopen(url)
except:
  print("Wrong!")
dic = dict()
for data in fhand:
  line = data.decode().split()
  for word in line:
    c = dic.get(word, 0)
    dic[word] = c + 1
print(dic)
