from django.contrib import admin
from .models import (
    Department, Team, Role, TeamMember,
    Dependency, ContactChannel, Repository, AuditLog
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_head', 'team_count')
    search_fields = ('department_name',)

    def team_count(self, obj):
        return obj.teams.count()
    team_count.short_description = 'Teams'

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'department', 'team_leader', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('team_name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)
    search_fields = ('role_name',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role_in_team')
    list_filter = ('team',)

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ('source_team', 'target_team', 'dependency_type')
    list_filter = ('dependency_type',)

@admin.register(ContactChannel)
class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ('team', 'channel_type', 'channel_value')

@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('repo_name', 'team', 'repo_url')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('entity_name', 'action', 'user', 'timestamp')
    readonly_fields = ('timestamp',)