
#代理api，一次返回一个代理ip,格式: <ip>:<port>
PROXY_API = ''
#本地存放token的文件路径
TOKEN_FILE = 'files/tokens.txt'
#请求获取token的最大个数
MAX_TOKEN_GETS = 100
#请求token的最大线程数
MAX_TOKEN_THREADS = 100
# 签名服务器授权token，
API_TOKEN = "08338ef0b578ef208dfacbce2a9db2e0"
#MongoDB数据库设置
MongoDB = {
    'host'          :'127.0.0.1',
    'port'          :27017,
    'database'      :'抖音',
    'records'       :'爬取记录',
    'tokens'        :'tokens',
    'user'          :'',
    'password'      :'',
}
#日志设置
#启用日志
LOG_ENABLE = True
#日志级别
LOG_LEVEL = 'INFO'
#日志文件编码
LOG_FILE_ENCODING = 'UTF-8'
#日志文件路径
LOG_FILE_SAVE_PATH = r'txt/log.txt'
#日志时间格式
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#日志级别对应格式
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}