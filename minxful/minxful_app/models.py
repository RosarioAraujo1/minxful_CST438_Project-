from django.db import models
from django.utils import timezone
import django.contrib.auth.models as dcam
from django.contrib.auth.models import User

class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'wdland'

class Post(BaseModel):
    """ a post class """

    title_text = models.TextField(default=None)
    body_text = models.TextField()
    ##pub_date = models.DateTimeField("published", default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{:^30} \n {:^30}".format(self.title_text, self.body_text)

    def snippet(self):
        return self.body_text[:20] + " ....."


class Reply(BaseModel):
    """ A reply class """
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    body_text = models.CharField(default="", max_length=1000)
    pub_date = timezone.now().isoformat().split("T")[0]
    pub_time = timezone.now().isoformat().split("T")[1].split(".")[0]

    def __str__(self):
        """new line in temp variable so it works with str.format(...), useing
        print to make sure formatting works, in future should remove print and
        return only string so it can be used elseware."""

        nl = "\n"

        return "{:<13} {!r} on {} at {}|{} {:^30}".format(
            "replying to:", self.parent, self.pub_date, self.pub_time, nl,
            nl.join([self.body_text]))


