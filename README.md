# PySNMP-sample

## How to use

```
>cd path\to\dir

path\to\dir>git clone https://github.com/thinkAmi-sandbox/PySNMP-sample.git

path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

(env) >python get_request.py
# => [ObjectType(ObjectIdentity(ObjectName('1.3.6.1.2.1.43.10.2.1.6.1.1')), Integer32(4))]
```

　    
## Tested Envrionment

- Windows10 x64
- Python 3.5.1 32bit
- PySNMP 4.3.2

　  
## Related Blog (Written in Japanese)

[Windows + Python3 + PySNMPで、SNMPのGET Requestを送信する - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/06/12/083043)