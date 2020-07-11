from setuptools import setup, find_packages

setup(
    name='pycmd',  # 包名字
    version='0.13',  # 包版本
    description='python命令行程序',  # 简单描述
    author='何韦澄',  # 作者
    author_email='hezhefly@163.com',  # 作者邮箱
    url='/',  # 包的主页
    install_requires=["fire", "lxml", "requests"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fpip = pycmd:fpip',
            'youdict = pycmd:youdict',
            'nora = pycmd:nora',
        ]
    }
)
