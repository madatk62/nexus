# Third Party Stuff
from django.contrib import admin

# nexus Stuff
from nexus.proposals.models import Proposal, ProposalKind


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Proposal info', {'fields': ('title', 'speaker', 'status', 'kind', 'level',
                                      'duration', 'abstract', 'description')}),
        ('Timing', {'fields': ('accepted_at',)}),
    )
    list_display = ('speaker', 'title', 'submitted_at', 'status')
    list_filter = ('speaker', 'submitted_at', 'status')
    ordering = ('submitted_at',)
    search_fields = ('speaker__email', 'speaker__first_name', 'speaker__last_name')


@admin.register(ProposalKind)
class ProposalKindAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Proposal details', {'fields': ('kind',)}),
    )
    list_display = ('kind',)
