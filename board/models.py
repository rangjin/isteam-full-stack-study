from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글들'


class Comment(models.Model):
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="작성자")
    board = models.ForeignKey('board.Board', on_delete=models.CASCADE, verbose_name="게시글")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'
        verbose_name_plural = '댓글들'