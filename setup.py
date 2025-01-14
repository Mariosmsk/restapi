from distutils.core import setup
import os

name = 'restapi'
pckgs = []
for root,dirs,files in os.walk(name):
    if '__init__.py' in files:
        pckgs.append(name + '.'.join(root.split(name)[-1].split(os.sep)))
        
setup(name=name,
      version='0.1',
      description='Package for working with ArcGIS REST API',
      author='Caleb Mackey',
      author_email='calebma@bolton-menk.com',
      url='https://github.com/Bolton-and-Menk-GIS/restapi',
      license='GPL',
      packages=pckgs,
      package_dir={name: name},
      package_data={name: ['shapefile/*.json',
                                'test/*.py',
                                'admin/samples/*.py']},
      install_requires=['munch', 'requests']
)
