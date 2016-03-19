# lnkr

A no-frills short link creator. Built with Python (Flask).


### Getting Started

System Requirements: Python, virtualenv, SQLite3. Required Python modules are installed during the steps below.

1. Clone this repo: `git clone https://github.com/peakwinter/lnkr`
2. Create a virtualenv: `cd lnkr; virtualenv venv`
3. Enter the virtualenv: `source venv/bin/activate`
4. Install and link required modules: `pip install -r requirements.txt`
5. Run the server: `lnkr run`


### Methods

 * Follow a shortlink: **GET** `/go/{id}`
 * Get info on all registered shortlinks: **GET** `/links`
 * Get info on a particular shortlink: **GET** `/links/{id}`
   * returns a JSON shortlink object, with `id`, `url` and `created` (timestamp)
 * Create a shortlink: **POST** `/links`
   * Send `{"shortlink": {"url": "http://mydomain.com"}}` as JSON; returns the JSON shortlink object it just created.
 * Delete a shortlink: **DELETE** `/links/{id}`

You can also create a shortened link via the command line: `lnkr add $URL`.
