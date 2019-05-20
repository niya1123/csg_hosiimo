from django.db import models
from django.utils import timezone

from users.models import User
# from datetime import datetime


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 現在時刻の表示
    display_date = models.DateTimeField(
        verbose_name='投稿日時',
        default=timezone.now,
        editable=False,
    )

    # 名前入力。英名も考慮してmax_lengthは20としている。
    name = models.CharField(
        verbose_name='お名前',
        max_length=20,
    )

    # slackの@名。どちゃくそ長い名前の人がいるとだめなのでmax_lengthは多めにとってる。
    slack_name = models.CharField(
        verbose_name='slackの@名',
        max_length=10000,
    )

    # 部費か会費の選択。
    choice = (
        (1, '部費'),
        (2, '会費'),
    )

    # 選択の表示
    buhi_or_kaihi = models.IntegerField(
        verbose_name='部費か会費か',
        choices=choice,
    )

    # 何がほしいかを聞く。
    what_do_you_want = models.TextField(
        verbose_name='何がほしいか',
    )

    # なぜ欲するのか。
    why_do_you_want = models.TextField(
        verbose_name='何故ほしいのか、その理由',
    )

    # 欲しいものURL
    url = models.CharField(
        verbose_name='欲しいもののURL',
        max_length=100000,
        blank=True,
        null=True,
    )

    # 欲しいものの価格
    price = models.IntegerField(
        verbose_name='欲しいものの価格',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
