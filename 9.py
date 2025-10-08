punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
text = "Hello!!!, welcome??? to -- Python."

no_punct = "".join(ch for ch in text if ch not in punctuations)
print(no_punct)
