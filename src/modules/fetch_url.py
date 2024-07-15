import json
import urllib
import urllib2

from unittest import result


class Fetcher:
    """
    A class to fetch data from a base URL for a list of domains.
    """

    def fetch_data(self, domain, base_url):
        """
        Fetch data from a URL and add the domain to the response.

        :param domain: The domain to fetch data from.
        :param base_url: The base URL to fetch data from.
        :return: A dictionary containing the fetched data and domain.
        """
        url = base_url.format(domain)
        try:
            response = urllib2.urlopen(url)
            data = response.read()
            response.close()
            return json.loads(data)
        except urllib2.URLError as e:
            return {"success": False,"messageDetail": str(e), "domain": domain}

    def post_data(self, url, data):
        """
        Post data to a URL.

        :param url: The URL to post data to.
        :param data: The data to post.
        :return: The response from the POST request.
        """
        encoded_data = urllib.urlencode(data)
        req = urllib2.Request(url, encoded_data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')

        try:
            response = urllib2.urlopen(req)
            result = response.read()
            response.close()
            return json.loads(result)
        except urllib2.URLError as e:
            return {"success": False,"messageDetail": str(e)}


    def fetch_all(self, domains, base_url):
        """
        Fetch data from all domains using the base URL.

        :param domains: The list of domains to fetch data from.
        :param base_url: The base URL to fetch data from.
        :return: A list of dictionaries containing the fetched data.
        """
        responses = []
        for domain in domains:
            responses.append(self.fetch_data(domain, base_url))
        return responses



if __name__ == "__main__":
    base_url = "http://{}/operation/historicalPortfolioClosure"
    fetcher = Fetcher()
    
    results = fetcher.fetch_all(['api.mx.moderna.local.com', 'api.mx.moderna.local.com'], base_url)
    # results = fetcher.post_data('http://api.mx.caprepa.local.com/administration/smsVoices', {'message': 'Prueba de mensaje', 'number': '526675257721'})
    # print(results)

