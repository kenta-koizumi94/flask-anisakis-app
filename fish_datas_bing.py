# Bing用クローラーのモジュールをインポート
from icrawler.builtin import BingImageCrawler

# Bing用クローラーの生成
bing_crawler = BingImageCrawler(
    downloader_threads=4,          # ダウンローダーのスレッド数
    storage={'root_dir': 'test_fish'}) # ダウンロード先のディレクトリ名

# クロール（キーワード検索による画像収集）の実行
bing_crawler.crawl(
    keyword="生魚　切り身",   # 検索キーワード（日本語もOK）
    max_num=10)                    # ダウンロードする画像の最大枚数


















