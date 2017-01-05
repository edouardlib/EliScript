# encoding: utf-8

import click
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@click.command()
@click.option('--name', prompt='Name of the group to generate', help='Name of the group to generate.')
#@click.option('--name', prompt='Your name', help='The person to greet.')

def build(name):
	capitalizedName = name.capitalize()

	click.echo('Creating group named %s!' % name)
	os.mkdir(name)
	os.chdir(name)		
	vc = open(capitalizedName + 'ViewController.swift', 'wb')
	writeVC(vc, capitalizedName)

	protocol = open(capitalizedName + 'Protocol.swift', 'wb')
	writeProtocol(protocol, capitalizedName)

	presenter = open(capitalizedName + 'Presenter.swift', 'wb')
	writePresenter(presenter, capitalizedName)

def writeVC(file, name):
	print 'Start writing view controller'
	# Headers
	file.write('//\n//  ' + name + 'ViewController.swift\n//\n//  Template created by Edouard Libion on 30/12/16.\n//  Copyright © 2016 Edouard Libion. All rights reserved.\n//  Check my github for more cool stuff about IOS: https://github.com/edouardlib\n//')
	# Class declaration
	file.write('\n\nclass ' + name +'ViewController: BaseViewController, '+ name +'Protocol\n{')
	# Properties & bindings
	file.write('\n    //\n    // Properties\n    //\n\n    private let mPresenter = ' + name + 'Presenter()\n\n    //\n    // Binding views\n    //\n\n')
	# Life cycle
	file.write('    //\n    // Life cycle\n    //\n    \n    override func loadView() {\n        super.loadView()\n        self.view.addSubview(Bundle.main.loadNibNamed("' + name + 'View", owner: self, options: nil)?[0] as! UIView)\n    }    \n\n    override func viewDidLoad() {\n        super.viewDidLoad()\n        mPresenter.attachView(view: self)\n	}\n')
	# Acttions & methods implementation limiters
	file.write('    //\n    // Actions\n    //\n\n    //\n    // View methods implementation\n    //')		
	# end file
	file.write('\n}')
	file.close()

def writeProtocol(file, name):
	print 'Start writing protocol'
        # Headers
        file.write('//\n//  ' + name + 'ViewController.swift\n//\n//  Template created by Edouard Libion on 30/12/16.\n//  Copyright © 2016 Edouard Libion. All rights reserved.\n//  Check my github for more cool stuff about IOS: https://github.com/edouardlib\n//')
 	# Class declaration
        file.write('protocol '+ name +'Protocol: NSObjectProtocol {\n')
	# end file
        file.write('\n}')
	file.close()

def writePresenter(file, name):
	print 'Start writing presenter'
        # Headers
        file.write('//\n//  ' + name + 'ViewController.swift\n//\n//  Template created by Edouard Libion on 30/12/16.\n//  Copyright © 2016 Edouard Libion. All rights reserved.\n//  Check my github for more cool stuff about IOS: https://github.com/edouardlib\n//')
 	# Class declaration
        file.write('class ' + name + 'Presenter {\n\n')
        # Methods
	file.write('    var disposeBag = DisposeBag()\n\n\n    func attachView(view:'+ name + 'Protocol){\n        viewController = view\n    }\n    \n    func detachView() {\n        viewController = nil\ı\ı    }')
	# end file
        file.write('\n}')
	file.close()


if __name__ == '__main__':
    build()
