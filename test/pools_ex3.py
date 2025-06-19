
import time
import os
import concurrent.futures

img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]
import logging
logging.basicConfig(filename='processes.log', level=logging.DEBUG,
                    format='%(asctime)s  %(process)d %(thread)d %(levelname)s: %(message)s'
                    )
logger = logging.getLogger(__name__)
from time import sleep
def download_image(img_url):
    #img_bytes = requests.get(img_url).content
    logger.info(f"[Process ID]:{os.getpid()} Downloading..")
    sleep(5)
    logger.info(f"[Process ID]:{os.getpid()} Downloading finished")

def task1(name):
    # sleep for less than a second
    logger.info(f'[Process ID]:{os.getpid()} arg:{name}')
    sleep(3)
    logger.info(f'[Process ID]:{os.getpid()} arg:{name} finsihed')
    return f'process {os.getpid()} {name}'
def task2(name):
    # sleep for less than a second
    logger.info(f'[Process ID]:{os.getpid()} arg:{name}')
    sleep(5)
    logger.info(f'[Process ID]:{os.getpid()} arg:{name} finsihed')
    return f'process {os.getpid()} {name}'

def main():
    t1 = time.time()
    print("Downloading images with Multiprocess")

    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(1) as executor:
        executor.map(download_image, img_urls)
        '''
        for i in range(5):
            future1 = executor.submit(task1, str(i))

        # below code will wait for previous submit processes finished
        for i in range(11, 15):
            future2 = executor.submit(task2, str(i))

        future1 = executor.submit(task1, 'task1 ')
        future2 = executor.submit(task1, 'task2 ')
        '''
    t2 = time.time()
    print(f'Multiprocess Code Took:{t2 - t1} seconds')


if __name__ == '__main__':
    main()