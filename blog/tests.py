from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create(username='test1', password='12345')
        test_post = Post.objects.create(category_id=1, title='post title', excerpt='excerpt test', content='content test', slug='test', author_id=1, status='published')


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'test1')
        self.assertEqual(excerpt, 'excerpt test')
        self.assertEqual(str(cat), 'django')
        self.assertEqual(title, 'post title')
        self.assertEqual(content, 'content test')
        self.assertEqual(status, 'published')
        return super().setUpTestData()


# Create your tests here.
