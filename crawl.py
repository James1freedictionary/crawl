import requests
from bs4 import BeautifulSoup
import time
import itertools
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import gc
import string

def g_char():
    except_char = ['\u17fa','\u17fb','\u17fc','\u17fd' ,'\u17fe','\u17ff'
                    ,'\u17ea','\u17eb','\u17ec','\u17ed','\u17ee','\u17ef'
                    ,'\u17de', '\u17df']
    for i in string.ascii_letters + string.digits:
        char.append(i)
    for i in string.digits[8:] + string.ascii_uppercase[:6]:
        for e in string.digits + string.ascii_uppercase[:6]:
            hax_s = "0x" + "17" + i + e
            char_from_hax_s = chr(int(hax_s, 16))
            if char_from_hax_s not in except_char:
                char.append(char_from_hax_s)
            else:
                pass
    del except_char
    gc.collect()

def split_char(n):
    num_part = 40 #split to number of part
    size_of_each_part = len(char) // num_part
    for i in range(num_part):
        if i != num_part -1:
            part = char[size_of_each_part * i:size_of_each_part * (i+1)]
        else:
            part = char[size_of_each_part * i:]
        if n == 0:
            yield ()
            break
        else:
            yield (part, *[char]*(n-1))

def g_product(i_in_total_char):
    product = itertools.product(*i_in_total_char)
    return ["".join(x) for x in product]

def pool(splitted_char):
    num_count_keywords = 1300 #num of count_keywords 
    with ProcessPoolExecutor() as exe:
        result = exe.map(g_product, splitted_char)
        for i in result:
            for e in i:
                count_keywords.append(e)
                if len(count_keywords) == num_count_keywords: 
                    threading(count_keywords)
                    for x in range(num_count_keywords): #delete element in count_keywords to release memory
                        del count_keywords[-1]
                        gc.collect()
            del i
            gc.collect()
    del num_count_keywords
    gc.collect()
        
def retry(func, limit=3):
    def wrapping(*arg):
        atempt = 0
        while atempt < limit:
            try:
                return func(*arg)
            except:
                print("error, try atempting")
                time.sleep(2)
                atempt += 1
        if atempt == 3:
            print(f"fail: {arg}")
            with open("fail.txt", "a") as f:
                f.write(f"fail: {arg}" + "\n")
            return "fail"
    return wrapping

@retry
def requests_and_bs(word):
    url = f"http://dictionary.tovnah.com/?q={word}&dic=all&criteria=start"
    s = requests.Session()
    r = s.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    t = soup.find(id = "box-wrap")
    if "Did you mean:" in str(t):
        del r, url, soup, t, s
        gc.collect()
        return "404"
    else:
        del url, s, r, soup
        print(word)
        with open("wordlist.txt", "a") as f:
            f.write(word + "\n")
        return word + "\n" + str(t).replace("\n", "")+ "\n" + "</>" +"\n"

def get_data(word):
    return requests_and_bs(word)

def threading(keywords):
    with ThreadPoolExecutor() as exe:
        result = exe.map(get_data, keywords)
        for i in result:
            if i != "404" and i != "fail":
                with open("crawl.txt", "a") as f:
                    f.write(i)
            del i
            gc.collect()

def do_task():
    for i in range(15): #number of element-product
        splitted_char = list(split_char(i))
        pool(splitted_char)
        del splitted_char
        gc.collect()
    threading(count_keywords) #end thread for remaining count_keywords
    del count_keywords, char
    gc.collect()

if __name__ == "__main__":
    char = []
    count_keywords = []
    g_char()
    do_task()
    print("you are done! happy coding!")
    with open("done.txt", "w") as f:
        f.write("you are done! happy coding!")
