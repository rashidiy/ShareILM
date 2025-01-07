from django.contrib.auth import mixins
from django.shortcuts import redirect,render
from django.contrib.auth import logout
from apps.models.books import Book

from accounts.utils.email_verification import RedisDataStore


class LoginAndVerificationRequiredMixin(mixins.LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_email_verified:
            if RedisDataStore.is_expired(f'ev:{request.user.email}'):
                RedisDataStore.send_verification_code(request.user.email)
            return redirect('accounts:email_verification')
        return super().dispatch(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    return redirect('home')


def search_results(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # Yoki boshqa xususiyatlar
    return render(request, 'booksaw/search_results.html', {'books': books, 'query': query})