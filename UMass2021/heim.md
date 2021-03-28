# heim

You get this by visiting the page:


![image](https://user-images.githubusercontent.com/29373869/112760912-96365c00-8ff0-11eb-8a83-1d501d1157ad.png)


What is this BEARER token???
I insert a random username and get an access_token. After multiple failed attempts trying to decode the token, I notice that the request needs to have a an aditional parameter.

![image](https://user-images.githubusercontent.com/29373869/112761096-65a2f200-8ff1-11eb-9c75-325776bab5ba.png)
Source: https://swagger.io/docs/specification/authentication/bearer-authentication/

So I used curl

```
curl -H "Authorization: Bearer <token>" url
```

![image](https://user-images.githubusercontent.com/29373869/112761166-d21df100-8ff1-11eb-8256-127b8b6d21b9.png)

Huh... Let's try to add /heim to the url

```
curl -H "Authorization: Bearer <token>" url/heim
```

![image](https://user-images.githubusercontent.com/29373869/112761189-02fe2600-8ff2-11eb-865f-b3405e182ff9.png)


Ding Ding! But it's not over yet. After decoding it we get a long json with this:


![image](https://user-images.githubusercontent.com/29373869/112761223-350f8800-8ff2-11eb-9667-b1f0d79ed077.png)

```
curl -H "Authorization: Bearer <token>" url/flag
```


![image](https://user-images.githubusercontent.com/29373869/112761263-6daf6180-8ff2-11eb-8536-e191ce37c22f.png)


Well, let's try to get a token for Odin.


![image](https://user-images.githubusercontent.com/29373869/112761348-d3035280-8ff2-11eb-8f99-012f4137893a.png)


FLAG=UMASS{liveheim_laughheim_loveheim}
