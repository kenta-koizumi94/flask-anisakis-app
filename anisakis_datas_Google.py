# Google用クローラーのモジュールをインポート
from icrawler.builtin import GoogleImageCrawler

# Google用クローラーの生成
google_crawler = GoogleImageCrawler(
    downloader_threads=4,
    storage={'root_dir': '/content/drive/Mydrive/anisakis_app/datas1'})

google_crawler.crawl(keyword='anisakis', max_num=200, min_size=None, max_size=None, )

google_crawler = GoogleImageCrawler(
    downloader_threads=4,
    storage={'root_dir': '/content/drive/Mydrive/anisakis_app/datas2'})

google_crawler.crawl(keyword='アニサキス', max_num=200, min_size=None, max_size=None, )















