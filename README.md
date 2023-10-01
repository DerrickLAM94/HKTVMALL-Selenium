# HKTVMALL-Selenium Data Crawler

This repository contains a data crawler built to conduct market research and analysis for top local online retailers in the Parenting and Baby category. The crawler collects data and stores it in a database, enabling analysts and market researchers to gain insights and better understand the competition.

## Features

- Automated data crawling for top local online retailers in the Parenting and Baby category.
- Data storage in a database for further analysis.
- Customizable configuration options for data collection.

## Installation

To use the HKTVMALL-Selenium Data Crawler, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the command: `pip install -r requirements.txt`.
3. Configure the database connection in `database.py`.
4. Customize the crawling parameters in `hktvmall_scraping.py` as per your requirements.
5. Run the `hktv.py` script to start the data crawling process.
6. Analyze the collected data stored in the database using your preferred tools.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your modifications and ensure the code follows the project's coding standards.
4. Test your changes thoroughly.
5. Submit a pull request detailing your changes.

## Resources

- [Documentation](https://github.com/DerrickLAM94/HKTVMALL-Selenium/blob/main/README.md)
- [Issue Tracker](https://github.com/DerrickLAM94/HKTVMALL-Selenium/issues)

<img width="605" alt="Library" src="https://github.com/DerrickLAM94/HKTVMALL-Selenium/assets/140989898/e5522ba4-1a3b-4d86-811f-2d6604de8b96">

- Importing Dependencies:
- The script starts by importing various modules from the Selenium library, as well as other necessary libraries like Pandas, time, and os.

<img width="907" alt="URL Link" src="https://github.com/DerrickLAM94/HKTVMALL-Selenium/assets/140989898/df1444a1-45ee-41e3-9d0a-19509dc07eab">

- Defining the List of URLs:
- It defines a list called urls containing multiple URLs to different product search pages on the HKTVMall website. Each URL corresponds to a specific category or search criteria.

<img width="880" alt="selenium" src="https://github.com/DerrickLAM94/HKTVMALL-Selenium/assets/140989898/f7fc531e-2df2-451d-a690-7e00c7235a89">

- Scraping Product Details:
- The script uses Selenium to find product elements on the current page using XPath selectors.
For each product, it extracts information such as product name, number of items sold, original price, promotional price, store name, URL, image URL, and review count.
This information is stored in a dictionary called product_info and added to the product_info_list.

<img width="423" alt="Pandas" src="https://github.com/DerrickLAM94/HKTVMALL-Selenium/assets/140989898/436624dc-b2b0-4243-96d3-4b49e83c58c6">

- Storing Data in CSV:
For each URL, the script creates a Pandas DataFrame df from the product_info_list and saves it as a CSV file with a unique filename in the specified folder.


