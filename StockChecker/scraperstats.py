import time

class ScraperStats:
    def __init__(self):
        self.last_successful_scrape_time = {}
        self.total_response_time=0
        self.total_scrapped_data = {}

    def add_scrape(self, success: bool,product_name,website_name):
        product_value=total_scrapped_data.get(product_name)
        if product_value is None:
            total_scrapped_data[product_name] = {}
            total_scrapped_data[product_name][website_name] = {"Error":0, "Total": 1}
        else:
            count = product_value.get(website_name)
            if count is None:
                total_scrapped_data[product_name][website_name] = {"Error":0, "Total": 1}
            else:
                total_scrapped_data[product_name][website_name]["Total"]+=1
                if not succes:
                    total_scrapped_data[product_name][website_name]["Error"]+=1

    def success_rate(self,total_scrapped_data):
        success_rate_dict = {}
        for product_name in total_scrapped_data:
            websites_per_product = total_scrapped_data.get(product_name)
            success_rate_dict[product_name] = {}
            for website_name in websites_per_product:
                scrape_info_per_website = websites_per_product.get(website_name)
                #print(scrape_info_per_website)
                Error=scrape_info_per_website.get("Error")
                Total=scrape_info_per_website.get("Total")
                if Total == 0:
                    success_rate=0
                else:
                    success=Total-Error
                    success_rate=success / Total

                success_rate_dict[product_name][website_name] = success_rate
        print(success_rate_dict)



    def average_response_time(self):
        if self.successful_scrapes == 0:
            return 0.0
        return self.total_response_time / self.successful_scrapes

    def get_stats(self):
        return {
            "Total Scrapes": self.total_scrapes,
            "Successful Scrapes": self.successful_scrapes,
            "Failed Scrapes": self.failed_scrapes,
            "Success Rate (%)": self.success_rate(),
            "Average Response Time (s)": self.average_response_time(),
            "Last Successful Scrape Time": time.ctime(self.last_successful_scrape_time) if self.last_successful_scrape_time else "N/A"
        }








