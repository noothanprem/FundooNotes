import redis


class RedisOperation:

    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.username = ''
        self.password = ''

    response = {"success": False,
                "message": "",
                "data": []}

    def smd_response(self, success, message, data):
        self.response['success'] = success
        self.response['message'] = message
        self.response['data'] = data
        return self.response

    def __connect__(self):
        try:
            self.red = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

        # ping = self.red.ping()

        except NameError:
            response = self.smd_response(False, "Name Error")
            return response
        except ConnectionError as e:
            response = self.smd_response(False, "Connection error")
            return response
        return self.red

    def set(self, key, value):
        self.red.set(key, value)

    def get(self, key):
        value = self.red.get(key)

        return value

    def delete(self, key):
        self.red.delete(key)

    def rpush(self, key, value):
        self.red.rpush(key, value)

    def hmset(self, key, value):
        self.red.hmset(key, value)

    def hget(self, key):
        value = self.red.hget(key)

        return value

    def hvals(self, key):
        value = self.red.hvals(key)

        return value




