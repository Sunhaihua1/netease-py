import requests
def music_search():
    name = input("请输入要搜索的内容\n")
    url = 'https://musicapi.leanapp.cn/search?keywords='+name
    id_list = requests.get(url=url).json()
    ids = []
    names = []
    for id in id_list['result']['songs']:
        ids.append(id['id'])
        names.append(id['name'])
    music_dict = dict(zip(names, ids))
    for key,value in music_dict.items():
        print(key,"的id为",value)
def music_download():
    id_choice=input('请选择要下载的歌曲id(不包含汉字)\n')
    id_choice=id_choice.replace(' ', '')
    url='http://music.163.com/song/media/outer/url?id='+id_choice+'.mp3'
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36'
    }
    music_data=requests.get(url=url,headers=headers).content
    name=input('请为该歌曲命名\n')+'.mp3'
    print('正在下载中')
    fp=open(name,'wb')
    fp.write(music_data)
    print(name,'下载成功')

if __name__=='__main__':
    music_search()
    music_download()
    choice=input('请选择接下来的操作\n---1 重新搜索\n---2 继续下载')
    if choice==1:
        music_search()
    else:music_download()



