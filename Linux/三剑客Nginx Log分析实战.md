#### egrep awk sed sort uniq head
```
egrep " /topics/[0-9]{1,}" nginx.log\
| awk '{print $7}'|sed 's#?.*##'\
| sed 's#/topics/[0-9]*$#/topics/topics#'\
| sed 's#/topics/[0-9]*/replies/[0-9]*/.*#/topics/replies#'\
| sed 's#/topics/[0-9]*/show_wechat#/topics/show_wechat#'\
| sort |uniq -c | sort -nr | head -3
```

