import sys
import time
import os
from datetime import datetime
from crawler_logic import executor
from crawler_logic import CrawlerLogic
from utiles import global_internal_list
from utiles import global_external_list
from utiles import write_to_file
from utiles import global_broken_links_list

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# crawler
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

SEC_TO_SLEEP = 3


class Crawler:

    @staticmethod
    def crawl(home_page_url):
        start_time = datetime.now()
        print("Crawling in progress")
        CrawlerLogic.get_all_links_from_page_recursive(home_page_url, 0)
        time.sleep(SEC_TO_SLEEP)
        executor.shutdown(wait=True)

        path = os.getcwd() + "/links.txt"

        if os.path.exists(path):
            os.remove(path)

        write_to_file(global_external_list)
        write_to_file(global_internal_list)
        write_to_file(global_broken_links_list)

        end_time = datetime.now()
        file = open("links.txt", "a")
        file.write('Duration: {}'.format(end_time - start_time))
        file.close()
        print("crawling ended successfully")
        print("Results in file - links.txt")


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# main
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

if __name__ == '__main__':
    url = sys.argv[1]
    Crawler.crawl(url)
