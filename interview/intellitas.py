# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
 
# def count_posts(request):
#     users = User.objects.all()
#     posts_count = 0
#     for user in users:
#         posts_count += us


# for user in users:
#     post = user.post_all().count()



# def foo(attrs, my_list=[], my_dict={}):
#     pass


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def valid_parenthesis(string):
    stack = []
    dictionary = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in [')', ']', '}']:
            if not stack or dictionary[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack


inputs = ["()", "()[]{}", "(]",  "([])"]

for input in inputs:
    result = valid_parenthesis(input)
    print(result)


import random


def mutable_params(abc=[], csdf={}):
    # csdf[random.randint(0, 9)] = 'hey'
    abc.append(5)
    return abc, csdf


result = mutable_params([5])
print(result)
result = mutable_params()
print(result)
