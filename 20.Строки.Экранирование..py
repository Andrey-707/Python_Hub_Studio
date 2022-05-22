# Python_Hub_Studio
# Python_7_Hours

# СТРОКИ. ЭКРАНИРОВАНИЕ.

# СИНТАКСИС СТРОК.

# Использование кавычек
s = "Lets write string as 's'"
print(s) # OUT: Lets write string as 's'

# альтернативный вариант использования кавычек
s = 'Lets write string as "s"'
print(s) # OUT: Lets write string as "s"

# Использование апострофа
s = "Let\'s write string as 's'"
print(s) # OUT: Let's write string as 's'

# Перенос строки.
s = "Lets \
write string as 's'"
print(s) # OUT: Lets write string as 's'

# Перенос строки.
s = "Lets \
write string \
as 's'"
print(s) # OUT: Lets write string as 's'

# Использование обратного слэша.
s = "Lets write\ string as 's'"
print(s) # OUT: Lets write\ string as 's'

# Использование обратного слэша. Перевод строки \n
s = "Lets write stri\ng as 's'"
print(s) # OUT: Lets write stri
#               g as 's'

# Использование обратного слэша.
url = "https:\www.youtube.com"
print(url) # OUT: https:\www.youtube.com

# Использование обратного слэша.
url = "https:\www.youtube.com\new"
print(url) # OUT: https:\www.youtube.com
#                 ew

# Использование обратного слэша.
url = "https:\www.youtube.com\\new"
print(url) # OUT: https:\www.youtube.com\new


# Использование обратного слэша.
import os

os.walk('D:\\')

# Использование обратного слэша.
url = "https:\\www.youtube.com\\new"
print(url) # OUT: https:\www.youtube.com\new

# Использование спец. символа, который означает "строка для чтения". НЕ происходит перевод строки \n
url = r"https:\www.youtube.com\new"
print(url) # OUT: https:\www.youtube.com\new

# Использование спец. символа, который означает "строка для чтения". НЕ происходит перевод строки \n
path = r"D:\path_to_file\File.txt"
print(path) # OUT: D:\path_to_file\File.txt
