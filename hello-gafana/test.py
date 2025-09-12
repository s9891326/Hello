import logging
import os

# 設定log檔案路徑
log_folder = os.path.dirname(__file__)
log_file = os.path.join(log_folder, 'app.log')

# 設定logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# 寫入一筆log
logging.info('hello grafana log')
