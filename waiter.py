
import os
import time
from config import *
from log import getLogger
from deco.waiter import check
from util.threads import CrawlThread
from util.tools import time_to_date
from util.waiter import request_token
from config import TOKEN_FILE
from dbhelper import Database

logger = getLogger(__name__)

class Waiter:

    def __init__(self):
        self.tokens = set()
        self.db = Database(MongoDB)

    @check
    def generate_tokens(self,proxy_api=PROXY_API,count=MAX_TOKEN_GETS,toDB=False,
                        tname=MongoDB['tokens'],path=None):
        _tokens = set()
        lower = min(MAX_TOKEN_THREADS,count)
        _got = 0
        step = min(lower, count)
        while len(_tokens)!=count:
            if not proxy_api:
                logger.error(f'No proxy api for requesting tokens.Set one!')
                return
            threads = []
            for i in range(step):
                threads.append(CrawlThread(request_token,args=(proxy_api,)))
            for i in threads:
                i.start()
            for i in threads:
                i.join()
                res = i.get_result()
                if res:
                    _tokens.add(i.get_result())
                    _got += 1
            if _got >= count:
                logger.info(f'Got {_got} tokens.')
                self.tokens.update(_tokens)
                break
            else:
                step = count-_got
        if toDB:
            for i in _tokens:
                _ = {
                        'token':i,
                        "generate_at":time_to_date(time.time())
                     }
                self.db.save(_,tname=tname)
            logger.info(f'Tokens saved into table "{tname}" successfully.')
        if path:
            with open(path,'a') as f:
                for i in _tokens:
                    f.write(i+'\n')
                logger.info(f'Tokens saved into file "{path}" successfully.')

    def _check_token_files(self,file_path=TOKEN_FILE):
        if os.path.isfile(file_path):
            with open(file_path) as f:
                lines = f.readlines()
                for i in lines:
                    self.tokens.add(i.strip('\n'))
                logger.info(f'Loaded tokens from "{file_path}",amount:{len(self.tokens)}')
        else:
            logger.warning(f'Token files not found.')

    def _check_token_table(self):
        if not self.db.connected:
            self.db.connect()
        tokens = self.db.all(MongoDB['tokens'])
        if tokens:
            _ = 0
            for i in tokens:
                self.tokens.add(i['token'])
                _+=1
            logger.info(f'Loaded tokens from table "{MongoDB["tokens"]}",amount:{_}')
        else:
            logger.warning(f'Token data table not found.')