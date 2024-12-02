import chakin

print("Searching for English word vectors...")
results = chakin.search(lang='English')
for result in results:
    print(result)
