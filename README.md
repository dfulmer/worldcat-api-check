## Set up

Clone the repo

```
git clone [copy from above]
cd [directory from above]
```

build container
```
docker-compose build
```

start container
```
docker-compose up -d
```

## Run the program
In order for it to work, you need to fill in the client_id and client_secret variables. Remove this:
[Add client id here]
[add client secret here]
And add you client id and client secret. 

```
docker-compose run --rm app python helloworldcat.py
```