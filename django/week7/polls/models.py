from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date poll was published')

    def __str__(self):
        return "{0} - ({1})".format(self.question_text, self.id)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text    
