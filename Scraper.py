def get_links():
    urls = []
    data = bs(requests.get("http://www.yes24.com/24/Category/BestSeller").content)
    booklinks = data.find_all(class_='copy')
    for i in range((len(booklinks))):
        urls.append("http://www.yes24.com/" + booklinks[i].a['href'])
    return urls


def get_data(urls):
    titles = []
    ratings = []
    authors = []
    dates = []
    prices = []
    discounts = []
    for i in urls:
        data = bs(requests.get(i).content)
        if len(requests.get(i).content) > 1000:

            titles.append(data.find(class_='gd_titArea').get_text(strip=True))
            authors.append(data.find(class_='gd_auth').get_text(strip=True))
            dates.append(data.find(class_='gd_date').get_text(strip=True))
            ratings.append(data.find(class_='yes_b').get_text(strip=True))

            price_discount = data.find(class_='accentRow').text.split()
            prices.append(price_discount[1])
            discounts.append(price_discount[2] + price_discount[3])
        else:
            titles.append('restricted access')
            authors.append('restricted access')
            dates.append('restricted access')
            ratings.append('restricted access')
            prices.append('restricted access')
            discounts.append('restricted access')

    return titles, authors, dates, ratings, prices, discounts


def save_file(titles, authors, dates, ratings, prices, discounts):
    file1 = open("/home/myfile.txt", "a")  # change to your txt file path
    file1.truncate(0)
    for i in range(len(titles)):
        file1.write("Title: " + titles[i] + "\n")
        file1.write("Author(s): " + authors[i] + "\n")
        file1.write("Date: " + dates[i] + "\n")
        file1.write("Rating: " + ratings[i] + "\n")
        file1.write("Price: " + prices[i] + "\n")
        file1.write("Discount: " + discounts[i] + "\n \n \n \n")
    file1.close()


titles, authors, dates, ratings, prices, discounts = get_data(get_links())
save_file(titles, authors, dates, ratings, prices, discounts)

file1 = open("/home/myfile.txt", "a")
file1.truncate(0)
for i in range(len(titles)):
    file1.write("Title: " + titles[i] + "\n")
    file1.write("Author(s): " + authors[i] + "\n")
    file1.write("Date: " + dates[i] + "\n")
    file1.write("Rating: " + ratings[i] + "\n")
    file1.write("Price: " + prices[i] + "\n")
    file1.write("Discount: " + discounts[i] + "\n \n \n \n")
file1.close()

