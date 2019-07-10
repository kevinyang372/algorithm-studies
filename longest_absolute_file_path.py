# Suppose we abstract our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.

# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

def lengthLongestPath(input):
    if not input: return 0
    
    temp = [0]
    for ind in range(len(input)):
        if input[ind:ind + 1] == '\n' and input[ind + 1:ind + 2] != '\t':
            temp.append(ind + 1)
    
    temp.append(len(input) + 1)
    
    stack = [[input[temp[i]:temp[i + 1] - 1], 0, 1] for i in range(len(temp) - 1)]
    max_length = 0
    
    while stack:
        node, base, level = stack.pop()
        res = []
        
        for ind in range(len(node)):
            if node[ind:ind + level + 1] == '\n' + level*'\t' and node[ind + level + 1:ind + level + 2] != '\t':
                res.append(ind)
        
        if not res:
            if '.' in node:
                base += len(node)
                max_length = max(base, max_length)
        else:
            base += len(node[:res[0]]) + 1
            res.append(len(node))
        
            for s in range(len(res) - 1):
                stack.append([node[res[s] + level + 1:res[s + 1]], base, level + 1])
    
    return max_length