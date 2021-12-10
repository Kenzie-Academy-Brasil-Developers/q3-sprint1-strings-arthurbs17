def standardize_names(character_name):
    standard_name = character_name.strip().split(' ')
    return '-'.join(standard_name)

def standardize_title(title):
    standard_title = title.title()
    return standard_title

def standardize_text(text):
    standard_text = text.split()
    standard_text[0] = standard_text[0].capitalize()
    for i in range(len(standard_text)-1):
        if standard_text[i].endswith('.'):
           standard_text[i + 1] = standard_text[i + 1].capitalize()
    
    return ' '.join(standard_text)

def title_creator(text):
    return (f'--------------------{text.title()}--------------------')

def text_merge(text_of_blog_a, text_of_blog_b):
    split_text_a = text_of_blog_a.split()
    split_text_b = text_of_blog_b.split()
    split_text_a[-1] = split_text_a[-1].rstrip('.')
    split_text_b[0] = split_text_b[0].lower()
    new_text = split_text_a + split_text_b
    new_text[0] = new_text[0].capitalize()
    for i in range(len(new_text)-1):
        if new_text[i].endswith('.'):
           new_text[i + 1] = new_text[i + 1].capitalize()

    return ' '.join(new_text)