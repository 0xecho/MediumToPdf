from googlesearch import search 
from weasyprint import HTML
import argparse
import sys
import xmltodict 
import requests

parser = argparse.ArgumentParser(description='Search Medium for a desired topic and save the top results in pdf format')
parser.add_argument('term', help="search term to use", nargs='+')

args = parser.parse_args()
term = " ".join(args.term)

# TODO: search term and get list of results :DONE
# TODO: take results, filter users and get xss feed of articles from medium :DONE
# TODO: filter articles by post and get content :DONE
# TODO: convert the content html or pdf :DONE
# TODO: worry about formatting
# TODO: accept path to store pdf files and number of files to download

query = f'site:medium.com {term}'

search_results = list(search(query, num=1, start=0, stop=5))

for result in search_results:
  userid = result.split('/')[3]
  post_slug = result.split('/')[4]
  feed_url = f"https://medium.com/feed/{userid}/"

  response = requests.get(feed_url)  
  xml_data = response.text

  rss_data = xmltodict.parse(xml_data)
  items_by_user = rss_data['rss']['channel']['item']

  for item in items_by_user:
    link = item['link']
    if 'content:encoded' in item and post_slug in link:
      content = item['content:encoded']
      filename = "-".join(link.split('?')[0].split('/')[-1].split('-')[:-1])+'.pdf'

      HTML(string=content).write_pdf('./'+filename)
print("[+] All Done ;)")
