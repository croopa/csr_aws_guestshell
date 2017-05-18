from distutils.core import setup
project_name = 'csr_aws_guestshell'
project_ver = '0.0.2'
setup(
    name=project_name,
    packages=[project_name],  # this must be the same as the name above
    version=project_ver,
    description='A helper library for Cisco guestshell on AWS',
    author='Christopher Reder',
    author_email='creder@cisco.com',
    scripts=["bin/get-metadata.py", "bin/get-route-table.py"],
    # use the URL to the github repo
    url='https://github.com/CiscoDevNet/' + project_name,
    download_url='https://github.com/CiscoDevNet/' + project_name + '/archive/' + \
        project_ver + '.tar.gz',
    keywords=['cisco', 'aws', 'guestshell'],
    classifiers=[],
    license="MIT",
    install_requires=[
        'awscli',
        'boto',
        'boto3',
    ],
)