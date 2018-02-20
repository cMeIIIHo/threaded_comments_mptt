from django_comments.abstracts import CommentAbstractModel
from mptt.models import MPTTModel, TreeForeignKey


class ThComment(MPTTModel, CommentAbstractModel):

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['submit_date']
