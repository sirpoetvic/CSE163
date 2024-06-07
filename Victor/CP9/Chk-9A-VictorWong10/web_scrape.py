import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_selector_table():
    """
    Reads a webpage and extracts out the contents of a table.
    https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#reference_table_of_selectors

    Returns a dataframe with the content:
    Selector            Example        Description
    .class	            .intro	       Selects all elements with class="intro"
        .class1.class2	    .name1.name2   Selects all elements with both name1 and name2...
    .class1 .class2	    .name1 .name2  Selects all elements with name2 that is a desc...
        #id	                #firstname	   Selects the element with id="firstname"
    <60 rows>
    """
    url = "https://www.w3schools.com/cssref/css_selectors.asp"
    page = requests.get(url)
    # create a beautiful soup object that can parse the HTML content
    obj = BeautifulSoup(page.content, "html.parser")
    # get the table markup from soup object
    table = obj.find("table")
    # parse the 3 columns by getting the <td> data that is a child of <tr>
    rows = obj.find_all("tr")[1:]

    # create a list for each column, getting the text content as needed
    selector, example, ex_desc = [], [], []

    for row in rows:
        trd = row.find_all("td")
        selector.append(trd[0].get_text())
        example.append(trd[1].get_text())
        ex_desc.append(trd[2].get_text())

    # Create and return a dataframe using the lists created above
    lists = pd.DataFrame(
        {
            "Selector": selector,
            "Examples": example,
            "Example Description": ex_desc,
        }
    )

    return lists


def main():
    print(get_selector_table())


if __name__ == "__main__":
    main()
