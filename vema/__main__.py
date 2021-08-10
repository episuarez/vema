import argparse
import click

from . import Vema
from .src import routers

parser = argparse.ArgumentParser(description="Vema manager");
parser.add_argument("-gr", action="store_true", default=False, help="Generate the routers. Caution! Overwrites the file.");
parser.add_argument("-build", action="store", dest="domain", help="Generate static pages.");
parser.add_argument("-run", action="store_true", default=False, help="Launch web server (Development environments)");
parser.add_argument("-run-debug", action="store_true", default=False, help="Launch the web server (development environments)(debug mode)");

args = parser.parse_args();

if args.gr:
    click.progressbar(routers.generate_routers(), label="Generating routers...", length=1);
    print("Router file has been generated.");

if args.run:
    app = Vema(args.domain);
    app.run();

if args.run_debug:
    app = Vema(args.domain);
    app.run(debug=True);

if args.domain != None:
    if len(args.domain) > 10:
        app = Vema(args.domain);
        click.progressbar(app.compile(), label="Generating static web...", length=1);
        print("Static web has been generated.");
    else:
        print("A valid domain name is required.");