class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'due_date')
    list_filter = ('due_date',)
    date_hierarchy = 'due_date'
    ordering = ('due_date',)
    filter_horizontal = ('book',)
    raw_id_fields = ('name',)

    class Book(models.Model):
        name = models.CharField(max_length=100)
        book = models.ManyToManyField(book)
        studentid = models.ForeignKey(name)
        due_date = models.DateField()

        def __unicode__(self):
            return self.title