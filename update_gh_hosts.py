import ctypes, sys
import requests, re

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    sys.stderr.write("Cannot Retrive the Administrator Permission!")
    exit(0x233)

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
gh_hosts_url = "https://cdn.jsdelivr.net/gh/521xueweihan/GitHub520@main/hosts"
start_line = "# GitHub520 Host Start\n"
end_line = "# GitHub520 Host End\n"

new_gh_hosts_content = ["\n"]+requests.get(gh_hosts_url).text.splitlines(True)+["\n"]

hosts_file = open(hosts_path,"r+")

hosts_content = hosts_file.readlines() if hosts_file.readable() else []

bk = hosts_content

try:    # if github hosts exists
    idx_start = hosts_content.index(start_line)
    idx_end = hosts_content.index(end_line)
    hosts_content = hosts_content[:idx_start] + new_gh_hosts_content + hosts_content[idx_end+1:]
except:   # elif github hosts not exists
    hosts_content = hosts_content+new_gh_hosts_content

for i in range(len(hosts_content)-1):
    if hosts_content[i]=="\n" and hosts_content[i+1]=="\n":
        hosts_content[i] = ""

hosts_file.seek(0)
hosts_file.writelines(hosts_content)
hosts_file.close()
