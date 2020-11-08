from database import Database
from models.post import Post
from models.blog import Blog


Database.initialize()

# post = Post(blog_id="123",
#             title="Another great post",
#             content="This is some sample content",
#             author="Casey"
# )
#
# post.save_to_mongo()

# posts = Post.from_blog('123')
#
# for post in posts:
#     print(post)

# blog = Blog(author="Casey",
#             title="Sample title",
#             description="Sample description"
#             )
#
# blog.new_post()
#
# blog.save_to_mongo()
#
from_database = Blog.from_mongo('8237c11b47e845788bf973441a6233b2').json()
#
# print(blog.get_posts())

print(from_database)