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
