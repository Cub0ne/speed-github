# speed-github
可能会解决github在国内加载和下载速度慢的问题


### 速度慢原因


CDN，Content Distribute Network，可以直译成内容分发网络，CDN解决的是如何将数据快速可靠从源站传递到用户的问题。用户获取数据时，不需要直接从源站获取，通过CDN对于数据的分发，用户可以从一个较优的服务器获取数据，从而达到快速访问，并减少源站负载压力的目的。

但是GitHub的CDN被某墙屏了，由于网络代理商的原因，所以访问下载很慢。




### 实现原理
直接获取ip地址并绑定本地host，绕过DNS解析。通过脚本获取下列网址ip
<pre>
<code>
	gist.github.com
    github.com
    www.github.com
    avatars0.githubusercontent.com
    avatars1.githubusercontent.com
    avatars2.githubusercontent.com
    avatars3.githubusercontent.com
    avatars4.githubusercontent.com
    avatars5.githubusercontent.com
    avatars6.githubusercontent.com
    avatars7.githubusercontent.com
    avatars8.githubusercontent.com
    camo.githubusercontent.com
    cloud.githubusercontent.com
    gist.githubusercontent.com
    marketplace-screenshots.githubusercontent.com
    raw.githubusercontent.com
    repository-images.githubusercontent.com
    user-images.githubusercontent.com
</code>
</pre>

将获取的ip与对应的网址填入host文件中，然后刷新本地DNS.


### 运行环境

- python3+
- 依赖库
	- BeautifulSoup
	- requsts
	- shutil

### 使用方式
 此分支产出host文件，目标是每天更新，推荐使用SwitchHost软件远程更新