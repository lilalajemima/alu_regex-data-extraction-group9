regex_patterns = {
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'url': r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[\w-./?%&=]*)?',
    'phone_number': r'\(?\d{3}\)?[.\s-]?\d{3}[.\s-]?\d{4}',
    'credit_card': r'\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}',
    'time_24h': r'([01]\d|2[0-3]):[0-5]\d',
    'time_12h': r'(1[0-2]|0?[1-9]):[0-5]\d\s?(AM|PM|am|pm)',
    'html_tag': r'<[a-zA-Z][^>]*?>',
    'hashtag': r'#\w+',
    'currency': r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
}
New test data sample for each features test_data = {
    'email': ['jane_doe23@website.net', 'contact@business.co.jp', 'support@domain.org'],
    'url': ['https://shop.example.io/products', 'http://docs.sample-site.com/manual'],
    'phone_number': ['(555) 123-4567', '987-654-3210', '555.987.6543'],
    'credit_card': ['4321 8765 2109 6543', '4321-8765-2109-6543'],
    'time_24h': ['09:15', '23:59'],
    'time_12h': ['10:45 AM', '11:15 PM', '6:00 pm'],
    'html_tag': ['<h1>Hello World</h1>', '<span class="highlight">Text</span>', '<a href="link.html">Click here</a>'],
    'hashtag': ['#CoolTech', '#PythonRocks', '#100DaysOfCode'],
    'currency': ['$5.00', '$999.99', '$12,345.67']
}
