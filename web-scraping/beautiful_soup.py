from bs4 import BeautifulSoup 
import requests  
def main():
    
    # BeautifulSoup objects
    html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
    soup = BeautifulSoup(html, 'html5lib')
    print("HTML DOC:\n", soup.prettify())

    # Tags
    tag_object = soup.title
    print("Tag Object:", tag_object)
    print("Tag Object Type:", type(tag_object))

    # For more than one tag objects of the same name, the first element with that Tag name is called (corresponds to the most paid player).
    tag_object = soup.h3
    print(tag_object)

    # Children, Parents and Siblings
    tag_child = tag_object.b 
    print("Child:\n", tag_child)
    parent_tag = tag_child.parent
    print("Parent:\n", parent_tag)
    print("Body element:\n", tag_object.parent)
    sibling_1 =  tag_object.next_sibling
    print("Paragraph element:", sibling_1)
    sibling_2 = sibling_1.next_sibling
    print("Header element:", sibling_2)

    print("Salary of Stephen Curry:\n", sibling_2.next_sibling)

    # HTML attributes
    print(tag_child['id'])
    print(tag_child.attrs)
    print(tag_child.get('id'))

    # Navigable String
    tag_string = tag_child.string
    print(tag_string)
    print(type(tag_string))
    unicode_string = str(tag_string)
    print(unicode_string)

    # Filter
    table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
    table_bs = BeautifulSoup(table, 'html5lib')

    # Name
    table_rows = table_bs.find_all('tr')
    print(table_rows)
    first_row = table_rows[0]
    print(first_row)
    print(type(first_row))
    print(first_row.td)

    for i, row in enumerate(table_rows):
        print("row", i, "is", row)

    for i, row in enumerate(table_rows):
        print("row", i)
        cells = row.find_all('td')
        for j, cell in enumerate(cells):
            print("column", j, "cell", cell)

    list_input = table_bs.find_all(name = ["tr", "td"])
    print(list_input)

    # Attributes
    table_bs.find_all(id = "flight")
    list_input = table_bs.find_all(href = "https://en.wikipedia.org/wiki/Florida")
    print(list_input)
    table_bs.find_all(href=True)
    soup.find_all(id = "boldest")

    # String
    table_bs.find_all(string="Florida")

    # find
    two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
    two_tables_bs = BeautifulSoup(two_tables, 'html.parser')
    print(two_tables_bs.find("table"))
    print(two_tables_bs.find("table",class_='pizza'))

    # Downloading and scraping the contents of a web page
    url1 = "http://www.ibm.com"
    data = requests.get(url1).text
    soup = BeautifulSoup(data, 'html5lib')
    for link in soup.find_all('a', href = True): # Scrape all links
        print(link.get('href'))
    
    # Scrape all images Tags
    for link in soup.find_all('img'): 
        print(link)
        print(link.get('src'))

    url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
    data = requests.get(url2).text
    soup = BeautifulSoup(data, 'html5lib')
    table = soup.find('table') # find a html table in the web page

    for row in table.find_all('tr'): # row is represented by the tag <tr>
        cols = row.find_all('td') # column is represented by the tag <td>
        color_name = cols[2].string
        color_code = cols[3].string
        print("{}--->{}".format(color_name, color_code))


if __name__ == "__main__":
    main()