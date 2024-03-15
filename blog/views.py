from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    """Создание блога"""
    model = BlogPost
    fields = ('title', 'content', 'creation_date', 'publication_sign', 'views')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Создание динамического slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    """Обновление блога"""
    model = BlogPost
    fields = ('title', 'content', 'creation_date', 'publication_sign', 'views')

    def get_success_url(self):
        """Перенаправление после редактирования на просмотр блога"""
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogPostListView(ListView):
    """Для страницы с блогами"""
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        """Метод для вывода только тех блогов, где подтверждена публикация"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogPostDetailView(DetailView):
    """Для подробного описания блога"""
    model = BlogPost

    def get_object(self, queryset=None):
        """Метод для увеличения счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BLogPostDeleteView(DeleteView):
    """Для удаления блога"""
    model = BlogPost
    success_url = reverse_lazy('blog:list')
