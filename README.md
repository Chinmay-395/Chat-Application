![caption](./Django-Channels-Chat-App.mp4)

### Recommended Start

1. Clone the repo
2. Create a user through supuerUser
3. Install redis
4. create virtualenv and install dependencies from "requirements.txt" file
5. Run the app and go to the url "/messages/<user-name>" you want to chat-with

### Install Redis

1. Download Redis

   - Using [Homebrew](http://brew.sh):

     ```
     brew install redis

     brew services start redis
     ```

     Brew permission errors? Try `sudo chown -R "$USER":admin /usr/local`

   - Direct [Download](http://redis.io/download)

2. Open & Test Redis:

   - open Terminal

   - **redis-cli ping**

     ```
     $ redis-cli ping
     PONG
     ```

   - **redis-server**

     ````
     $ redis-server
     86750:C 08 Nov 08:17:21.431 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
     86750:M 08 Nov 08:17:21.433 * Increased maximum number of open files to 10032 (it was originally set to 256).
                     _._
                _.-``__ ''-._
           _.-``    `.  `_.  ''-._           Redis 3.2.5 (00000000/0) 64 bit
       .-`` .-```.  ```\/    _.,_ ''-._
      (    '      ,       .-`  | `,    )     Running in standalone mode
      |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
      |    `-._   `._    /     _.-'    |     PID: 86750
       `-._    `-._  `-./  _.-'    _.-'
      |`-._`-._    `-.__.-'    _.-'_.-'|
      |    `-._`-._        _.-'_.-'    |           http://redis.io
       `-._    `-._`-.__.-'_.-'    _.-'
      |`-._`-._    `-.__.-'    _.-'_.-'|
      |    `-._`-._        _.-'_.-'    |
       `-._    `-._`-.__.-'_.-'    _.-'
           `-._    `-.__.-'    _.-'
               `-._        _.-'
                   `-.__.-'

     86750:M 08 Nov 08:17:21.434 # Server started, Redis version 3.2.5
     86750:M 08 Nov 08:17:21.434 * The server is now ready to accept connections on port 6379

     ````

     **Close Redis** with `control` + `c` to quit
