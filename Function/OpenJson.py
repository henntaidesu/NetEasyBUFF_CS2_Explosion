import json
import os

def read_database_config():
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建相对路径
    file_path = os.path.join(script_dir, '../BuffDataConfig.json')

    with open(file_path, 'r') as file:
        data = json.load(file)

    host = data['host']
    port = int(data['port'])
    user = data['user']
    password = data['password']
    database = data['database']

    return host, port, user, password, database
