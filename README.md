# sreality.cz scraper and analytical tool 

## Description
#### *NOTE: This is a WIP and was hacked over a span of 2 or so hours - I suggest you read the LICENSE in full - below and in the LICENSE file*
sreality.cz crawler is a Python-based tool designed to fetch and display real estate listings from the Sreality API based on user-defined criteria such as location, price range, and other relevant property details. This tool offers both a command-line interface and an interactive mode, allowing users to refine their search for properties efficiently.

## Features

- Fetch real estate listings from the Sreality.cz API.
- Interactive mode for dynamic search criteria input.
- Filter listings by location, price range, and additional parameters.
- Display detailed property information including description, price, and contact details.
- Generate direct and API URLs for each property listing.
### COMING SOON
- working DB 
- visualizations in real-time
- stats
- analytics
- filtering
## Installation

### Prerequisites

- Python 3.x
- Requests library
- Colorama library

### Setup

1. Clone the repository to your local machine:
   \```bash
   git clone https://github.com/yourusername/realestate-crawler.git
   cd realestate-crawler
   \```
2. Install the required Python packages:
   \```bash
   pip install -r requirements.txt
   \```

## Usage

To start the Real Estate Crawler in interactive mode, run the following command in your terminal:
\```bash
python3 main.py --mode interactive
\```
Follow the on-screen prompts to specify your search criteria.

## Configuration

Environmental variables can be set to configure the API base URL and request timeout. Create a `.env` file in the project root with the following content:
\```makefile
SREALITY_BASE_URL=https://www.sreality.cz/api/cs/v2/
REQUEST_TIMEOUT=30
\```

## Contributing

Contributions to the Real Estate Crawler are welcome. Please follow the standard fork-and-pull request workflow. If you plan to introduce a significant change, it's best to discuss it first by opening an issue.

## License

This project is licensed under the I Don't Give A Fuck Public License (IDGAFPL). The full license text is as follows:

```
(C) 2016 My2ndAngelic.

I don't give a fuck about how this will be used. Everything will be allowed, including changing the name, citing wrongly, claiming ownership and destroying the computer. You are allowed to do anything with this as long as:

0. I don't give a fuck.
1. You agree that you don't give a fuck.
2. You agree that your use of this will have nothing to fuck with me now and in the future.
3. You don't fuck me legally/illegally.

As long as you agree with these term, you are free to do fucking anything, whether legal or not legal in your country, because I don't give a fuck. If you don't agree with my term, fuck off.
```

## Acknowledgments

- Thanks to the Seznam a.s for their funny unlimited API for providing access to real estate listings.
- This project is not officially associated with Sreality.cz and is just a hobby project. 
- Everything is under the IDGFAPL and that means, I do not give a fuck who, what and where the code is being used or what not.
