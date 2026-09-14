from django.db import models

class Group(models.Model):
    class Meta:
        ordering = ["created"]

    title = models.CharField(max_length=255)
    
    # Possible options when deleting an account:
    # - owner has to either delete groups or transfer ownership
    # - owner becomes null, any participant can claim ownerhsip
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    participants = models.ManyToManyField(
        "auth.User", related_name="groups"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    # other datetime that may need to be added:
    # - updated at
    # - last settled at
    # - last transaction added at

    def __str__(self) -> str:
        return self.title

class Transaction(models.Model):
    amount = models.IntegerField()

class TransactionPart(models.Model):
    pass