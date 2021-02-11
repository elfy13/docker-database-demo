
#!/usr/bin/env python3

# step 1: import the redis-py client package
import redis
import time

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def hello_redis():
    """Example Hello Redis Program"""
    
    print("Doing things")

    counter = 1;

    # step 3: create the Redis Connection object
    try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        while counter <= 10:
            
            keyStr = "msg:hello"
            valueStr = "Hello Redis!!! " + str(counter)

            # step 4: Set the hello message in Redis
            r.set(keyStr, valueStr)

            # step 5: Retrieve the hello message from Redis 
            msg = r.get(keyStr)
            print(msg)

            counter = counter + 1 
            time.sleep(1)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()
