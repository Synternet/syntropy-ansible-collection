import click
import jinja2


@click.command()
@click.argument("file_name")
@click.option(
    "--param",
    "-p",
    type=(str, str),
    multiple=True,
    help="Parameters to pass to the template.",
)
def command(file_name, param):
    """Jinja2 templating Command Line Interface"""
    with open(file_name, "r") as src_file:
        template = jinja2.Template(src_file.read())
        params = {key: value for key, value in param}
        config_contents = template.render(**params)
        click.echo(config_contents)


if __name__ == "__main__":
    command()
