#hw1
# import random
# def get_random_language(languages):
#     random_language = random.choice(languages)
#     with open('results.txt', 'a') as results_file:
#         results_file.write(random_language + '\n')
#     return random_language

# language_list = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# random_language = get_random_language(language_list)
# print(random_language)

#hw2
# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""

# with open('text.txt', 'w') as file:
#     file.write(text)
    
# with open('text.txt', 'r') as file:
#     print(file.read())


# 2 способ
# f = open('text.txt', 'w')
# f.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.""")
# f.close()

# r = open('text.txt', 'r')
# print(r.read())
# r.close()

#hw 3
# with open('text.txt', 'r') as file1, open('wikipedia.txt', 'w') as file2:
#     text = file1.read()
#     file2.write(text)