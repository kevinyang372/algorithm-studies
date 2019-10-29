# Given an absolute file path and a relative file path as inputs, write a function to determine the working directory after performing a cd command with the relative path as its argument.

# e.g.

# inputs:
# absolute path: "/bin/etc/abc"
# relative path: "/../xyz/tuv/../"

# output:
# "/bin/etc/xyz"

def findPath(absolute, relative):
	absolute = absolute.split('/')
	relative = relative.split('/')[1:-1]

	for i in relative:
		if i == '..':
			absolute.pop()
		else:
			absolute.append(i)

	return '/'.join(absolute)