from django.db import models


class TestModel(models.Model):
    """
    Base for test models that sets app_label, so they play nicely.
    """
    class Meta:
        app_label = 'tests'
        abstract = True


class ParentModel(TestModel):
    text = models.CharField(max_length=100, default='anchor')

    @property
    def child_ids(self):
        return list(self.children.values_list('id', flat=True))

    @property
    def old_child_ids(self):
        return list(self.old_children.values_list('id', flat=True))


class ChildModel(TestModel):
    parent = models.ForeignKey(ParentModel, related_name='children')
    old_parent = models.ForeignKey(ParentModel, related_name='old_children')


class OptionalChildModel(TestModel):
    parent = models.ForeignKey(ParentModel, blank=True, null=True,
                               related_name='optional_children')

class ReverseOneToOne(TestModel):
    pass

class OneToOne(TestModel):
    reverse_one_to_one = models.OneToOneField(
        ReverseOneToOne, related_name='one_to_one')
