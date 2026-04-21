d = 0
emoji = input()
d = d+ len(emoji)
d = d+  emoji.count(':')
d = d+ (5* emoji.count('_'))
print(d)
