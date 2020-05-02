"""Command Line Interface for projectdiffview."""
import distutils.dir_util as dir_util
import sys
from pathlib import Path

import click

from projectdiffview import projectdiffview, prompts
from PySide2.QtWidgets import QApplication


@click.group(
    invoke_without_command=True, context_settings=dict(help_option_names=["-h", "--help"])
)
@click.pass_context
@click.option("--verbose", "-vv", is_flag=True, help="Enable debug prints.")
@click.option("--debug", is_flag=True, help="Use the local debug directory.")
@click.version_option()
def cli(ctx, verbose, debug):
    """CLI for projectdiffview."""
    click.echo("Opening projectdiffview GUI.")
    ctx.obj = {"verbose": verbose, "debug": debug}
    if ctx.invoked_subcommand is None:
        app = QApplication([])
        gui = projectdiffview.projectdiffview(verbose=ctx.obj["verbose"], debug=ctx.obj["debug"])
        gui.show()
        prompts.warn_user()
        sys.exit(app.exec_())


@cli.command()
@click.pass_context
def clone(ctx):
    """Clone the full template folder into the current working directory."""
    app = QApplication([])
    gui = projectdiffview.projectdiffview(verbose=ctx.obj["verbose"], debug=ctx.obj["debug"])
    cwd = str(Path().cwd())
    click.echo(f"Cloning Template into: {cwd}")
    dir_util.copy_tree(
        str(gui.template_directory), str(cwd), preserve_symlinks=True, update=True,
    )
    gui.quit()
    sys.exit(app.exec_())


@cli.command()
@click.pass_context
def cleanup(ctx):
    """Clone the full template folder into the current working directory."""
    app = QApplication([])
    gui = projectdiffview.projectdiffview(verbose=ctx.obj["verbose"], debug=ctx.obj["debug"])
    gui.working_directory = Path().cwd()
    click.echo(f"Cleaning {gui.working_directory}...")
    gui.cleanup_working_folder()
    gui.quit()
    sys.exit(app.exec_())
