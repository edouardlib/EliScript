import click
import os

@click.command()
@click.option('--name', prompt='Name of the group to generate', help='Name of the group to generate.')
#@click.option('--name', prompt='Your name', help='The person to greet.')

def build(name):
	capitalizedName = name.capitalize()

	click.echo('Creating group named %s!' % name)
	os.mkdir(name)
	os.chdir(name)		
	vc = open(capitalizedName + 'ViewController.swift', 'wb')
	writeVC(vc)

	protocol = open(capitalizedName + 'Protocol.swift', 'wb')
	writeProtocol(protocol)

	presenter = open(capitalizedName + 'Presenter.swift', 'wb')
	writePresenter(presenter)

def writeVC(file):
	print 'Start writing view controllerr'

def writeProtocol(file):
	print 'Start writing protocol'

def writePresenter(file):
	print 'Start writing presenter'




if __name__ == '__main__':
    build()
