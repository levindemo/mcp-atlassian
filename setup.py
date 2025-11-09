from setuptools import setup, find_packages
import os


# 读取项目根目录下的 README.md 文件作为 long_description
# 这样做是一个好习惯，尤其是当你打算将包发布到 PyPI 时
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
    # --- 项目基本信息 ---
    name="your_project_name",  # 【重要】你的项目名称，将来安装后用这个名字导入
    version="0.1.0",  # 【重要】项目版本号，遵循语义化版本规则
    author="Your Name",  # 你的名字
    author_email="your.email@example.com",  # 你的邮箱
    description="A brief description of your project",  # 项目的简短描述
    long_description=read('README.md'),  # 项目的详细描述，通常来自 README.md
    long_description_content_type="text/markdown",  # 详细描述的格式
    url="https://github.com/yourusername/your_project_name",  # 项目的主页链接 (如 GitHub)
    license="MIT",  # 项目的许可证

    # --- 包结构配置 ---
    # 告诉 setuptools 你的代码在 'src' 目录下
    package_dir={'': 'src'},

    # 自动发现 'src' 目录下所有的 Python 包
    # 一个包是指包含 __init__.py 文件的文件夹
    packages=find_packages(where='src'),

    # 如果你的项目有数据文件（如配置文件、模板等）需要一起打包
    # 你需要使用 package_data 或 data_files
    # package_data={
    #     'your_package_name': ['data/*.txt', 'templates/*.html'],
    # },

    # --- 依赖管理 ---
    # 列出你的项目所依赖的其他 Python 库
    # 当别人安装你的包时，pip 会自动安装这些依赖
    # install_requires=[
    #     "requests>=2.25.1",
    #     "numpy>=1.19.5",
    # ],

    # --- 入口点（可选，但非常有用）---
    # 如果你想让你的项目可以通过命令行直接运行，可以在这里配置
    # entry_points={
    #     'console_scripts': [
    #         'your_command_name = your_package_name.main:main_function',
    #     ],
    # },

    # --- 分类信息（推荐）---
    # 这些信息有助于在 PyPI 上对包进行分类
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # 根据你的项目情况添加更多分类器
        # 完整列表见: https://pypi.org/classifiers/
    ],

    # 指定项目支持的 Python 版本
    python_requires='>=3.8',  # 根据你的项目实际情况修改
)