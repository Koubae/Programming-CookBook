from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 
import time 


def writerows(rows, filename):
    with open(filename, 'a', encoding='utf-8') as toWrite:
        writer = csv.writer(toWrite)
        writer.writerows(rows)
 

def getlistings(listingurl):
    '''
    scrap footballer data from the page and write to CSV
    '''

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        response = requests.get(listingurl, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    listings = []

    # loop through the table, get data from the columns
    for rows in soup.find_all("tr"):
        if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):          
                        
            name = rows.find("div", class_="name").a.get_text()
            hometown = rows.find_all("td")[1].get_text()
            school = hometown[hometown.find(",")+4:]
            city = hometown[:hometown.find(",")+4]
            position = rows.find_all("td")[2].get_text()
            grade = rows.find_all("td")[4].get_text()

            # append data to the list
            listings.append([name, school, city, position, grade])

    return listings


if __name__ == "__main__":
    '''
    Set CSV file name. 
    Remove if file alreay exists to ensure a fresh start
    '''
    filename = "footballers.csv"
    if os.path.exists(filename):
        os.remove(filename)
    
    '''
    Url to fetch consists of 3 parts:
    baseurl, page number, year, remaining url
    '''
    baseurl = "http://www.espn.com/college-sports/football/recruiting/databaseresults/_/page/" 
    page = 1
    parturl = "/sportid/24/class/2006/sort/school/starsfilter/GT/ratingfilter/GT/statuscommit/Commitments/statusuncommit/Uncommited"

    # scrap all pages
    while page < 259:
        listingurl = baseurl + str(page) + parturl
        listings = getlistings(listingurl)

        # write to CSV        
        writerows(listings, filename)

        # take a break
        time.sleep(3)

        page += 1

if page > 1:
    print("Listings fetched successfully.")