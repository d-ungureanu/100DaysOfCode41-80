from bs4 import BeautifulSoup
import lxml


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# heading = soup.find(name="h1", id="name")
# print(heading.text)


# first_h3_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# companies_urls_list = soup.select(selector="p a")
# print(company_url)
# print(company_url.get("href"))
# print("_______________________________________")
# print(companies_urls_list)
# print(companies_urls_list[0])
# print(companies_urls_list[0].get("href"))

# all_h3_headings = soup.find_all("h3", class_="heading")
# print(all_h3_headings)


# id_name = soup.select("#name")
# print(id_name)

print("Using find_all() function: \n",soup.find_all("a"))
print("\n\n")
print("Using select funtion:\n", soup.select("a"))

