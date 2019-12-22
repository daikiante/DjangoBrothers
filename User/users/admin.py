from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User


class MyUserChangeForm(UserChangeForm):
    """User 情報を変更するフォーム"""
    class Meta:
        model = User
        # 全ての情報を変更可能
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    """User を作成するフォーム"""
    class Meta:
        model = User
        # emailとパスワードが必要
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    """カスタムユーザーモデルの Admin"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissiond'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_)
    )