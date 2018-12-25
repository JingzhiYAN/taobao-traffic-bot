import requests

def main():
    headers = {
    "charset":"utf-8",
    "Accept-Encoding":"gzip",
    "referer":"https://servicewechat.com/wxffc08ac7df482a27/117/page-frame.html",
    "authorization":"5bda7657a4ce660001f7eed8",
    "auth":"eyJoYXNoIjoibWQ0IiwiYWxnIjoiSFMyNTYiLCJ0eXAiOiJKV1QifQ.eyJzaWQiOiI0M2RkNGY2YS01NTk1LTRjNGEtYTkyMi05ODEzNjdiMTlmMTEiLCJleHBpcmUiOjE1NDExMzAyNjJ9.9AC8VBcXiBG48vHa-LLgVEWOnloTdQvNWzYAyvqGnMA",
    "content-type":"application/json",
    "auth-sign":"c475525b214bb5d9ae431ac029cb9b50",
    "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070336) NetType/WIFI Language/zh_CN Process/appbrand2",
    "Host":"www.xiaohongshu.com",
    "Connection":"Keep-Alive",
    }
    # url = "http://www.xiaohongshu.com/sapi/wx_mp_api/sns/v1/homefeed?oid=homefeed.cosmetics_v2&cursor_score=&sid=session.1540996623416187718"
    url = "http://www.xiaohongshu.com/sapi/wx_mp_api/sns/v1/homefeed?oid=homefeed.cosmetics_v2&cursor_score=1541067389.9550&sid=session.1540996623416187718"


    datas = requests.get(url= url, headers=headers ).json()
    data = datas['data']
    # print(data)
    for i in data:
        print(i)
        # print(i['title'])
        # print(i['share_link'])
        title = '标题: ' + i['mini_program_info']['share_title']
        print(title)
        link_url = '链接: ' + i['share_link']
        print(link_url)
        b_picture = '封面图片: '+ i['mini_program_info']['thumb']
        print(b_picture)
        type = '类型: ' + i['type']
        print(type)
        level = '级别: ' + str(i['level'])
        print(level)
        h_picture = '用户头像: ' + i['user']['images']
        print(h_picture)
        username = '用户名: ' + i['user']['nickname']
        print(username)
        user_id = 'userid: ' + i['user']['userid']
        print(user_id)
        zan = '喜欢点心: ' + str(i['likes'])
        print(zan)

        # 以追加的方式及打开一个文件，文件指针放在文件结尾，追加读写！
        with open('text', 'a', encoding='utf-8')as f:
            f.write('\n'.join([title,link_url,b_picture,type,level,h_picture,username,user_id,zan]))
            f.write('\n' + '=' * 100 + '\n')
if __name__ == "__main__":
    main()