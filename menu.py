from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        # check for account
        # if not, prompt for account creation
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        # User read or write blogs
        # if read:
            # list blogs
            # allow user to pick one
            # display posts
        # if write:
            # check if user has a blog
            # if they do, prompt to write a new post
            # if not, prompt for blog creation
        read_or_write = input("Do you want to read (R) or write(W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        if read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find('blogs', {})
        for blog in blogs:
            print("id: {}, title: {}, 'author: {}".format(
                blog['id'],
                blog['title'],
                blog['author']
            ))

    def _view_blog(self):
        blog_to_see = input("Enter id of blog to be viewed: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts(blog.id)
        for post in posts:
            print("date: {}, title: {}/n/n{}".format(
                post['created_date'],
                post['title'],
                post['content']
            ))
