import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from . import repository, db
from .utils import human_dt, parse_hours

console = Console()

@click.group()
def cli():
    """DevTrackr CLI"""
    pass

@cli.command('init-db')
def init_db_cmd():
    db.init_db()
    console.print('[green]Database initialized.[/green]')

@cli.command('add-dev')
@click.option('--name', prompt='Developer name')
@click.option('--email', default=None)
def add_dev(name, email):
    d = repository.create_developer(name=name, email=email)
    console.print(f'[green]Created developer:[/green] {d.id} - {d.name}')

@cli.command('list-devs')
def list_devs():
    devs = repository.list_developers()
    table = Table('ID','Name','Email')
    for d in devs:
        table.add_row(str(d.id), d.name, d.email or '')
    console.print(table)

@cli.command('edit-dev')
@click.argument('dev_id', type=int)
@click.option('--name', default=None)
@click.option('--email', default=None)
def edit_dev(dev_id, name, email):
    d = repository.edit_developer(dev_id, name=name, email=email)
    if not d:
        console.print(f'[red]Developer {dev_id} not found.[/red]')
    else:
        console.print(f'[green]Updated developer {d.id}[/green]')

@cli.command('delete-dev')
@click.argument('dev_id', type=int)
def delete_dev(dev_id):
    ok = repository.delete_developer(dev_id)
    if ok:
        console.print(f'[green]Deleted developer {dev_id}[/green]')
    else:
        console.print(f'[red]Developer not found.[/red]')

@cli.command('add-project')
@click.option('--developer-id', prompt='Developer ID', type=int)
@click.option('--title', prompt='Project title')
@click.option('--description', default=None)
def add_project(developer_id, title, description):
    p = repository.create_project(title=title, developer_id=developer_id, description=description)
    console.print(f'[green]Created project:[/green] {p.id} - {p.title}')

@cli.command('list-projects')
@click.option('--developer-id', default=None, type=int)
def list_projects(developer_id):
    projs = repository.list_projects(developer_id=developer_id)
    table = Table('ID','Title','Developer ID')
    for p in projs:
        table.add_row(str(p.id), p.title, str(p.developer_id))
    console.print(table)

@cli.command('edit-project')
@click.argument('project_id', type=int)
@click.option('--title', default=None)
@click.option('--description', default=None)
def edit_project(project_id, title, description):
    p = repository.edit_project(project_id, title=title, description=description)
    if not p:
        console.print(f'[red]Project {project_id} not found.[/red]')
    else:
        console.print(f'[green]Updated project {p.id}[/green]')

@cli.command('delete-project')
@click.argument('project_id', type=int)
def delete_project(project_id):
    ok = repository.delete_project(project_id)
    if ok:
        console.print(f'[green]Deleted project {project_id}[/green]')
    else:
        console.print(f'[red]Project not found.[/red]')

@cli.command('start-session')
@click.option('--project-id', prompt='Project ID', type=int)
@click.option('--notes', default=None)
def start_session_cmd(project_id, notes):
    s = repository.start_session(project_id=project_id, notes=notes)
    console.print(f'[green]Started session {s.id} for project {project_id} at {human_dt(s.started_at)}[/green]')

@cli.command('stop-session')
@click.argument('session_id', type=int)
def stop_session_cmd(session_id):
    s = repository.stop_session(session_id)
    if not s:
        console.print(f'[red]Session not found or already stopped.[/red]')
    else:
        console.print(f'[green]Stopped session {s.id}. Duration: {s.duration_hours} hours[/green]')

@cli.command('add-session')
@click.option('--project-id', prompt='Project ID', type=int)
@click.option('--hours', prompt='Hours')
@click.option('--notes', default=None)
def add_session_manual_cmd(project_id, hours, notes):
    hrs = parse_hours(hours)
    s = repository.add_session_manual(project_id=project_id, duration_hours=hrs, notes=notes)
    console.print(f'[green]Added manual session {s.id} | {s.duration_hours}h[/green]')

@cli.command('list-sessions')
@click.option('--project-id', default=None, type=int)
@click.option('--active', default=None, type=bool)
def list_sessions_cmd(project_id, active):
    rows = repository.list_sessions(project_id=project_id, active=active)
    table = Table('ID','Project','Hours','Active','Started At','Stopped At','Notes')
    for r in rows:
        table.add_row(str(r.id), str(r.project_id), str(r.duration_hours or ''), str(r.active), human_dt(r.started_at), human_dt(r.stopped_at), (r.notes or '')[:50])
    console.print(table)

@cli.command('delete-session')
@click.argument('session_id', type=int)
def delete_session_cmd(session_id):
    ok = repository.delete_session(session_id)
    if ok:
        console.print(f'[green]Deleted session {session_id}[/green]')
    else:
        console.print(f'[red]Session not found.[/red]')

@cli.command('add-hiccup')
@click.option('--project-id', prompt='Project ID', type=int)
@click.option('--title', prompt='Hiccup title')
@click.option('--details', default=None)
def add_hiccup_cmd(project_id, title, details):
    h = repository.add_hiccup(project_id=project_id, title=title, details=details)
    console.print(f'[green]Added hiccup {h.id}[/green]')

@cli.command('list-hiccups')
@click.option('--project-id', default=None, type=int)
@click.option('--resolved', default=None, type=bool)
def list_hiccups_cmd(project_id, resolved):
    rows = repository.list_hiccups(project_id=project_id, resolved=resolved)
    table = Table('ID','Project','Title','Resolved','Created At')
    for r in rows:
        table.add_row(str(r.id), str(r.project_id), r.title, str(r.resolved), human_dt(r.created_at))
    console.print(table)

@cli.command('edit-hiccup')
@click.argument('hiccup_id', type=int)
@click.option('--title', default=None)
@click.option('--details', default=None)
@click.option('--resolved', default=None, type=bool)
def edit_hiccup_cmd(hiccup_id, title, details, resolved):
    h = repository.edit_hiccup(hiccup_id, title=title, details=details, resolved=resolved)
    if not h:
        console.print(f'[red]Hiccup not found.[/red]')
    else:
        console.print(f'[green]Updated hiccup {h.id}[/green]')

@cli.command('delete-hiccup')
@click.argument('hiccup_id', type=int)
def delete_hiccup_cmd(hiccup_id):
    ok = repository.delete_hiccup(hiccup_id)
    if ok:
        console.print(f'[green]Deleted hiccup {hiccup_id}[/green]')
    else:
        console.print(f'[red]Hiccup not found.[/red]')

@cli.command('summary')
@click.option('--dev-id', default=None, type=int)
@click.option('--project-id', default=None, type=int)
def summary_cmd(dev_id, project_id):
    if dev_id:
        total = repository.total_hours_for_developer(dev_id)
        console.print(Panel(f'[bold]Developer {dev_id} Total Hours: {total}h[/bold]'))
        projs = repository.list_projects(developer_id=dev_id)
        table = Table('Project ID','Title','Hours')
        for p in projs:
            hrs = repository.total_hours_for_project(p.id)
            table.add_row(str(p.id), p.title, str(hrs))
        console.print(table)
    elif project_id:
        total = repository.total_hours_for_project(project_id)
        console.print(Panel(f'[bold]Project {project_id} Total Hours: {total}h[/bold]'))
    else:
        console.print('[yellow]Please provide --dev-id or --project-id for summary.[/yellow]')
