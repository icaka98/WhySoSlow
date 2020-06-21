from bs4 import BeautifulSoup
import requests
import pdfkit

url = 'https://blog.deeplearning.ai/blog/the-batch-happy-new-year-hopes-for-ai-in-2020-yann-lecun-kai-fu-lee-anima-anandkumar-richard-socher'
url2 = 'https://blog.deeplearning.ai/blog/the-batch-google-achieves-quantum-supremacy-amazon-aims-to-sway-lawmakers-ai-predicts-basketball-plays-face-detector-preserves-privacy-0-1-0-0-0-0-0-0'

result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

template_table = soup.find('div', {'class': 'blog-section'})

content = str(template_table).encode("utf-8")
print(template_table)

html_file = open("table.html", "wb")
html_file.write(content)
html_file.close()

pdfkit.from_file('table.html', 'out.pdf')
