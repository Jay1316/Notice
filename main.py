from util import Util

if __name__ == "__main__":
    url = input("Enter the site you wanna scrap: ")
    print("Enter login details")
    username = input("Username: ")
    password = input("Password: ")

    util = Util(url, username, password)

    util.login()
    # print(util.getUrl())

    notices = [link.get('href') for link in util.getSoup().find_all('a') if 'notice' in link.get('href')]
    notices.pop(0)

    contents = []
    for notice in notices:
        util.openSite(notice)
        content = str(util.getSoup().find_all('div', {'class': 'col-sm-12'})[0])
        content = content.split('>')
        contents.append(util.clean(content))

    count = 1
    for content in contents:
        print(f"Notice {count}")
        for line in content: print(line)
        count += 1
