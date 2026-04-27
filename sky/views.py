from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department, Team, Dependency

@login_required
def organisation_view(request):
    departments = Department.objects.prefetch_related('teams').all()
    dependencies = Dependency.objects.select_related(
        'source_team', 'target_team'
    ).all()
    return render(request, 'sky/organisation.html', {
        'departments': departments,
        'dependencies': dependencies,
    })

@login_required
def department_list(request):
    query = request.GET.get('q', '')
    departments = Department.objects.prefetch_related('teams')
    if query:
        departments = departments.filter(department_name__icontains=query)
    return render(request, 'sky/department_list.html', {
        'departments': departments,
        'query': query,
    })

@login_required
def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    teams = department.teams.prefetch_related(
        'members__user',
        'outgoing_dependencies__target_team',
        'incoming_dependencies__source_team',
        'contact_channels',
        'repositories'
    ).all()
    return render(request, 'sky/department_detail.html', {
        'department': department,
        'teams': teams,
    })

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    upstream = team.outgoing_dependencies.select_related('target_team').all()
    downstream = team.incoming_dependencies.select_related('source_team').all()
    return render(request, 'sky/team_detail.html', {
        'team': team,
        'upstream': upstream,
        'downstream': downstream,
    })